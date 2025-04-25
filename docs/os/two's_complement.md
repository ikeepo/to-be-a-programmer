# Two's Complement
> [wiki](https://en.wikipedia.org/wiki/Two%27s_complement)
method of representing signed integers.
Greates value as sign (Most Significan Bit)

It ensures the addition and subtraction works same, 在计算机内存角度不用考虑负号；
range $-2^{n-1} - 2{n-1} - 1$.
# Steps: Encode
1. start from positive version
3 => `0011`
2. flip all bits
`1100`
3. add 1
`1101`  = -3
# Steps: Decode
1. check sign
`1` means negative
2. Flip the bit
`0010`
3. add `1`
`0011` means 3
# Ones's Complement
> [Wiki](https://en.wikipedia.org/wiki/Ones%27_complement)

# Formula
$-k = 2^n - k$
公式的核心是Mod运算，-k+k=0是mod(2^n)下的0，也就是2^n;
-8是特殊的，16-8=8，所以8跟-8的位表示一样；

$-k = 2^{n+1} - k$两个公式等价；
## 4bits数
usign => [0,15];
sign => [-8, 7];
其中0-7跟unsigned二进制一致，-1~-8用15-8表示；
负数的表示是通过保证与整数相加得到0来获取的；
## 为什么刚好能对应

# Why Decimal value is called magnitude
