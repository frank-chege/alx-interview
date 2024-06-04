#!/usr/bin/python3
'''checks if a dataset is valid utf-8 encoded'''
from typing import List

def validUTF8(data: List[int])->bool:
    '''checks if a dataset is valid UTF-8'''
    mask1 = 1
    mask2 = 1 << 1
    mask3 = 1 << 2
    mask4 = 1 << 3
    #get each byte
    idx = 0
    while idx < len(data):
        byte = data[idx]
        #get the value of the bits using a bit mask
        bit1 = byte & mask1
        bit2 = byte & mask2
        bit3 = byte & mask3
        bit4 = byte & mask4
        #1-byte char
        if bit1 == 0:
            idx += 1
            continue
        if bit2 == 0:
            return False
        #2-byte char
        elif bit3 == 0:
            #check the 2nd byte
            try:
                byte = data[idx+1]
            except:
                return False
            byte2_bit1 = byte & mask1
            byte2_bit2 = byte & mask2
            if byte2_bit1 == 1 and byte2_bit2 == 0:
                idx += 2
                continue
            else:
                return False
        #3-byte char
        elif bit3 == 1 and bit4 == 0:
            #check 2nd byte
            try:
                byte = data[idx+1]
            except:
                return False
            byte2_bit1 = byte & mask1
            byte2_bit2 = byte & mask2
            if byte2_bit1 == 1 and byte2_bit2 == 0:
                #check 3rd byte
                try:
                    byte = data[idx+2]
                except:
                    return False
                byte3_bit1 = byte & mask1
                byte3_bit2 = byte & mask2
                if byte3_bit1 == 1 and byte3_bit2 == 0:
                    idx += 2
                    continue
                else:
                    return False
            else:
                return False
        #4-byte char
        elif bit1 == 1 and bit2 == 1 and bit3 == 1 and bit4 == 0:
            #check 2nd byte
            try:
                byte = data[idx+1]
            except:
                return False
            byte2_bit1 = byte & mask1
            byte2_bit2 = byte & mask2
            if byte2_bit1 == 1 and byte2_bit2 == 0:
                #check 3rd byte
                try:
                    byte = data[idx+2]
                except:
                    return False
                byte3_bit1 = byte & mask1
                byte3_bit2 = byte & mask2
                if byte3_bit1 == 1 and byte3_bit2 == 0:
                    #check 4th byte
                    byte = data[idx+3]
                    byte4_bit1 = byte & mask1
                    byte4_bit2 = byte & mask2
                    if byte4_bit1 == 1 and byte4_bit2 == 0:
                        idx += 3
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                return False

