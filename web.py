# web demo

import urllib.request as ur
import requests
from bs4 import BeautifulSoup 
import re
import time


# using urllib.request
'''
page = ur.urlopen('https://www.google.com/')
print(type(page))          #<class 'http.client.HTTPResponse'>
print(type(page.read()))  #<class 'bytes'>
print(page.read())        #b'' 
print()
print(page.getheader('Content-Type'))   #text/html; charset=ISO-8859-1
print()
for key,value in page.getheaders() :    
    print(key + ":", value)
print()
'''
'''
Date: Thu, 15 Mar 2018 16:20:53 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2018-03-15-16; expires=Sat, 14-Apr-2018 16:20:53 GMT; path=/; domain=.google.com
Set-Cookie: NID=125=C1Rp0jh-4qvTZhtWYrhohySQTsXdUNeqvtLm3B5YcRITS-CPklQydgzSA68DTLV98RYFRzYQZYrYuoIUgBWp_I2zOGTZShkMNVwODQ-eLzoZvrfKCN80gnR4oNiEDZT5; expires=Fri, 14-Sep-2018 16:20:53 GMT; path=/; domain=.google.com; HttpOnly
Alt-Svc: hq=":443"; ma=2592000; quic=51303431; quic=51303339; quic=51303335,quic=":443"; ma=2592000; v="41,39,35"
Accept-Ranges: none
Vary: Accept-Encoding
Connection: close
'''
#print(page.info()) #same as for loop          

'''
#using requests

page = requests.get('https://python.org/')
print(page.status_code)     #200     
print(type(page))          #<class 'requests.models.Response'>
print(page)     #<Response [200]>
text = page.text                     
print(type(text))      #<class 'str'>
content = page.content
print(type(content))     #<class 'bytes'>
print(page.headers['Content-Type'])    #text/html; charset=utf-8 
print(page.encoding)      #utf-8
'''


# reading large file
'''
There can be a few issues when we have a large web page to download.
It is not possible to store all the content of the web page in a string, and even if it just fits in a string, 
the string will be long and difficult to work with. 
Requests’ iter_content( ) generator downloads a portion of the web page at a time.
We can use this generator to download the data and store it in a file, which is more easily accessible 
than a string.
Sometime when the file is large and the network connection is slow, we need to put a 
timer on the request so that the code is not blocked indefinitely.
requests.get(‘a_url', timeout=2)
The timer is in seconds. It is the max number of seconds that elapse since the last server response, 
it is not the total download time.
Last but not least, if the download time is long and there are multiple downloads that we must do, 
then threads or multiprocessing is a good solution.

'''
'''
page = requests.get('https://python.org/')
with open("ex5output.txt", 'wb') as outfile :        # can use .txt extension here because the page format is text/html
    for block in page.iter_content(chunk_size=128):
        outfile.write(block)
print("done")
'''

# beautiful soup
'''
BeautifulSoup accepts a Response object byte string, either from urllib or from Requests, 
nd a parser choice. “lxml” is the recommended parser for its speed and flexibility with HTML / XML standards.
BeaufifulSoup returns a BeautifulSoup object, which has methods that can help us get data from the Response 
object byte string.
'''

#page = requests.get('https://python.org/')
#soup = BeautifulSoup(page.content, "lxml")         
#print(soup.prettify()[0:4000])                     
#print(soup.prettify().encode("utf8")[0:6000])      
                                                
#print(soup.find('head'))                           
#print(soup.title)     #<title>Welcome to Python.org</title>                             

#for tag in soup.find_all(re.compile('b')) :        
    #print(tag.name)
    
'''
body
label
button
blockquote
table
tbody
b
b
b
b
b
'''

#for tag in soup.find_all(['image', 'table']) :     
    #print(tag)  
'''
<table border="0" cellpadding="0" cellspacing="0" class="quote-from" width="100%">
<tbody>
<tr>
<td><p><a href="/success-stories/industrial-light-magic-runs-python/">Industrial Light &amp; Magic Runs on Python</a> <em>by Tim Fortenberry</em></p></td>
</tr>
</tbody>
</table>
'''
    
#print(soup.b)              #<b>Web Development</b>                         
#for tag in soup.find_all('b') :                    
    #print(tag)                                     
    #print(tag.get_text())    
'''
<b>Web Development</b>
Web Development
<b>GUI Development</b>
GUI Development
<b>Scientific and Numeric</b>
Scientific and Numeric
<b>Software Development</b>
Software Development
<b>System Administration</b>
System Administration
'''

#for link in soup.find_all('a'):                    
    #print(link.get('href'))  #return all links(website url) 
    
#for tag in soup.find_all(True) :                   
    #print(tag.name)  #returns all tag name, 'a' 'div', 'ul' etc

#print(soup.get_text().encode("utf8"))   #print a lot of \n and other information

    
#print(soup.find_all(string='Python'))              
#print(soup.find_all(string=re.compile('python', re.I)))      
#print(soup.find_all('a', string=re.compile('python')))       

#for tag in soup.find_all('div') :                  
    #print(tag.encode("utf8"))                     
#print(soup.find_all('div', class_="copyright"))    
#print(soup.select('div.copyright'))
#print(soup.find_all(id="success-story-2"))    #both works the same       
#print(soup.select('div#success-story-2'))    #both works the same
#print(soup.select('div p a'))                       


# using web API

page = requests.get("http://api.open-notify.org/iss-now.json")    #international space station
jDict = page.json()
print(jDict)
print()
print("Current time:", time.ctime(jDict['timestamp']))
print("Latitude:", jDict['iss_position']['latitude'], "\nLongitude:", jDict['iss_position']['latitude'])
'''
{'message': 'success', 'timestamp': 1521132906, 'iss_position': {'longitude': '52.6879', 'latitude': '-6.3272'}}

Current time: Thu Mar 15 09:55:06 2018
Latitude: -6.3272 
Longitude: -6.3272
'''

# To take it further, we can install and use the geopy module: https://pypi.python.org/pypi/geopy
# which will return a map location for a particular latitude,longitude
# We can also use the google map api: 
#  https://developers.google.com/maps/documentation/geocoding/intro#ReverseGeocoding
# which will return json formatted data with the map location of the latitude,longitude


'''
# find registration dates for de anza
# "https://www.deanza.edu/calendar/springdates.html"


'''
