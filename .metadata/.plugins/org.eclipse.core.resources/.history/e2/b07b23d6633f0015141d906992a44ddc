# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 10.
@attention: Tuple_Practice of Python Practice
@author: Sangyun
'''
''

#Tuple의 특징 
#1. List와 똑같은데, 값을 지우거나 변경하지 못한
#2. []말고 ()를 써서 만든 다는 

#Tuple을 만들어보자
Tuple_0 = (1, 2, 3)
Tuple_1 = 1, 2, 3           # Tuple_0과 동일하
Tuple_2 = (1,)              # 튜플의 요소가 한개일 때는 뒤에 콤마(,)를 붙이지 않으면 일반변수로 생성된다
Tuple_3 = (2, 3, "GAY")
Tuple_4 = (1, 2, (3, 4))

Not_Tuple = (1)             # 위에서 설명했듯이 일반 변수로 인식한

#Tuple은 List와 다르게 출력될 때 ()로 감싸진다
print (Tuple_0)             # (1, 2, 3)
print (Tuple_1)             # (1, 2, 3)
print (Tuple_2)             # (1,)
print (Tuple_3)             # (2, 3, 'GAY')
print (Tuple_4)             # (1, 2, (3, 4))

Tuple_List = (1, 2, [3, 4])     # Tuple안에 List가 있다
Tuple_List[2][0] = 1            # List로 감싸진 값은 수정이 가능하다 
#Tuple_List[0] = 2              # 하지만 Tuple로 감싸진 값은 수정이 불가능하다 
print (Tuple_List)              # (1, 2, [1, 4])

