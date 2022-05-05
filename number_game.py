#終極密碼

#模組
import random
from math import *

#密碼
password=(floor(random.uniform(0,100)))
#最大值
num_max=100
#最小值
num_min=0
#猜測數字
guess_num=None

#遊戲過程
while guess_num != password : 
    guess_num=int(input("請輸入一個數字: "))
    #猜測數字 > 密碼
    if guess_num > password and guess_num < num_max :
        num_max=guess_num
        print ("\n"+str(num_min)+"~"+str(num_max))
    #猜測數字 < 密碼
    elif guess_num < password and guess_num > num_min :
        num_min=guess_num
        print ("\n"+str(num_min)+"~"+str(num_max))
    #猜中
    elif guess_num==password:
        print("\n"+"bomb!!")
    #猜測數字範圍外
    else :
        print("\n"+"please guess a number between"+str(num_min)+("~ ")+str(num_max))
