# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 13.
@attention: About Module 
@author: Sangyun
'''
# 참고 
# Unresolved Import 이 메세지는 왜 뜨는지 나도모름...
# 실행에 있어서는 크게 문제 되지는 않는듯 
# Eclipse - PyDev에서만 뜨는 것 일 수도 ....

import MyPythonModule       # MyPythonModule.py를 임포트시킴 (.py는 때야함) 

if __name__ == "__main__":
    MyPythonModule.HelloWorld()             # MyPythonModule.을 쓰지 않고 함수를 쓰고싶으면 
    from MyPythonModule import HelloWorld   # 이렇게 해주자 
    HelloWorld()                            # 올ㅋ 
    
    from MyPythonModule import *            # 그런데 클래스, 함수, 변수를 모두 MyPythonModule.을 떼서 쓰고싶으면, 이렇게 해주자
                                            # *은 모든것을 뜻한다 
    I = Person()
    I.Set_State("Sangyoon", 177, "Unlimited")
    I.Show_State()
          
# 대화형 인터프리터에서 경로 추가하기
# 이렇게 추가해놓으면 임포트 시킬 때마다 경로를 입력하는 짓을 안해도 된다   
# 계속 지정 되어있으니까 venv에서만 쓰자                            
# import sys
# sys.path.append("/Users/Sangyun/Documents/workspace/Python_Workspace/Python_Practice/13_Module")

# 이렇게 Path지정을 할 수도 있다 - 대화형 인터프리터에서 해야함 ㅇ 
# set PYTHONPATH = /Users/Sangyun/Documents/workspace/Python_Workspace/Python_Practice/13_Module

