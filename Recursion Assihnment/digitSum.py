## Read input as specified in the question.
## Print output as specified in the question.
def find_sum(num):
    if num==0:
        return 0
    else:
        return num%10 + find_sum(num//10)


num = int(input())
print(find_sum(num))