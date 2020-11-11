from bs4 import BeautifulSoup as bs
import json

database = {}

with open('index.html','r',encoding='utf-8') as infile:
  raw = infile.read()
  soup = bs(raw, 'html.parser')
  sections = soup.find_all("div",{"class":"page-section__widget"})
  for section in sections:
    header = section.find("header")
    hTitle = header.find("span").text
    headerTitle = hTitle.replace("\n","").strip()
    print(headerTitle)
    database[headerTitle] = {}
    links = section.find_all("li")
    section_links = []
    for link in links:
      anchor = link.find("a",{"class":"bookmark-item__link"})
      anchor_text = anchor.text.strip()
      print(anchor_text)
      # print(anchor.text)
      # print(anchor['href'])
      section_links.append({"title":anchor_text,"url":anchor['href']})
    database[headerTitle]['links'] = section_links

with open('all_links.json','w',encoding='utf-8') as outfile:
  jsonData = json.dumps(database)
  outfile.write(jsonData)
