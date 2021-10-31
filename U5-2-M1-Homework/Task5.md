# Unit 5.2 M1 Homework Task 5

Q) In order to store strings in memory, each character in the string mut be encoded so that tit can be stored as binary . ASCII is one example of a character set. Each character in ASCII can be represented by 7 bits (although they are commonly stored as 8 bits). Given that, what is the maximum number of characters that could be in the ASCII set. 

- 64
- 72
- 128
- 140 

My guess 128
But I'm still investigating this.

The ASCII table has 128 characters, with values from 0 through 127. Thus, 7 bits are sufficient to represent a character in ASCII; however, most computers typically reserve 1 byte, (8 bits), for an ASCII character. One byte allows a numeric range from 0 through 255 which leaves room for growth in the size of the character set, or for a sign bit.