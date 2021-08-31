from random import *

n=int(input("로또 길이 :"))
arr=list(map(int,input("복권을 뽑아주세요 :").split()))
cnt=0
if  n!=len(arr):
    print("잘못된 복권입니다")
else:
    for i in range(n):
        point=int(random()*10)+1
        print(point,end=' ')
