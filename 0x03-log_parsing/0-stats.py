'''
read from stdin and compute some metrics
'''
#!/usr/bin/python3
import sys
import ipaddress
from dateutil.parser import parse
import signal
import re

#global dict containing the codes
status_codes = {
    'File size': 0,
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
#compiled pattern
pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*)\] "GET /projects/260 HTTP/1\.1" (\d{3,4}) (\d+)$'
compiled_pat = re.compile(pattern)

def handler(signum, frame):
    '''handles the keyboard interrupt signal'''
    printer() #call printer function

def printer():
    '''print the dictionary'''
    for key, value in status_codes.items():
        if value == 0:
            continue
        else:
            print(f'{key}: {value}')

def format_checker(line)->bool:
    '''receives line read from stdin and check whether it matches the specified format'''
    global status_codes
    global compiled_pat
    match = compiled_pat.match(line)
    if match:
        code = int(match.group(3))
        size = int(match.group(4))
        #update the status codes
        status_codes['File size'] += size
        status_codes[code] += 1
        return True
    else:
        return False

def main():
    '''read from stdin'''
    #setup the signal
    signal.signal(signal.SIGINT, handler)
    count = 0
    try:
        for line in sys.stdin:
            #check if the line format matches the specified one
            if format_checker(line.strip()):
                pass
                count += 1
                #check if count is
            if count == 10:
                printer() #call printing function
                count = 0
    finally:
        #print any remaining lines
        if count < 10:
            printer()

if __name__ == '__main__':
    main()