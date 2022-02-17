from functionCollection import *

name = ["Kamal", "Putun", "Rishi", "Bumba", "Ayush"]
nameAddress = {"Bhagalpur": "Kamal", "Pune": "Rishi", "Kolkota": "Bumba"}
fun_argsKwargs(*name, **nameAddress)

print("******** Word Reverse ********")
# Input "geeks quiz practice code"
# Output "code practice quiz geeks"
str1 = "geeks quiz practice code"
#word_reverse(str1)

print("******** Remove th from the begining of the word ********")
# Input "this is thoughtworksth"
# Output "htis is htoughtworksth"
string1 = "this is thoughtworksth"
string2 = "th"
string3 = ""
for k in range(0, len(string2)):
    k1 = k+1
    string3 = string3 + string2[len(string2)-k1]
print(string3)
string2 = string1.split(" ")
print(string2)
#for i in range(0, len(string2)):
#    if string2[i].startswith(string3):





# Driver code
s = "mAlayalaM"
st = s.lower()
ans = isPalindromeForLoop(st)

j = -1
flag = 0
for i in st:
    if i != st[j]:
        flag = 1
    j = j - 1
if flag == 1:
    print("Not a Palindrome")
else:
    print("Palindrome")
if ans:
    print("Yes")
else:
    print("No")
