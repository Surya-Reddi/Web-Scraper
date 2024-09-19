import requests
from bs4 import BeautifulSoup

def main():
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    
    # print (response.text)
    soup = BeautifulSoup(response.content, "html.parser")
    
    quotes = soup.find_all("span", attrs={"class":"text"})
    authors = soup.find_all("small", attrs={"class": "author"})
   
    for q,a in zip(quotes,authors):
        print( q.text + "-" + a.text)
    
if __name__ == "__main__" :
    main()
