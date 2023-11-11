import math 
x = int(input("Nhập x:"))
ex=1
n=1
t=x
while math.fabs(t)>=0.0001:
    ex += t
    n += 1
    t *=(x/n)
print("Gía trị gần đúng của e mũ X là:",ex