import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Set up Excel workbook wowedwd
excel = openpyxl.Workbook()
sheet = excel.active
sheet.append(["Rank", "Name", "Year", "Rating"])

# Set up Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the IMDB list page
    driver.get("https://www.imdb.com/list/ls046196709/")

    # Wait for the page to load
    driver.implicitly_wait(10)  # seconds

    # Find all movie items
    movie_items = driver.find_elements(By.CLASS_NAME, "lister-item-content")

    # Extract and append data to the Excel sheet
    for movie in movie_items:
        name = movie.find_element(By.TAG_NAME, "a").text
        year = movie.find_element(By.CLASS_NAME, "lister-item-year").text.strip('()')
        rating = movie.find_element(By.CLASS_NAME, "ipl-rating-star__rating").text
        rank = movie.find_element(By.CLASS_NAME, "lister-item-index").text.replace(".", "")
        sheet.append([rank, name, year, rating])

    # Save the Excel file
    excel.save("Scrap.xlsx")

except Exception as e:
    print("Error fetching or parsing data:", e)

finally:
    # Close the WebDriver
    driver.quit()
