# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 10.
@attention: Sets_Practice of Python_Practice
@author: Sangyun
'''

#Sets == 집합 / Python 2.3버전부터 추가되었다고 한다
#Sets의 특징 
#1. 중복을 허용하지 않는 점 
#2. 순서가 없는 점 -> 순서가 없기 때문에 인덱싱을 지원하지않음 
#Sets의 이러한 중복을 허용하지 않는 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용되기도 한다.

#Sets를 만들어보자
#set키워드를 사용해서 Sets자료형을 만들 수 있다
Value = "asdfasdf"
Sets_0 = set([1,2,3])
Sets_1 = set("Hello Gay")
Sets_2 = set(Value)

print (Sets_0)
print (Sets_1)
print (Sets_2)
#Python버전에 따라 출력이 다르다 
#2.x버전 출력========================================
# set([1, 2, 3])
# set(['a', ' ', 'e', 'G', 'H', 'l', 'o', 'y'])
# set(['a', 's', 'd', 'f'])
#3.x버전 출력========================================
# [1, 2, 3]
# ['a', ' ', 'e', 'G', 'H', 'l', 'o', 'y']
# ['a', 's', 'd', 'f']

#교집합, 합집합, 차집합
A_Sets = {1, 2, 3, 4, 5}
B_Sets = {3, 4, 5, 6, 7}
print (A_Sets & B_Sets)
print (A_Sets | B_Sets)
print (A_Sets - B_Sets)

#Python버전에 따라 출력이 다르다
#2.x버전 출력========================================
#set([3, 4, 5])
#set([1, 2, 3, 4, 5, 6, 7])
#set([1, 2])
#3.x버전 출력========================================
#{3, 4, 5}
#{1, 2, 3, 4, 5 ,6, 7}
#{1, 2}




