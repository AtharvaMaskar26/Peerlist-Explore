from selenium import webdriver
from bs4 import BeautifulSoup
import codecs
import time
from utils import remove_emojis
import json

database = []
# Open the text file in read mode
with open('processed_links.json', 'r') as json_file:
    processed_links = json.load(json_file)

with open('data.json', 'r') as json_file:
    radial_data = json.load(json_file)

counter = 0
for i, project in enumerate(processed_links):
    if i >= len(radial_data):
        try:
            # Step 1: Set up the WebDriver
            driver = webdriver.Chrome()  
            # Step 2: Fetch the web page
            driver.get(project['project_link'])  

            # Step 3: Get the page source after JavaScript execution
            html = driver.page_source

            # Step 4: Parse the HTML content
            soup = BeautifulSoup(html, 'html.parser')

            # Extracting Project Name
            project_name = soup.find('h1', class_='text-gray-gray1k font-semibold text-lg md:text-xl')  
            project_name = "" if project_name == None else project_name.get_text()

            # Extracting Project Subheading
            project_subheading = soup.find('h2', class_='text-primary font-normal text-sm md:text-base')
            project_subheading = "" if project_subheading == None else project_subheading.get_text()

            # Extracting image url
            # image_url = soup.find('img', class_='block max-h-[calc(100vh-40px)] rounded-lg w-full lg:h-[332px] h-[180px] object-cover')  
            # image_url = "" if image_url == None else image_url


            # Extracting Description
            description = soup.find('div', class_='px-4 lg:px-6 flex flex-col gap-4')  

            if description != None:
                text_description = description.find('div', class_='break-words text-primary text-sm rich-text-paragraph-regular link-break h-20 fade-overflow-text')
                text_description = "" if text_description == None else text_description.get_text()  
            else:
                text_description = ""

            # Extracting Month and Year
            # month_year = soup.find('p', class_='text-primary font-normal text-2xl font-instrument italic mt-2 group-hover:underline') 

            # Extracting number of comments
            # num_of_comments = soup.find_all('p', class_='text-green-bright font-normal text-xs flex justify-end')

            # Extracting number of upvotes 
            number_of_upvotes = soup.find('div', class_='px-3 border-l py-2 border-green-text')
            number_of_upvotes = "" if number_of_upvotes == None else number_of_upvotes  

                # Extracting Project By
                # project_by = soup.find_all('div', class_='flex flex-col gap-6')  
                # project_by = soup.find_all('p', class_='text-gray-gray1k font-semibold text-sm group-hover:underline')  
                # admins = project_by[1].find_all('div')

            # Read the existing data from the JSON file
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)

            project = {
                "link": project['project_link'],
                "monthly_rank": project['monthly_rank'],
                "project_name": project_name,
                "project_subheading": remove_emojis(project_subheading),
                # "image_url": image_url['src'],
                "description": remove_emojis(text_description),
                # "month_year": month_year.get_text(),
                "month": project['Month'], 
                "year": project['year'],
                "number_of_upvotes": number_of_upvotes.get_text(),
            }

            counter += 1
            existing_data.append(project)
            print(f"Counter: {counter}, Len: {len(existing_data)}, isEqual= {counter == len(existing_data)}")

            # Write the updated data back to the JSON file
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, indent=4)

            driver.quit()
        except Exception as e:
            print(e)
    else:
        pass

# with open("database.txt", "w", encoding="utf-8") as file:
#     for project in database:
#         file.write(f"{project}\n")

# Step 3: Write data to a JSON file
# with open('data.json', 'w') as json_file:
#     json.dump(database, json_file, indent=4)


