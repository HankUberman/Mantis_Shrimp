#   This File allows us to search through ScanCodes that are available in IBKR, run in terminal to be directed to a web browser for the full directory, the terminal will show all filtering tags. 
# 
# Scan Codes are the top level of the search & ranking system, try to to keep the search broad. 



keyword = 'LOW'
from ib_insync import *
util.startLoop()  

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=17)



xml = ib.reqScannerParameters()

print(len(xml), 'bytes')

path = 'scanner_parameters.xml'
with open(path, 'w') as f:
    f.write(xml)

import webbrowser
#webbrowser.open(path)

# parse XML document
import xml.etree.ElementTree as ET
tree = ET.fromstring(xml)

# find all tags that are available for filtering
'''
tags = [elem.text for elem in tree.findall('.//AbstractField/code')]
print(len(tags), 'tags:')

print(tags)
'''
scanCodes = [e.text for e in tree.findall('.//scanCode')]

print(len(scanCodes), 'scan codes, showing the ones starting with', keyword,':')
print([sc for sc in scanCodes if sc.startswith(keyword)])
print('''


''')
print(len(scanCodes), 'scan codes, showing all values')
print([sc for sc in scanCodes]) #if sc.startswith(keyword)])
