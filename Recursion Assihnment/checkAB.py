'''
Suppose you have a string, S, made up of only 'a's and 'b's. 
Write a recursive function that checks if the string was generated using the following rules:
a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.


Input format :
String S
Output format :
'true' or 'false'
Constraints :
1 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
abb
Sample Output 1 :
true
Sample Input 2 :
abababa
Sample Output 2 :
false

'''





def check_ab(str):
    if len(str)==0:
        return 'true'
    
    if str[0]=='a':
        return check_ab(str[1:])
    elif str[0]=='b':
        if str[1]=='b':
            return check_ab(str[2:])
        else:
            return 'false'
    else:
        return'false'
        


#Input
str = input()

# Function Call
if str[0]!='a':
    ans='false'
else:
    ans = check_ab(str)

# Print output
print(ans)