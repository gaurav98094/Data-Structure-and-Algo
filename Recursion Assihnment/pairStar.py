'''
Given a string S, compute recursively a new string where identical chars that are adjacent in the original string 
are separated from each other by a "*".


Input format :
String S
Output format :
Modified string
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
hello
Sample Output 1:
hel*lo
Sample Input 2 :
aaaa
Sample Output 2 :
a*a*a*a

'''

def pair_star(str,x):
    if x>len(str)-2:
        return str
    else:
        if str[x+1]==str[x]:
            return pair_star(str[:x+1]+"*"+str[x+1:],x+1)
        else:
            return pair_star(str,x+1)


#String
str = input()

#Function call
ans  = pair_star(str,0)

#printing output
print(ans)