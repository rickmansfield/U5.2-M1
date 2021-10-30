"""
Decimal to Binary
-----------------
25
63
9
111
  
On paper this evaluates quickly 11001
25 // 2 -> 12 R 1
12 // 2 -> 6  R 0
6 // 2  -> 3  R 0
3 // 2  -> 1  R 1
1 // 2  -> 0  R 1

BUT...The computer will need both equations
25 // 2 = 12
    25 % 2 = 1
12 // 2 = 6
    12 % 2 = 0
6 // 2 = 3
    6 % 2 = 0
3 // 2 = 1
    3 % 2 = 1
1//2 = 0
    1 % 2 = 1
to be able to arrive at >> 11001

BIN 1000001 = 'A'
HEX 41 = 'A'
DEC 65 = 'A'
"""

print(0b11001) # 25
print(bin(25)) # 0b11001
print(0b1000001) #65
print(hex(65)) # 0x41
print(bin(41)) # 0b101001
print(int("0x41", 16)) # 65 >>> converts from base 16 to base 10
