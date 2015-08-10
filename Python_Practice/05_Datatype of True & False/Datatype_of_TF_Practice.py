# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 10.
@attention: 데이터 타입의 참과 거짓 
@author: Sangyun
'''

#변수의 참과 거짓을 판별할 함수 
def Checker(Value):
    if (Value) :        #전달받은 인자가 True면  
        print ("True")
    else :              #전달받은 인자가 False면 
        print ("False")
        
def String_Check():             
    Checker ("")                # False 
    Checker ("I`m Gay")         # True
    
def List_Check():
    Checker ([])                # False
    Checker ([1, 2, [3, 4]])    # True
    
def Tuple_Check():
    Checker (())                # False
    Checker ((1, 2, "Three"))   # True

def Dictionary_Check():
    Checker ({})                # False - 이건 Sets자료형으로 분류해야 할거 같네요 
    Checker ({1 : "One"})       # True

def Sets_Check():
    Checker ({})                # False
    Checker ({1, 2, "asdf"})    # True

def Intergel_Check():
    Checker (0)                 # False
    Checker (1)                 # True

def None_Check():
    Checker (None)
    
if __name__ == '__main__':
    String_Check ()
    List_Check ()
    Tuple_Check ()
    Dictionary_Check ()
    Sets_Check ()
    Intergel_Check ()
    None_Check ()
    
    
    
    
    
    