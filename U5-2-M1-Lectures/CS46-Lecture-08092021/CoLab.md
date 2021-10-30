# Unit 5.2 M1 Number Bases & Characters

- [Unit 5.2 M1 Number Bases & Characters](#unit-52-m1-number-bases--characters)
  - [Topics Covered today](#topics-covered-today)
  - [Decimal](#decimal)
    - [Decimal / Radix 10](#decimal--radix-10)
  - [Binary](#binary)
    - [Binary/Radix 2](#binaryradix-2)
  - [Conversion between Decimal and Binary](#conversion-between-decimal-and-binary)
  - [Hexadecimal](#hexadecimal)
    - [Hexadecimal / Radix 16](#hexadecimal--radix-16)
  - [Conversion Between Binary and Hexadecimal](#conversion-between-binary-and-hexadecimal)
  - [Arrays](#arrays)
  - [Strings](#strings)

## Topics Covered today
- Number Bases NOTE - Etymology Radix is a Latin word for "root". Root can be considered a synonym for base, in the arithmetical sense.
- Decimal
- Binary
- Hexadecimal

## Decimal
### Decimal / Radix 10
```
10^n

0 - 9

10^3 10^2 10^1  10^0
TH   H    T     U/O
0    0    0     0
2    1    5     7
```

## Binary
### Binary/Radix 2
```
2^n

0 - 1

2^3 2^2 2^1  2^0
8   4   2    1
0   0   0    0 
1   0   1    0 => 1 * 8 + 0 * 4 + 1 * 2 + 0 * 1 => 10 (Base 10) 
```

## Conversion between Decimal and Binary
```
25
63
9
111
```
## Hexadecimal
### Hexadecimal / Radix 16

```
0-9 A-F
16^n

16^2  16^1 16^0
256s  16s   1s
 0    0    0    
 0    0    1
 0    2    1  =>  2 * 16 + 1 * 1 => 33 DECIMAL
 0    F    F => 15 * 16 + 15 * 1 => 255
 1    0   0 => 1 * 256 + 0 * 16 + 0 * 1 => 256
 ```
## Conversion Between Binary and Hexadecimal
```
8421
10010001
10000001
00111100
10101100

1001        0001
[9]          [1]

1111
F

91 <> 10010001
```

## Arrays
- go to /CS46-Lecture-08092021/Arrays.py

## Strings
-
- ASCII
- UTF8 / 16
