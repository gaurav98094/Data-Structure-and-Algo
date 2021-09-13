# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(str):
    # Please add your code here
    if len(str)==1:
        return str
    
    if str[0]==str[1]:
        return removeConsecutiveDuplicates(str[1:])
    else:
        return str[0] + removeConsecutiveDuplicates(str[1:])

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
