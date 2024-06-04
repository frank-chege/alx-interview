#!/usr/bin/python3
'''checks if a dataset is valid utf-8 encoded'''
from typing import List

#convert the data to bytes
#check against the utf-8 rules using bitwise operators
#1 byte char - 1st bit is 0
# negate the first 4 bits
#if 1st bit is 1 , it's a 1 byte char
#count the no. of bytes ie bits == 8
#if > 8, not valid utf-8
#2 byte char - 1st byte bits are 11.. 2nd byte begins with 10
#if first 2 bits are 0 and , it's a 2 byte char
#count the no of bit ie bits == 16
#3 byte char - 1st byte bits are 111.. 2nd byte begins with 10.. 3rd byte 10..
#if first 3 bits are 0's , it's a 3-byte char
#total bit == 24
#4 byte char - 1st byte bits are 1111.. 2nd byte begins with 10.. 3rd byte 10.. 4th byte 10..
#if first 4 bits are 0's, it's a 4-byte char
#check if total bits == 32

def validUTF8(data: List[int])->bool:
    '''checks if a dataset is valid UTF-8'''
    #convert list into bytes
    byte_list = data.encode('UTF-8')
    mask1 = 1 << 7
    mask2 = 1 << 6
    mask3 = 1 << 5
    mask4 = 1 << 4
    #get each byte
    for byte in byte_list:
        bit1 = byte & mask1
        bit2 = byte & mask2
        bit3 = byte & mask3
        bit4 = byte & mask4
        if bit1 == 0:
            return True
        elif (bit1 == 1 and bit2 == 1) and bit3 == 1 or bit4 == 1:
            return True
        else:
            return False

