import pandas as pd
import polars as pl


class ApacheLogReader(object):
    @classmethod
    def read_log(cls, logFilePath: str):
        log = pl.read_csv(logFilePath, 
                                  has_header=False, 
                                  separator=" ",
                                  ignore_errors = True,
                                  infer_schema_length=10000, 
                                  truncate_ragged_lines=True,
                                  new_columns=['IPaddress', 'Ignore1', 'Ignore2', 'DateTime', 'ignore3','URL', 
                                                'HTTPSTATE', 'ResponseSize', 'RequestProcessingTime', 
                                                'Referer', 'UserAgent', 'transmissionSize', 'Cookie', 'Ignore3'])
        log = log.select(['IPaddress', 'DateTime', 'URL', 
                        'HTTPSTATE', 'ResponseSize', 'RequestProcessingTime', 
                        'Referer', 'UserAgent', 'transmissionSize', 'Cookie'])
        log = cls._process_datetime(log)
        log = cls._process_url(log)
        return log
    
    @staticmethod
    def _process_datetime(df: pl.DataFrame) -> pl.DataFrame:
        return df.with_columns([
            pl.col('DateTime').str.slice(1, 2).alias('Day'),
            pl.col('DateTime').str.slice(13).alias('Time'),
            # その他の日付関連の処理が必要な場合はここに追加
        ])

    @staticmethod
    def _process_url(df: pl.DataFrame) -> pl.DataFrame:
        # URL列をスペースで分割し、新しい列を追加
        split_url = df.select(pl.col('URL').str.split(' ', inclusive=False).alias('split_url'))
        return df.with_columns([
                                split_url['split_url'].arr.get(0).alias('GET_POST'),
                                split_url['split_url'].arr.get(1).alias('URL')
                            ]).drop(['split_url'])

class ApacheLog(object):
    def __init__(self, logFilePath: str):
        self.logFile = ApacheLogReader.read_log(logFilePath)

    def __str__(self) -> str:
        return str(self.logFile)

    #日付でフィルター
    def filter_by_day(self, day: str) -> pl.DataFrame:
        day = int(day)
        return (self.logFile.with_columns(pl.col("Day").cast(pl.Int32))
                            .filter(pl.col("Day") == day))
    # 時間でフィルター
    def filter_by_time(self, from_time: str, end_time: str) -> pl.DataFrame:
        filter_jouken1 = (pl.col("Time") >= from_time)
        filter_jouken2 = (pl.col("Time") <= end_time)
        return self.logFile.filter(filter_jouken1 & filter_jouken2)
    
    # CSVファイルに出力
    def to_csv(self, filePath: str):
        self.logFile.write_csv(filePath)
