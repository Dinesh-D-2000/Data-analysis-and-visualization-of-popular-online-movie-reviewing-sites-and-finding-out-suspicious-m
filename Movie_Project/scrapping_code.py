import requests
from bs4 import BeautifulSoup
import openpyxl
excel=openpyxl.Workbook()
sheet=excel.active
sheet.append(["Rank","Name","Year","Rating"])

try:

    data = requests.get("https://www.imdb.com/list/ls046196709/")
    soup = BeautifulSoup(data.text, 'html.parser')

    movie_items = soup.find_all('div', class_='lister-item-content')

    for movie in movie_items:
        name = movie.find('a').text
        year = movie.find('span', class_='lister-item-year').text.strip('()')
        rating = movie.find('span', class_='ipl-rating-star__rating').text
        rank = movie.find('span', class_="lister-item-index").text.replace(".","")
        sheet.append([rank,name,year,rating])
    excel.save("Scrap.xlsx")

except Exception as e:
    print("Error fetching or parsing data:", e)
