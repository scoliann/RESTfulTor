# Summary 
restfulTor.py is a python module that allows the user to change IP addresses and make RESTful calls to be made through the Tor network.

## Inspiration
While doing a final project for CS229 Machine Learning at Stanford, my team was dealing with a large dataset.  For each line in the dataset, we needed to call the sentiment analysis API at "http://text-processing.com/api/sentiment/".  Due to the number of API calls being made, my computer kept on being rate limited and blocked.  Therefore, I conceived the idea of sending all traffic to the API through Tor.  This would allow us to ping the API until one IP is blocked, then simply switch IP addresses.  The system worked perfectly, and we were able to send as much traffic as needed to the API!

## How to Use
The main function of restfulTor.py contains examples of how to do the following:
- Open Tor browser programmatically
- Make GET, POST, PUT, and DELETE requests
- How to change IP addresses
The main function can be run using python restfulTor.py.

## Prerequisites
It is necessary for the Tor browser to be open and running before any RESTful requests or IP address changes can be made.  For this reason, I have included an installation of Tor in the folder labeled "Tor".

## Shoutouts
A special thanks to the following:
- 1) The Tor Project (https://www.torproject.org/)
- 2) HttpBin, which was extremely useful for testing (https://httpbin.org/)
- 3) The brave few who attempted to achieve the same functionality.  It was only by reading through numerous other attempts that I was eventually able to figure out how to use Tor programmatically.
