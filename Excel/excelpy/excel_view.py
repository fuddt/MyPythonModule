# Excelに合わせてデータフレームを作成
import pandas as pd
import openpyxl


class ExcelView:
    """
    how to use:

    #Excelファイルを読み込む
    ev = ExcelView('sample.xlsx')

    -------------------------------------------
    #Excelの列名と行番号に準じた形式で表示したい
    ・行番号は1から始まる
    ・列名はAから始まる

    ev.view_sheet('Sheet1', format='excel')
    >>
            A	        B	        C	    D	
    1	RecordSpec	DataKubun	MakeDate	Year	
    2	SE	            A	    20050303	1987	
    3	SE	            A	    20060508	1987	
    4	SE	            A	    20050303	1987	
    
    -----------------------------------------------
    #pandasのDataFrameに準じた形式で表示したい
    ・行番号は0から始まる
    ・列名は1行目のデータに準じる
    ev.view_sheet('Sheet1', format='pandas')
    >>
        DataKubun	MakeDate	Year	MonthDay	
    0	A	        20050303	1987	0519	
    1	A	        20060508	1987	0602	
    2	A	        20050303	1987	0615

    -----------------------------------------------
    #openpyxlの公式ドキュメント推奨の方法で表示したい
    ev.view_sheet('Sheet1', format='reference')
    ・行は1列目のデータに準じる
    ・列は1行目のデータに準じる
    >>
        DataKubun	MakeDate	Year	MonthDay	
    SE	A	        20050303	1987	0519	    
    SE	A	        20060508	1987	0602	    
    """
    
    def __init__(self, filename: str):
        self.workbook = openpyxl.load_workbook(filename)

    def view_sheet(self, sheet_name: str, format_type: str = 'reference') -> pd.DataFrame:
        if sheet_name not in self.workbook.sheetnames:
            raise ValueError(f'Sheet {sheet_name} が見つかりません。')

        sheet = self.workbook[sheet_name]
        if format_type == 'excel':
            return self._view_sheet_as_excel(sheet)
        elif format_type == 'pandas':
            return self._view_sheet_as_pandas(sheet)
        elif format_type == 'reference':
            return self._view_sheet_as_reference(sheet)
        else:
            raise ValueError(f'Format {format_type} はサポート対象外です。')
        
    @staticmethod
    def _to_excel_column_name(n: int) -> str:
        """Excelの列名に変換する関数。ASCIIコードでは、65は文字「A」を表す。"""
        string = ""
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            string = chr(65 + remainder) + string
        return string
    
    def _view_sheet_as_excel(self, sheet) -> pd.DataFrame:
        data = list(sheet.values)
        column_names = [self._to_excel_column_name(i) for i in range(1, len(data[0]) + 1)]
        df = pd.DataFrame(data[1:], 
                          columns=column_names, 
                          index=pd.RangeIndex(start=1, stop=len(data)+1))
        return df

    def _view_sheet_as_pandas(self, sheet) -> pd.DataFrame:
        data = list(sheet.values)
        return pd.DataFrame(data[1:], columns=data[0])

    def _view_sheet_as_reference(self, sheet) -> pd.DataFrame:
        data = list(sheet.values)
        index = [r[0] for r in data[1:]]  # Skip header for index
        return pd.DataFrame(data[1:], columns=data[0], index=index)