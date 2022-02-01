print('Hello!')

from ib_insync import *
util.startLoop()  

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=17)

sub = ScannerSubscription(
    instrument='STK', 
    locationCode='STK.NYSE', 
    scanCode='LOW_PE_RATIO')

tagValues = [
#    TagValue("changePercAbove", "1"),
    TagValue('priceAbove', 15),
    TagValue('priceBelow', 50),
    TagValue('minPeRatio',2),
    TagValue('maxPeRatio',20)]

# the tagValues are given as 3rd argument; the 2nd argument must always be an empty list
# (IB has not documented the 2nd argument and it's not clear what it does)
scanData = ib.reqScannerData(sub, [], tagValues)

symbols = [sd.contractDetails.contract.symbol for sd in scanData]
print(symbols)




