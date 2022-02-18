# byteaddresshelper
A simple program to determine the byte address of a page depending on different customizable variables.

# How to use

The program will prompt you with a series of questions about the nature of the byte address you're trying to calculate, simply input the variables as it prompts you and it will output the correct byte address.

# Sample output

Here is a sample output using random values.

 ```
 ========================================
Direct map or set associative (d/s): s
Byte address or word address (b/w): b
Please enter byte address: 100101010101
Please enter block size: 8
Please enter amount of blocks in cache: 4
Please enter set size (2 blocks, 4 blocks, etc.): 2
Word Address: 1001010101
Block Address: 1001010
Tag | Set: 100101 | 0
========================================
Direct map or set associative (d/s): d
Byte address or word address (b/w): w
Please enter word address: 101010100101
Please enter block size: 4
Please enter amount of blocks in cache: 4
Word Address: 101010100101
Block Address: 1010101001
Tag | Index: 10101010 | 01
========================================
```
