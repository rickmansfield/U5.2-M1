"""
initiate empty list set to a variable binary_letters or bl for short
initiate empty string set to a variabe called letters or l for short
write conditionals
    if binary == "" then return that empty string no need to go further
write for loop for each index in the range of (start 0 : length binary: 8 )
    append bl with the binary at that index +8
write another for loop for each string in bl
    convert string to int to char and set to a variable called binary integer or bi 
    then l += bi
Return letters or l
"""
def csBinaryToASCII(binary):
    bl = []
    l = ""
    if binary == "":
        return ""
    for i in range(0, len(binary), 8):
        bl.append(binary[i:i+8])
        print("binary_letters", bl)
    for str in bl: 
        b_int = chr(int(str, 2))
        print("b_int", b_int)
        l += b_int
    return l
    
print(csBinaryToASCII("011011000110000101101101011000100110010001100001")) # lambda
print(csBinaryToASCII("01101100"))
print(csBinaryToASCII("01100001"))
print(csBinaryToASCII("01101101"))
print(csBinaryToASCII("01100010"))
print(csBinaryToASCII("01100100"))
print(csBinaryToASCII("01100001"))
print(csBinaryToASCII(""))
    
    
    
    
    