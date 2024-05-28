from selenium import webdriver
from bs4 import BeautifulSoup
import json

# Importing utils modules
from utils import generate_links
from utils import get_month_and_year

webpage_urls = generate_links()

all_project_links = []

for i, link in enumerate(webpage_urls):
    counter = 0
    # Step 1: Set up the WebDriver
    driver = webdriver.Chrome()  
    # Step 2: Fetch the web page
    driver.get(link)  

    # Step 3: Get the page source after JavaScript execution
    html = driver.page_source

    # Step 4: Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # Step 5: Extract the desired information
    project_links = soup.find_all('a', class_='h-full flex flex-1 flex-row items-center') 



    month, year = get_month_and_year(link)
    print(f"{year}'{month}")

    for project_link in project_links:
        counter += 1
        print(counter)
        project = {
            "Month": month, 
            "year": year,
            "monthly_rank": counter, 
            "project_link": project_link['href']
        }

        all_project_links.append(project)

    driver.quit()

# Write the array of objects to the JSON file
with open("unprocessed_links.json", 'w') as json_file:
    json.dump(all_project_links, json_file, indent=4)
