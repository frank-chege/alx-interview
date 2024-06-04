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
    try:
        byte_list = data
    except:
        return False
    mask1 = 1 << 7
    mask2 = 1 << 6
    mask3 = 1 << 5
    mask4 = 1 << 4
    #get each byte
    for idx in range(0, len(byte_list)):
        byte = byte_list[idx]
        #get the value of the bits using a bit mask
        bit1 = byte & mask1
        bit2 = byte & mask2
        bit3 = byte & mask3
        bit4 = byte & mask4
        #1-byte char
        if bit1 == 0:
            return True
        #2-byte char
        elif bit1 == 1 and bit2 == 1 and bit3 == 0:
            #check the 2nd byte
            byte = byte_list[idx+1]
            byte2_bit1 = byte & mask1
            byte2_bit2 = byte & mask2
            if byte2_bit1 == 1 and byte2_bit2 == 0:
                return True
            else:
                return False
        #3-byte char
        elif bit1 == 1 and bit2 == 1 and bit3 == 1 and bit4 == 0:
            #check 2nd byte
            byte2_bit1 = byte & mask1
            byte2_bit2 = byte & mask2
            if byte2_bit1 == 1 and byte2_bit2 == 0:
                #check 3rd byte
                byte = byte_list[idx+2]
                byte3_bit1 = byte & mask1
                byte3_bit2 = byte & mask2
                if byte3_bit1 == 1 and byte3_bit2 == 0:
                    return True
                else:
                    return False
            else:
                return False
        #4-byte char
        elif bit1 == 1 and bit2 == 1 and bit3 == 1 and bit4 == 0:
            #check 2nd byte
            byte2_bit1 = byte & mask1
            byte2_bit2 = byte & mask2
            if byte2_bit1 == 1 and byte2_bit2 == 0:
                #check 3rd byte
                byte = byte_list[idx+2]
                byte3_bit1 = byte & mask1
                byte3_bit2 = byte & mask2
                if byte3_bit1 == 1 and byte3_bit2 == 0:
                    #check 4th byte
                    byte = byte_list[idx+3]
                    byte4_bit1 = byte & mask1
                    byte4_bit2 = byte & mask2
                    if byte4_bit1 == 1 and byte4_bit2 == 0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

