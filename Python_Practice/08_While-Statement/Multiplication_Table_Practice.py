# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 11.
@attention: While을 배웠으면 구구단을 해야지!!
@author: Sangyun
'''

def Multiplication_View(Number) : 
    Multiple_Number = 1
    
    while Multiple_Number < 10 :
        
        print ("%s X %s = %d" % (Number, Multiple_Number, int(Number) * Multiple_Number))       # int (Value)로 문자열을 정수형으로 
        
        Multiple_Number += 1        # 참고 : 파이썬에는 증감연산자가 없다 
                                    # A++, --A, 이런거 없다 
                                    
                            
if __name__ == '__main__':
    Multiplication_View(input("몇 단 : "))        # input(prompt)는 입력받은 데이터를 모두 문자열로 취급함 
                                                 # prompt 매개변수는 입력받기전에 질문 등을 출력할 때 쓰인다 
                                                 # prompt로 출력된 정보는 개행이 되지 않는다 
                                                 # 따로 print 해줄 필요가 없다!!!
    

# 출력 Example
# 몇 단 : 9
# 9 X 1 = 9
# 9 X 2 = 18
# 9 X 3 = 27
# 9 X 4 = 36
# 9 X 5 = 45
# 9 X 6 = 54
# 9 X 7 = 63
# 9 X 8 = 72
# 9 X 9 = 81