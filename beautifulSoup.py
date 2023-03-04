from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
y_news = response.text

ID = "35008392"

soup = BeautifulSoup(y_news, "html.parser")
title_of_news = soup.find_all(name="tr", class_="athing")
# print(title_of_news)

artical_titles = []
artical_links = []

for news in title_of_news:
    title_name = news.select(selector="a")
    # print(title_name)
    for tag in title_name:
        if tag.text != "":
            artical_titles.append(tag.text)
            artical_links.append(tag.get("href"))

    upscore = soup.find_all(name="span", class_="score")
    artical_score = [score.getText() for score in upscore]


# print(artical_titles)
# print(artical_links)
final_score = [int(score.split(" ")[0]) for score in artical_score]
maximun_score_index = final_score.index(max(final_score))


print(artical_titles[maximun_score_index])
print(artical_links[maximun_score_index])
print(max(final_score))



# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# content = soup.find_all(name="a")
# # print(content)
#
# # for tag in content:
#     # print(tag.get("href"))
#     # print(tag.getText())
# # print(soup.prettify())
#
# # print(soup.find(name="h1", id="name").getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
