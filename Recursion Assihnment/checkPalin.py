## Read input as specified in the question.
## Print output as specified in the question.
def isPalindrome(str):
    if len(str)<=1:
        return 'true'
    if str[0]==str[-1]:
        return isPalindrome(str[1:-1])
    else:
        return 'false'



str = input()
print(isPalindrome(str))