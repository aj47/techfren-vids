# filename: stackoverflow_scrapper.py

import requests
from bs4 import BeautifulSoup
import json

# The URL of StackOverflow's homepage
url = 'https://stackoverflow.com/'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the webpage's content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the posts
posts = soup.find_all(class_='summary')

# A list to store all the posts
post_data = []

for post in posts:
    post_details = {}
    title = post.find('a', class_='question-hyperlink')

    if title:
        post_details['title'] = title.text.strip()
        post_details['link'] = url + title['href']
        
    post_data.append(post_details)

# Write the post data into a file called 'stackoverflow_posts.json'
with open('stackoverflow_posts.json', 'w') as json_file:
    json.dump(post_data, json_file, indent=4)