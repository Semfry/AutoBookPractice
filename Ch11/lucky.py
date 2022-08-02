# lucky.py - Opens several Google search results

import requests, sys, webbrowser, bs4

print("Googling...")  # display text while downloading the Google page
res = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status

# Retrieve top search result link
soup = bs4.BeautifulSoup(res.text, features="lxml")


# Open a browser tab for each result
LinkElems = soup.select(".r a")
numOpen = min(5, len(LinkElems))
for i in range(numOpen):
    webbrowser.open("http://google.com" + LinkElems[i].get("href"))
