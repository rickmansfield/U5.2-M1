"""
Given a string, implement a function that returns the string with all lowercase
characters.
Example 1:
Input: "LambdaSchool"
Output: "lambdaschool"
Example 2:
Input: "austen"
Output: "austen"
Example 3:
Input: "LLAMA"
Output: "llama"
*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
"""
Understand
s = "AaaAbBBbG&235423jioj345634rgerRGRGRERG445$%^&£$%^£"
ord_s = []
for c in s:
  ord_s.append(ord(c))

print(ord_s)

for i in range(len(ord_s)):
  if ord_s[i] > 64 and ord_s[i] < 91:
    ord_s[i] += 32
    print(chr(ord_s[i]))

ss = ""

for n in ord_s:
  ss += chr(n)

print(ss)
Plan
- create a list to hold ordinal values

- iterate over all chars in the string and    append the ord value to the list
- iterate over the ordinal list if the value is between 64 and 91 then increment the value by 32

- create an empty string
- iterate over the ordinal values concat each chr of the value to the string 

- return the string
"""


def to_lower_case(string):
    # Your code here
    ord_s = []
    ss = ""
    for c in string:
        ord_s.append(ord(c))

    for i in range(len(ord_s)):
        if ord_s[i] > 64 and ord_s[i] < 91:
            ord_s[i] += 32
        ss += chr(ord_s[i])

    return ss


print(to_lower_case("LambdaSchool"))
print(to_lower_case("austin"))
print(to_lower_case("LLAMA"))
print(to_lower_case("AaaAbBBbG&235423jioj345634rgerRGRGRERG445$%^&£$%^£"))
