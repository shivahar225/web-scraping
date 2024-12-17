from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

#print(soup.title)

article = soup.find(name="a")
article_text = article.getText
article_link = article.getText("href")
article_upvote = soup(name="span", class_="score")

#print(article)
#print(article_text)
#print(article_link)
#print(article_upvote)


article_texts = []


for article_tag in article:
    text = article_tag.getText()
    article_texts.append(text)

#print(article_texts)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)

#print(largest_number)

