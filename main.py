from bs4 import BeautifulSoup
import requests
# with open("website.html") as website:
#     contents = website.read()

# soup = BeautifulSoup(contents, "html.parser")

# anchors = soup.find_all(name="a")

# print(anchors)

response = requests.get("https://news.ycombinator.com/news").text

# print(website)


soup = BeautifulSoup(response, "html.parser")



articleText = soup.find(name="a", class_="storylink").getText()

articleLink = soup.find(name="a", class_="storylink").get("href")

articleUpvote = (soup.find(name="span", class_="score").getText())

print(articleText)
print(articleText)
print(articleUpvote)