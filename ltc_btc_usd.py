#ltc_btc_usd conversion tool v1.0
#github.com/rawlbot/ltc_btc_usd
#This tool pulls from BTC-E's Public API
#and is designed to provide data relevant to BTC-E 

import json
import urllib2
import time

def main():
	
	#current standard fee on BTC-e 	
	fee = float(0.002)
	
	#Request for LTC being sold
	balance = float(input('How many LTC do you want to sell? '))
	
	#date stamp
	print "As of: " + time.strftime("%c")
		
	ltc_btc(balance, fee)
	ltc_usd(balance, fee)


#convert LTC to USD Includes Fee	
def ltc_usd(balance, fee):
	
	last_trade = urllib2.urlopen('https://btc-e.com/api/2/ltc_usd/ticker')
        decoded = json.loads(last_trade.read())
        conversion = (decoded["ticker"]["sell"]) * balance
	expense = conversion * fee
	net_profit = conversion - expense
	print "Currently " + str(balance) + " LTC are worth $" + str(net_profit) + " after fees!"

#convert LTC to BTC then BTC to USD. Includes Fee
def ltc_btc(balance, fee):
	
	last_trade = urllib2.urlopen('https://btc-e.com/api/2/ltc_btc/ticker')
	decoded = json.loads(last_trade.read())
        conversion = (decoded["ticker"]["sell"]) * balance
	expense = conversion * fee
        net_btc = conversion - expense
        print "Your " + str(balance) + " LTC are worth " + str(net_btc) + " BTC after fees!"

	last_trade = urllib2.urlopen('https://btc-e.com/api/2/btc_usd/ticker')
        decoded = json.loads(last_trade.read())
	btc_usd = (decoded["ticker"]["sell"]) * net_btc
	expense = btc_usd * fee
        net_profit = btc_usd - expense
	print "Currently " + str(net_btc) + " BTC are worth $" + str(net_profit) + " after fees!"

main()

