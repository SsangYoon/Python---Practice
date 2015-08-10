# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 10.
@attention: Dictionary_Practice of Python_Practice
@author: Sangyun
'''

#Dictionary의 기본적인 모습 
#{Key1:Value1, Key2:Value2, Key3:Value3 ...}

#Dictionary를 만들어보자
Dictionary_0 = {"Name" : "Sangyoon", "Height" : 177, "Weight" : "Unlimited"}
Dictionary_1 = {"List" : [1, 2], "Tuple" : (2, 3)}
Dictionary_2 = {1 : "One", 2 : "Two"}

#Dictionary는 순서가 없다
#무엇이 있느냐가 중요하다 
print (Dictionary_0)        # {'Name': 'Sangyoon', 'Weight': 'Unlimited', 'Height': 177}
print (Dictionary_1)        # {'List': [1, 2], 'Tuple': (2, 3)}
print (Dictionary_2)        # {1: '1', 2: '2'}

#중복된 Key를 넣게 된다면 나중에 대입된 Value로 덮여 씌워진다
Wrong_Dictionary_0 = {1 : '1', 1 : 'One'}
print (Wrong_Dictionary_0)      # {1: 'One'}

#Dictionary 인덱싱
#Key를 이용하여 Value를 얻을 수 있다 
#존재하지 않는키로 인덱싱 하면 에러를 발생시키지만
#get함수에 존재하지 않는 키를 대입하면 None을 반환한다 
print (Dictionary_0["Name"])        # Sangyoon
print (Dictionary_1["List"][0])     # 1
print (Dictionary_2[1])             # One
print (Dictionary_0.get("Name"))    # Sangyoon
print (Dictionary_0.get("NO_KEY"))  # None


#Dictionary에 쌍을 추가하기
#Dictionary[Key] = Value로 이루어진
Add_Dictionary = {1 : "One", 2 : "Two"}
Add_Dictionary[3] = "Three"
Add_Dictionary[4] = "Four"
Add_Dictionary["Five"] = 5
Add_Dictionary[67] = "Six Seven"

#Dictionary는 순서가 없기때문에 추가도 지맘대로 된다 
print (Add_Dictionary)      # {1: 'One', 2: 'Two', 67: 'Six Seven', 4: 'Four', 3: 'Three', 'Five': 5}

#Dictionary 요소 삭제
#del Dictionary[Key]하면 Key : Value쌍이 삭제된다 
Delete_Dictionary = {"Name" : "Sangyoon", "Old" : 18}
del Delete_Dictionary["Old"]
print (Delete_Dictionary)       # {'Name': 'Sangyoon'}

#Key, Value리스트 만들기
print (Dictionary_0.keys())     # ['Name', 'Weight', 'Height']
print (Dictionary_0.values())   # ['Sangyoon', 'Unlimited', 177]

#Key : Value 쌍 얻기
print (Dictionary_0.items())  
#파이썬 버번에 따라 결과가 다르다 
#Python 2.x ver -> [('Name', 'Sangyoon'), ('Weight', 'Unlimited'), ('Height', 177)]
#Python 3.x ver -> dict_items([('Name', 'Sangyoon'), ('Weight', 'Unlimited'), ('Height', 177)])

#Dictionary 비우기
Dictionary_0.clear()
print (Dictionary_0)        # {}

#Dictionary에 해당 Key가 있는지 조사
Check_Dictionary = {1 : "One", "Two" : 2}
print (1 in Check_Dictionary)           # True        #2.x 버전은 True는 1 False는 0으로 출력된다고 한
print ("Two" in Check_Dictionary)       # True
print (3 in Check_Dictionary)           # False
