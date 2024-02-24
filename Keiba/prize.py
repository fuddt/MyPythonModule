# 賞金の表
from abc import ABC, abstractmethod
import pickle

"""
JRDBの成績データから獲得賞金を計算する (未完成)
"""

#日本の地名
with open('./Japanese_place_names.pkl','rb') as data:
    ja_place_names = pickle.load(data)

class Components(ABC):
    """
    各馬6着以下の場合は何かしらの手当が出る。
    """
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def prize(self):
        pass
    
    @abstractmethod
    def validation_type(self):
        pass

class RaceIncentive(Components):
    def validation_type(self):
        "型の合わせ"
        dtype = {'条件': str,
                '着順': int}
        for k, v in dtype.items():
            self.data[k] = v(self.data[k])
            
    def prize(self):      
        if self.data['条件'] == 'OP':
            if self.data['着順'] >= 11:
                return 0
            incentive = {
                6:0.8,
                7:0.7,
                8:0.6,
                9:0.3,
                10:0.2,
                }
        else:
            if self.data['着順'] >= 10:
                return 0
            incentive = {
                6:0.8,
                7:0.7,
                8:0.6,
                9:0.3,
                 }
        return incentive[self.data['着順']]
    
class RaceIncentiveReductionRate(Components):
    def validation_type(self):
        "型の合わせ"
        dtype = {'条件': str,
                 '芝ダ障害コード': str,
                '距離': int,
                '1(2)着タイム差':float,
                '着順': int
                }
        for k, v in dtype.items():
            self.data[k] = v(self.data[k])
            
    def race_incentive_reduction_race_requirements_A1_A3(self, data):
        # 芝
        if (data['条件'] == ('A1' or 'A3')) and \
            (data['芝ダ障害コード'] == '1') and \
            ((data['距離'] <= 1400) or ( 1400 < data['距離'] < 2000))and\
            (3 < data['1(2)着タイム差']):
            return 0

        elif (data['条件'] == ('A1' or 'A3')) and \
             (data['芝ダ障害コード'] == '1') and \
             (2000 <= data['距離'])and\
             (4 < data['1(2)着タイム差']):
             return 0
        #ダート          
        elif (data['条件'] == ('A1' or 'A3')) and \
            (data['芝ダ障害コード'] == '2') and \
            ((data['距離'] <= 1400) or ( 1400 < data['距離'] < 2000))and\
            (4 < data['1(2)着タイム差']):
            return 0
        elif (data['条件'] == ('A1' or 'A3')) and \
             (data['芝ダ障害コード'] == '2') and \
             (2000 <= data['距離'])and\
             (5 < data['1(2)着タイム差']):
             return 0
        return 1.0
    #--------A1,A3以外
    def race_incentive_reduction_race_requirements_not_A1_A3(self, data):
        # 芝
        if (data['条件'] != ('A1' or 'A3')) and \
            (data['芝ダ障害コード'] == '1') and \
            ((data['距離'] <= 1400) or ( 1400 < data['距離'] < 2000))and\
            (3 < data['1(2)着タイム差']):
            return 0

        elif (data['条件'] != ('A1' or 'A3')) and \
            (data['芝ダ障害コード'] == '1') and \
            ( 1400 < data['距離'] < 2000)and\
            (4 < data['1(2)着タイム差']):
            return 0

        elif (data['条件'] != ('A1' or 'A3')) and \
             (data['芝ダ障害コード'] == '1') and \
             (2000 <= data['距離'])and\
             (4 < data['1(2)着タイム差']):
             return 0
        #ダート          
        elif (data['条件'] == ('A1' or 'A3')) and \
            (data['芝ダ障害コード'] == '2') and \
            (data['距離'] <= 1400)and\
            (4 < data['1(2)着タイム差']):
            return 0

        elif (data['条件'] != ('A1' or 'A3')) and \
            (data['芝ダ障害コード'] == '2') and \
            ( 1400 < data['距離'] < 2000)and\
            (5 < data['1(2)着タイム差']):
            return 0

        elif (data['条件'] != ('A1' or 'A3')) and \
             (data['芝ダ障害コード'] == '2') and \
             (2000 <= data['距離'])and\
             (6 < data['1(2)着タイム差']):
             return 0
        return 1.0
    
    def prize(self):
        if self.data['着順'] <= 5:
            return 0
        else:
            pass
        
        #タイム差3秒以上であれば次のステップ
        if self.data['1(2)着タイム差'] >3:
            pass
        else:
            return 1.0
        
        #条件がA1もしくはA3,またはそれ以外
        if self.data['条件'] == ('A1' or 'A3'):
            return self.race_incentive_reduction_race_requirements_A1_A3(self.data)
        else:
            return self.race_incentive_reduction_race_requirements_not_A1_A3(self.data)
    
class SpecialRaceIncentive(Components):
    def validation_type(self):
        "型の合わせ"
        dtype = {
                '着順': int
                }
        for k, v in dtype.items():
            self.data[k] = v(self.data[k])
            
    def prize(self):
        if 11 <= self.data['着順'] :           
            if self.data['レース名'] in ['大阪杯','天皇賞（春）','宝塚記念','天皇賞（秋）','ジャパンカップ','有馬記念']:
                return 200
            elif self.data['レース名'] in ['フェブラリーステークス','高松宮記念','ヴィクトリアマイル',\
                                          '安田記念','スプリンターズステークス','エリザベス女王杯','マイルチャンピオンシップ',\
                                          'チャンピオンズカップ']:
                return 150
            else:
                pass
        return 0

class SpecialRaceIncentive2(Components):
    def validation_type(self):
        "型の合わせ"
        dtype = {
                '着順': int,
                'グレード': str,
                '種別': str,
                '収得賞金' : int,
                '距離': int
                }
        for k, v in dtype.items():
            self.data[k] = v(self.data[k])
            
    def prize(self):
        if 11 <= self.data['着順'] :
            pass
        else:
            return 0
        
        if (self.data['グレード'] == '2'):
            pass
        else:
            return 0
        
        if self.data['種別'] == ('12' or '13' or '14'):
            pass
        else:
            return 0
        
        if 1800 <= self.data['距離']:
            pass
        else:
            return 0
        
        if 1600 < self.data['収得賞金']:
            return 100
        else:
            return 50

class SpecialRaceAllowance(Components):
    def validation_type(self):
        "型の合わせ"
        dtype = {
                'グレード': str,
                '種別': str,
                '距離': int
                }
        for k, v in dtype.items():
            self.data[k] = v(self.data[k])
            
    def prize(self):
        base = 47
        if (self.data['種別'] == '11') and (self.data['グレード'] == ''):
            add = 3
        elif (self.data['種別'] == ('12' or '13' or '14')) and \
             (self.data['グレード'] == '') and \
             (1800 <= self.data['距離']):
            add = 6
        else:
            add = 0
        return base + add 

class SpecialRaceAllowanceReductionRate(Components):
    def validation_type(self):
        "型の合わせ"
        dtype = {
                '収得賞金': int,
                '年齢': float,
                }
        for k, v in dtype.items():
            self.data[k] = v(self.data[k])
            
    def prize(self):
        if 5 <= self.data['年齢']:
            pass
        else:
            return 1.0
        
        if (5 <= self.data['年齢']) and (self.data['収得賞金'] < 200):
            return 0.5
        elif (5 <= self.data['年齢']) and (200<= self.data['収得賞金'] <= 500):
            return 1.0
        elif (6 <= self.data['年齢']) and (200<= self.data['収得賞金'] <= 500):
            return -12
        else:
            return 1.0
    
class SpecialRaceAllowanceReductionRate2(Components):
    def validation_type(self):
        "型の合わせ"
        dtype = {
                '1(2)着タイム差': float,
                '着順': int,
                '条件': str,
                }
        for k, v in dtype.items():
            self.data[k] = v(self.data[k])
            
    def prize(self):
        if self.data['着順'] <= 9:
            return 1.0
        else:
            pass
        
        if (9 <= self.data['着順']) and (3< self.data['1(2)着タイム差']):
            pass
        else:
            return 1.0
        branch_func = RaceIncentiveReductionRate(self.data)
        if self.data['条件'] == ('A1' or 'A3'):
            value = branch_func.race_incentive_reduction_race_requirements_A1_A3(self.data) 
            if value == 0:
                return 0.5
            else:
                return 1.0
        else:
            value = branch_func.race_incentive_reduction_race_requirements_not_A1_A3(self.data)
            if value == 0:
                return 0.5
            else:
                return 1.0

class DistanceAllowance(Components):
    def validation_type(self):
        "型の合わせ"
        dtype = {
                'グレード': str,
                '距離': int,
                '着順': int,
                '条件': str
                }
        for k, v in dtype.items():
            self.data[k] = v(self.data[k])
            
    def branch(self, data, value_1, value_2, value_3):
        if data['距離'] <= 1800:
            return value_1
        elif (1800 < data['距離']) and (data['距離'] < 2000):
            return value_2
        else:
            return value_3
              
    def prize(self):
        rate = {
            1:1.0,
            2:0.4,
            3:0.25,
            4:0.15,
            5:0.10,
            6:0.08,
            7:0.07,
            8:0.06,
            9:0.03,
            10:0.02
               } 
              
        if self.data['着順'] <= 10:
            pass
        else:
            return 0
        
        if (self.data['条件'] == 'OP') and (self.data['グレード'] != '4'):
            base = self.branch(self.data, 140, 260, 380)
        elif (self.data['条件'] in ['8', '9', '10', '15', '16']) and ():
            base = self.branch(self.data, 140, 260, 380)
        elif (self.data['条件'] in ['04', '05']) and (self.data['グレード'] == '5'):
            base = self.branch(self.data, 80, 140, 200)
        else:
            base = 0    
        return base*rate[self.data['着順']]
            
class DomesticHorseEncouragementAward(Components):
    def validation_type(self):
        "型の合わせ"
        dtype = {
                'グレード': str,
                '年齢': float,
                '条件': str
                }
        for k, v in dtype.items():
            self.data[k] = v(self.data[k])
            
    def prize(self):
        rate = {
            1:1.0,
            2:0.4,
            3:0.25,
            4:0.15,
            5:0.10,
            6:0.06,
            7:0.04
        }
        if self.data['着順'] <= 7:
            pass
        else:
            return 0
        # #　内国産馬かどうかの判別のために、産地名が日本の地名かどうかを判別。
        # with open('Japanese_place_names.pkl','rb') as data:
        #     ja_place_names = pickle.load(data)
        
        if self.data['産地名'] in ja_place_names:
            pass
        else:
            return 0

        if (self.data['条件'] == ('A1' or 'A3')) and (self.data['年齢'] == 2):
            base = 200
        elif (self.data['条件'] == ('A1' or 'A3')) and (self.data['年齢'] == 3):
            base = 170
        elif (self.data['条件'] == ('04' or '05')) and (3 <= self.data['年齢'] ):
            base = 90
        elif (self.data['条件'] == ('04' or '05')) and (self.data['年齢'] < 3):
            base = 120
        elif (self.data['条件'] == ('08' or '09')):
            base = 150
        elif (self.data['条件'] == ('15' or '16')):
            base = 160
        elif (self.data['条件'] == 'OP') and (self.data['グレード'] == '5'):
            base = 200
        elif self.data['グレード'] == '6':
            base = 220
        elif self.data['グレード'] in ['2', '3', '4']:
            base = 250
        elif self.data['グレード'] == '1':
            base = 350
        else:
            base = 0
        return base*rate[self.data['着順']]

class Prize(object):
    def __init__(self):
        self.amount = 0
        self.prize_1to5 = dict(zip([1,2,3,4,5],['１着賞金', '２着賞金', '３着賞金', '４着賞金', '５着賞金']))
    def sum(self, data):
        #データフレームをSeriesにする念の為の処理
        data = data.loc[data.index[0],:].copy()
        
        #競走中止は0 なので修正する。
        if data['着順'] == 0:
            data['着順'] = 18
        else:
            pass
        
        if data['着順'] >5:
            objs = [
                RaceIncentive(data),
                RaceIncentiveReductionRate(data),
                SpecialRaceIncentive(data),
                SpecialRaceIncentive2(data),
                SpecialRaceAllowance(data),
                SpecialRaceAllowanceReductionRate(data),
                SpecialRaceAllowanceReductionRate2(data),
                DistanceAllowance(data),
                DomesticHorseEncouragementAward(data),
                ]
            prizes=[]
            for obj in objs:
                obj.validation_type()
                prizes.append(obj.prize())
            
            race_incentive = prizes[0] * prizes[1]
            special_race_incentive = prizes[2] + prizes[3]
            # 特別出走手当のみ 定率と定額での減額があるので条件分岐する。
            if prizes[5] < 0.0: 
                special_race_incentive_allowance = (prizes[4]+prizes[5])*prizes[6]
            else:
                special_race_incentive_allowance = prizes[4]*prizes[5]*prizes[6]
            distance_allowance = prizes[7]
            domestic_horse_encouragement_award = prizes[8]
            self.amount = race_incentive + special_race_incentive + special_race_incentive_allowance + \
                        distance_allowance + domestic_horse_encouragement_award
        else:
            #5着以内であれば、そのレースの賞金の金額。
            columns = self.prize_1to5[data['着順']]
            self.amount = data[columns]