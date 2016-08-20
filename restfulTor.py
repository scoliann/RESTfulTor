from stem.control import Controller
from stem import Signal
import pycurl
import urllib
import cStringIO
import time
from requests import get
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver 


# Set Variables
SOCKS_PORT = 9150
CONTROL_PORT = 9151


# Parent Class
class torBaseFunct:

	# Constructor
	def __init__(self):
		return

	# Open Tor Browser
	def openTor(self):
		binary = FirefoxBinary('Tor/Tor Browser/Browser/firefox.exe')
		profiler = webdriver.FirefoxProfile('Tor/Tor Browser/Browser/TorBrowser/Data/Browser/profile.default')
		browser = webdriver.Firefox(firefox_binary=binary, firefox_profile=profiler)
		browser.implicitly_wait(60)

	# Change Your Tor IP
	def changeIP(self):

		# Create controller
		with Controller.from_port(port = CONTROL_PORT) as controller:

			# Authenticate
			controller.authenticate()
	
			# Generate new IP
			controller.signal(Signal.NEWNYM)

			# Wait for new Tor path to connect
			time.sleep(controller.get_newnym_wait())


# Child Class
class torRest(torBaseFunct):

	# Constructor
	def __init__(self):
		return

	# Tor RESTful API Request
	def request(self, callType, url, parameters={}):

		# Encode parameters - eg. {'text': 'fuck your api'}
		encodedData = urllib.urlencode(parameters)

		# Create curl and set parameters
		query = pycurl.Curl()
		query.setopt(query.URL, url)
		query.setopt(query.POSTFIELDS, encodedData)
		query.setopt(query.CUSTOMREQUEST, callType)

		# Tor Proxy Settings
	  	query.setopt(pycurl.PROXY, 'localhost')
	  	query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
	  	query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)

		# Set stream to collect response from url
		output = cStringIO.StringIO()
	  	query.setopt(pycurl.WRITEFUNCTION, output.write)
	
		try:
			# Perform the POST request and close
			query.perform()
			query.close()
			return output.getvalue()
		except pycurl.error as exc:
	    		return "Unable to reach %s (%s)" % (url, exc)


if __name__ == '__main__':

	# Create new torRest class
	tor = torRest()

	# Start Tor web browser
	print 'Wait a few moments as Tor web browser opens...\n'
	tor.openTor()

	# Demonstrate sending a GET request through Tor
	getResult = tor.request('GET', 'https://httpbin.org/get')
	print 'Demonstrating GET request through Tor:'
	print '\tResult of GET request: \n' + getResult + '\n'

	# Demonstrate sending a POST request through Tor
	postResult = tor.request('POST', 'https://httpbin.org/post', {'postKey' : 'some POST value'})
	print 'Demonstrating POST request through Tor:'
	print '\tResult of POST request: \n' + postResult + '\n'

	# Demonstrate sending a PUT request throught Tor
	putResult = tor.request('PUT', 'https://httpbin.org/put', {'putKey' : 'some PUT value'})
	print 'Demonstrating PUT request through Tor:'
	print '\tResult of PUT request: \n' + putResult + '\n'

	# Demonstrate sending a DELETE request throught Tor
	deleteResult = tor.request('DELETE', 'https://httpbin.org/delete', {'deleteKey' : 'some DELETE value'})
	print 'Demonstrating DELETE request through Tor:'
	print '\tResult of DELETE request: \n' + deleteResult + '\n'

	# Demonstrate changing IP address
	firstTorIP = tor.request('GET', 'https://httpbin.org/ip')
	nonTorIp = get('https://httpbin.org/ip').text
	tor.changeIP()
	secondTorIP = tor.request('GET', 'https://httpbin.org/ip')
	print 'Demonstrating changing Tor IP address:'
	print '\tCurrent Tor IP: \n' + firstTorIP + '\n'
	print '\tCurrent Non-Tor IP: \n' + nonTorIp + '\n'
	print '\tNew Tor IP: \n' + secondTorIP + '\n'








			





