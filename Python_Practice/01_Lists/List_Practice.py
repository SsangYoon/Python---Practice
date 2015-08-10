# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 9.
@attention: List_Practice of Python_Practice
@author: Sangyun
'''

#리스트는 대괄호를 사용합니다
a = [1, 2, 4, 5, 6, 7]
b = [1, 2, 3, 4, 5, 'A', 'B', 'C']
c = ["Sangyoon", 1, 2, 'C']
d = [1, 2, 3, [4, 5], ["I`m", "Gay"]]
e = [1, 2, ["I`m", "Real", ["Gerate", "Gay"]]]
Empty_List_0 = []           #비어있는 리스트는 이렇게 생성합니다
Empty_List_1 = list()       #둘다 동일

print (a)                   # [1, 2, 4, 5, 6, 7]
print (b)                   # [1, 2, 3, 4, 5, 'A', 'B', 'C']
print (c)                   # ['Sangyoon', 1, 2, 'C']
print (d)                   # ['Sangyoon', 1, 2, 'C']
print (e)                   # [1, 2, ['I`m', 'Real', ['Gerate', 'Gay']]]
print (Empty_List_0)        # []
print (Empty_List_1)        # []

#리스트도 문자열과 마찬가지로 인덱싱과 슬라이싱이 된다
#리스트 인덱싱 
print (d[0])        # 1
print (d[-1])       # ['I`m', 'Gay']
print (d[-1][0])    # I`m
print (d[-1][-1])   # Gay
print (e[2][2][1])  # Gay

#리스트 슬라이싱
Temp = a[2:5]
print (Temp)        # [4, 5, 6]
Temp = d[:-1]
print (Temp)        # [1, 2, 3, [4, 5]]
Temp = e[2:]
print (Temp)        # [['I`m', 'Real', ['Gerate', 'Gay']]]

#리스트 합치기, 반복하기
print (a * 3)       # [1, 2, 4, 5, 6, 7, 1, 2, 4, 5, 6, 7, 1, 2, 4, 5, 6, 7]
print (a + e)       # [1, 2, 4, 5, 6, 7, 1, 2, ['I`m', 'Real', ['Gerate', 'Gay']]]

#리스트는 문자열과 다르게, 수정,삭제가 가능하다
#리스트 수정 
Change_List = [1, 2, 3, "I`m", "Gay"]
Change_List[3:5] = ["I`m Gay"]
print (Change_List)

#리스트 삭제
Delete_List_0 = [1, 2, 3, "Lottelia"]
del Delete_List_0[3]
print (Delete_List_0)       # [1, 2, 3]

Delete_List_1 = [1, 2, 3, "Lotte", "Lia"]
Delete_List_1[3:5] = []     # del Delete_List_1[3:5]도 같은 표현 
print (Delete_List_1)       # [1, 2, 3]

Delete_List_2 = [1, 2, 3]
Delete_List_2[-1] = []      # 삭제가아닌 비어있는 리스트로 수정한다고 해석함 
print (Delete_List_2)       # [1, 2, []]


#리스트관련 함수들
#리스트에 요소 이어 붙이
Append_List_0 = [1, 2, 3, 4]
Append_List_0.append(5)
print (Append_List_0)         # [1, 2, 3, 4, 5]

Append_List_1 = [1, 2, 3, 4]
Append_List_1.append([5, 6, 7, 8])
print (Append_List_1)           # [1, 2, 3, 4, [5, 6, 7, 8]]

#Sort (정렬)
Sort_List = [1, 3, 4, 9, 7]
Sort_List.sort()                #디펄트값이 알아서 들어가므로 괄호안을 비워줘도 된다
print (Sort_List)               # [1, 3, 4, 7, 9]

#Reverse (뒤집기) 순서대로 정령하고 다시 뒤집는게 아니라 그냥 뒤집는 
Reverse_List = [5, 1, 2, 3, 8]
Reverse_List.reverse()
print (Reverse_List)        # [8, 3, 2, 1, 5]

#Index (위치반환)
Index_List = [1, 2, 5]
print (Index_List.index(5))     # 2

#Insert (요소 삽입)
Insert_List = [2, 3, 4]
Insert_List.insert(0, 1)        # 0위치에 1을 삽입
print (Insert_List)             # [1, 2, 3, 4]

#Remove (요소제거)
#remove(value)는 첫번째 나오는 value만 삭제한다 
Remove_List = [1, 2, 3, 3, 3]
Remove_List.remove(3)
print (Remove_List)         # [1, 2, 3, 3]

#Pop (마지막 요소 반환)
Pop_List = [1, 2, 3, 'A', 'B', 'C']
print (Pop_List.pop())      # C

#Count (요소 갯수 세기)
#count(value)는 value가 리스트안에 몇개있는지 세어준
Count_List = [1, 2, 3, 4, 5, 6, 1, 2]
print (Count_List.count(1)) # 2

#Extend (리스트 확장하기)
Extend_List = ["A", "B", "I`m Gay"]
Extend_List.extend(["Real", "Gay"])       # Extend_List += ["Real", "Gay"]와 같
print (Extend_List)         # ['A', 'B', 'I`m Gay', 'Real', 'Gay']

#내려쓰기 된다 오
asdf = [["I`m", "Real", "Gay"],
        ["How", "About", "You?"],]

print (asdf[0][0:3])        # ['I`m', 'Real', 'Gay']
print (asdf[1][0:3])        # ['How', 'About', 'You?']


