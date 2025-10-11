# Dart 
# int: memory
arbitrary-precision integer, which means it's limited only by the memory.
Arbitrary precision vs fixed width which has overflow problem .

A machine word is the natural unit of data a processor can handle in one operation. On a 32-bit CPU, a word = 32bits = 4 bytes.

Small integer (that fit in a machine word) are stored using **tagged pointers**.

