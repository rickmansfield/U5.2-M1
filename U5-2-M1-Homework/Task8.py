"""
initiate empty string to capture result_Sound or rs for sort
conditionals
    if number % 3, 5, 7 return rs += appropriate sound "Pling, Plang, Plong"
    if no factor of 3, 5, 7, the result should still be an empty string so return rs += number converted to string
return rs
"""

def csRaindrops(number):
    rs = ""
    if number %3 == 0:
        rs += "Pling"
    if number %5 == 0:
        rs += "Plang"
    if number %7 == 0:
        rs += "Plong"
    elif rs == "":
        rs += str(number)
    return rs

print(csRaindrops(28))
print(csRaindrops(30))
print(csRaindrops(34))