import requests
from bs4 import BeautifulSoup
import time

#list for storing links
list=["https://en.wikipedia.org/wiki/Philosophy"]

#wikipedia link for Philosophy page
phy="https://en.wikipedia.org/wiki/Philosophy"

#function for searching hisory of urls
def continue_crawl(list,url):
    for l in list:
        if l==url:
            return True
    return False

s="https://en.wikipedia.org"

#user input for random wikipedia page
url=raw_input("Enter the link to your wikipedia page\n")
search=False

while search==False:
    list.append(url)
    r=requests.get(url)
    html=r.text
    soup = BeautifulSoup(html, 'html.parser')
    next=soup.p.a.get("href")
    n=str(next)
    url=s+n
    print(url)
    #time sleep so that continous request can be avoided 
    time.sleep(1)
    search=continue_crawl(list,url)

#checking if loop termination is due to philosophy page or due to revisiting same site    
if list[-1]==phy:
    print("philosophy page has been reached")
else:
    print("crawaler has struck into loop")
