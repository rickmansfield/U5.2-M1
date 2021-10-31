# Unit 5.2 M1 Homework Task 6
"""
- Research these bitwise operators tilde, and, all, shift right, sift left, xor ^
- research int() and bin()
- https://www.youtube.com/watch?v=0zWiugtOMd4
- https://www.youtube.com/watch?v=w3SzPfs0CHM
- Complement Formula ~X = -X-1
- bitwise left shift value << No. shifted or x << n
- bitwise left shift value << No. shifted or x << n
- initiate empty integer
- while loop for n >0
- left shift reversed_num by 1
- write conditional for 
- 
"""
# print(bin(12)) # 0b1100
# print(int(0b1100)) #12
# print("x ^ 1 = ", 9 ^ 1 )

def csReverseIntegerBits(n):
    reversed_num = 0
    while (n > 0):
        reversed_num = reversed_num << 1 # value << No. shifted or x << n
        print("Left Shift 1:", reversed_num)
        if (n & 1 == 1):
            print("n post shift", n)
            reversed_num = reversed_num ^ 1
            print(" reversed_num ^ 1:", reversed_num)
        n = n >> 1
    return reversed_num

# print(csReverseIntegerBits(417)) # 267

print(csReverseIntegerBits(267)) # 417

# print(csReverseIntegerBits(0)) # 0