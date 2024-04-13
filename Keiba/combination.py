
import numpy as np
from abc import ABC,abstractmethod

def validation(horse_num):
    if type(horse_num) in (str, int, list, np.ndarray):
        pass
    else:
        raise TypeError("list, int, str, numpy.ndarrayのいずれかで渡してください。")


class Combination(ABC):
  """
  引数のパターン
  list, numpy.ndarray,int, strが可能
  """
  def __init__(self,horse_num):
    #単純に出走頭数から全通りを計算するとき
    if type(horse_num) != list and not isinstance(horse_num,np.ndarray):
        horse_num = int(horse_num)
        horse_num = list(range(1, horse_num + 1))

    #指定した馬番から組み合わせを構築する場合
    if type(horse_num) == list:
        horse_num = [int(num) for num in horse_num]
    else:
        horse_num = horse_num.astype(int)
    horse_num.sort()
    self.horse_num = np.array(horse_num)

  @abstractmethod
  def combination_ticket(self):
    pass

class CombinationBracketQuinella(Combination):
  def combination_ticket(self):
    if len(self.horse_num) <= 7:
      return False

    waku = [i for i in range(1,9)]
    combination = []
    for index,first in enumerate(waku):
      for second in waku[index:]:
        combination.append(str(first) + '-' + str(second))
    return combination

class CombinationQuinella(Combination):
  def combination_ticket(self):
    combination = []
    for first in self.horse_num:
      for second in  self.horse_num[first:]:
        combination.append(str(first) + '-' + str(second))
    return combination

class CombinationExacta(Combination):
  def combination_ticket(self):
    combination = []
    for _,first in enumerate(self.horse_num):
      for second in self.horse_num[self.horse_num != first]:
        combination.append(str(first) + '-' + str(second))
    return combination

class CombinationQuinellaPlace(CombinationQuinella):
  pass

class CombinationTrio(Combination):
  def combination_ticket(self):
    combination = []
    for first in self.horse_num:
      for second in self.horse_num[first:-1]:
        for third in self.horse_num[second:]:
          combination.append(str(first) + '-' + str(second) + '-' + str(third))
    return combination

class CombinationTrifecta(Combination):
  def combination_ticket(self):
    combination = []
    for _,first in  enumerate(self.horse_num):
      for _,second in enumerate(self.horse_num[self.horse_num != first]):
        for _,third in enumerate(self.horse_num[(self.horse_num != first) &(self.horse_num != second)]):
          combination.append(str(first) + '-' + str(second) + '-' + str(third))
    return combination


class TicketCombination(object):
  def combination_bracket(self,horse_num):
    return CombinationBracketQuinella(horse_num).combination_ticket()

  def combination_exacta(self,horse_num):
    return CombinationExacta(horse_num).combination_ticket()

#combination_quinella and quinella place is same
  def combination_quinella(self,horse_num):
    return CombinationQuinella(horse_num).combination_ticket()

  def combination_quinella_place(self,horse_num):
    return CombinationQuinella(horse_num).combination_ticket()
  
  def combination_trio(self,horse_num):
    return CombinationTrio(horse_num).combination_ticket()
  
  def combination_trifecta(self,horse_num):
    return CombinationTrifecta(horse_num).combination_ticket()

