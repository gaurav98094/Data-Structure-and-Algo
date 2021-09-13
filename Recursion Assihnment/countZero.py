def number_of_zero(n):
    if n==0:
        return 1
    if n<10:
        return 0
    
    if n%10==0:
        return 1 + number_of_zero(n//10)
    else:
        return number_of_zero(n//10)


#Number
num = int(input())

#Function call
ans  = number_of_zero(num)

#printing output
print(ans)