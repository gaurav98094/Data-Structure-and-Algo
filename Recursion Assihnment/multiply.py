from sys import setrecursionlimit
setrecursionlimit(10**6) 

#User Defined Functions
def get_sign(n1,n2):
    if n1>0 and n2>0:
        return 'p'
    elif n1<0 and n2<0:
        return 'p'
    else:
        return 'm'
    


def multiply_two_number(n1,n2):
    if n2==0:
        return 0
    else:
        return n1 + multiply_two_number(n1,n2-1)
        



#Number 1
num1 = int(input())

#Nmber 2
num2 = int(input())

#Function call
sig = get_sign(num1,num2)
ans  = multiply_two_number(abs(num1),abs(num2))

if sig=='m':
    ans *=-1
#printing output
print(ans)