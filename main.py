from bs4 import BeautifulSoup
import requests
# with open("website.html") as website:
#     contents = website.read()

# soup = BeautifulSoup(contents, "html.parser")

# anchors = soup.find_all(name="a")

# print(anchors)

response = requests.get("https://news.ycombinator.com/news")