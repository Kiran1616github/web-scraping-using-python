import requests
from bs4 import BeautifulSoup
url = "https://stackoverflow.com/questions/tagged/python"
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, "html.parser")


elem = soup.select('.s-post-summary--content-title')
print(elem)