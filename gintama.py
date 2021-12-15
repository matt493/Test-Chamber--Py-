#fetch all links of where id = "episode_related"
def getAllHrefFromPage(url):
    import requests
    from bs4 import BeautifulSoup

    #read a html page
    r = requests.get("https://gogoanime.wiki/category/gintama")
    soup = BeautifulSoup(r.text, "html.parser")
    #find all links in soup
    links = soup.find_all("a")
    print(links)