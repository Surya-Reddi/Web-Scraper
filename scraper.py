import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/jobs"
    response = requests.get(url)
    
    # print (response.content)
    soup = BeautifulSoup(response.content, "html.parser")
    
    elements = soup.find_all(class_ = "titleline")
    sites = [e.find_next(class_ = "sitestr") for e in elements]
    
    print(f"Elements : {len(elements)}")
    print(f"Sites : {len(sites)}")
    
    for e in elements:
        print(e.get_text())
    
if __name__ == "__main__" :
    main()
