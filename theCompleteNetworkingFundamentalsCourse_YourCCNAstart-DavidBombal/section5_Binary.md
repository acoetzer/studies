###### - Binary

<br>

<!-- Table Of Contents -->

### Table Of Contents

- [Binary Introduction](#binary-introduction)
    - [What Is A Binary Number](#what-is-a-binary-number)
- [Binary Math](#binary-math)
- [Binary Conversion Example](#binary-conversion-example)
    - [IPv4 Octet Table](#ipv4-octet-table)
    - [What Is The Binary Eqivalent To 192](#what-is-the-binary-eqivalent-to-192)
    - [What Is The Binary Eqivalent To 253](#what-is-the-binary-eqivalent-to-253)
    - [What Is The Deciaml Eqivalent To 1100 0000](#what-is-the-deciaml-eqivalent-to-1-1-0-0-0-0-0-0)
    - [What Is The Deciaml Eqivalent To 1111 1101](#what-is-the-deciaml-eqivalent-to-1-1-1-1-1-1-0-1)
- [Converting IP Addresses To Binary](#converting-ip-addresses-to-binary)
    - [Why Should We Know Binary](#why-should-we-know-binary)
    - [Lets Workout Our IPv4 Address In Binary](#lets-workout-our-ipv4-address-in-binary)

<br>
<br>

# Binary Introduction 
* Binary is a building block in networks today. Its used in multiple places such as:
    * Access Lists or Access Control Lists
        * which allow you to permit or deny various devices on your network.
        * You do this by matching specific ip addresses by their binary number.
    * Supnetting, or supnet mask.

## What Is A Binary Number
* We learn that a Binary Number is part of the base 2 numeral system or binary numeral system, which is essentially a method of mathematical expression which uses only two symbols 1 or 0 where we use the base 10 number system. 
    * This in computer electronics equates to devices having 2 states, on or off, though in binary on is 1 and off is 0.
* Each Bit has 2 States and that bit is then used as an exponent against the 2 states giving us the result of a decimal number which equates to the amount of combinations that that bit has.

# Binary Math

<br>

![binaryMath1Bit](./src/binaryMath1Bit.png "2 States and 1 Bit")

* 2 x 1 <sup>2<sup>1</sup></sup> = Decimal Number 2 and amount of Combinations which is either 1 or 0

<br>

![binaryMath2Bits](./src/binaryMath2Bits.png "2 State and 2 Bits")

* 2 x 2 <sup>2<sup>2</sup></sup> = Decimal Number 4 and amount of Combinations

<br>

![binaryMath3Bits](./src/binaryMath3Bits.png "2 States and 3 Bits")

* 2 x 3 <sup>2<sup>3</sup></sup> = Decimal Number 8 and amount of Combinations

<br>

![binaryMath4Bits](./src/binaryMath4Bits.png "2 States and 4 Bits")

* 2 x 4 <sup>2<sup>4</sup></sup> = Decimal Number 16 and amount of Combinations

<br>

* 2 to the power of 0 <sup>2<sup>0</sup></sup> = 1
* 2 to the power of 1 <sup>2<sup>1</sup></sup>
    * which is 2 multiplied together 1 time <sup>2x1</sup> = 2 Bits
* 2 to the power of 2 <sup>2<sup>2</sup></sup>
    * which is 2 multiplied together 2 times <sup>2x2</sup> = 4 Bits
* 2 to the power of 3 **<sup>2<sup>3</sup></sup>**
    * which is 2 multiplied together 3 times <sup>2x2x2</sup> = 8 Bits
* 2 to the power of 4 <sup>2<sup>4</sup></sup>
    * which is 2 multiplied together 4 time <sup>2x2x2x2</sup> = 16 Bits
* 2 to the power of 5 <sup>2<sup>5</sup></sup>
    * which is 2 multiplied together 5 time <sup>2x2x2x2x2</sup> = 32 Bits
* 2 to the power of 6 <sup>2<sup>6</sup></sup>
    * which is 2 multiplied together 6 time <sup>2x2x2x2x2x2</sup> = 64 Bits
* 2 to the power of 7 <sup>2<sup>7</sup></sup>
    * which is 2 multiplied together 7 time <sup>2x2x2x2x2x2x2</sup> = 128 Bits
* 2 to the power of 8 <sup>2<sup>8</sup></sup>
    * which is 2 multiplied together 8 time <sup>2x2x2x2x2x2x2x2</sup> = 256 Bits

# Binary Conversion Example
## IPv4 Octet Table

<br>

![ipv4BinaryOctetTable](./src/ipv4BinaryOctetTable.png "Showcasing the Octet Table")

<br>

## What Is The Binary Eqivalent To 192
![binaryEqivalentOfDecimalPart1](./src/binaryEqivalentOfDecimalPart1.png "The Binary Eqivalent Of The Decimal 192")

<br>

## What Is The Binary Eqivalent To 253
![binaryEqivalentOfDecimalPart2](./src/binaryEqivalentOfDecimalPart2.png "The Binary Eqivalent Of The Decimal 253 and Showing How To Work Backwards")

<br>

## What Is The Deciaml Eqivalent To 1100 0000
![decimalEqivalentOfBinaryPart1](./src/decimalEqivalentOfBinaryPart1.png "The Decimal Eqivalent Of The Binary 1100 0000")

<br>

## What Is The Deciaml Eqivalent To 1111 1101
![decimalEqivalentOfBinaryPart2](./src/decimalEqivalentOfBinaryPart2.png "The Decimal Eqivalent Of The Binary 1111 1101 and Shwoing How to Work backwards")

<br>

# Converting IP Addresses To Binary
* When looking at your phone as an example you will see the the configure IP was done automatically, this is typically with networks and is known as DHCP or Dynamic Host Configuration Protocol.
    * In other words a server allocates a IP to your device.
* With IPv4 It uses what is known as a dotted decimal address.
    * as an example our IP address is 192.168.100.8
    * This is considered 4 Octets, meaning 192 is 1 Binary Octet and we know that 192 is 1100 0000 which is an octet.
* So an IPv4 Address has 4 Octets therefor making it 32 Bits long. 
    * 8 Bits + 8 Bits + 8 Bits + 8 Bits = 32 Bits

## Why Should We Know Binary
* Why Should we know Binary when it comes to IP Addresses and that is becuase when working with Access Lists or cases where you need to permit or deny traffic you going to need to think in Binary.
    * Devices such as routers or firewalls use binary to determine what is allowed or denied.

## Lets Workout Our IPv4 Address In Binary
## 192.168.100.8 or 11000000 10101000 01100100 00001000 

<br>

![ourIPInBinary](./src/ourIPInBinary.png "Our IP worked Out In Binary")
