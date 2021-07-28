from bs4 import BeautifulSoup

with open("website.html") as website:
    contents = website.read()

soup = BeautifulSoup(contents, "html.parser")



print(soup.find_all(name="a"))