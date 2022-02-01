#   This File allows us to search through Scanner Parameters that are available in IBKR, run in terminal to be directed to a web browser for the full directory, the terminal will show all filtering tags. 
# 
# 
from ib_insync import *
util.startLoop()  


ib = IB()
ib.connect('127.0.0.1', 7497, clientId=17)
'''
sub = ScannerSubscription(
    instrument='STK', 
    locationCode='STK.US.MAJOR', 
    scanCode='TOP_PERC_GAIN')

scanData = ib.reqScannerData(sub)

print(f'{len(scanData)} results, first one:')
print(scanData[0])
'''
xml = ib.reqScannerParameters()

print(len(xml), 'bytes')

path = 'scanner_parameters.xml'
with open(path, 'w') as f:
    f.write(xml)

import webbrowser
webbrowser.open(path)

# parse XML document
import xml.etree.ElementTree as ET
tree = ET.fromstring(xml)

# find all tags that are available for filtering
tags = [elem.text for elem in tree.findall('.//AbstractField/code')]
print(len(tags), 'tags:')
print(tags)