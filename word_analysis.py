import requests             
from bs4 import BeautifulSoup 
import csv                  
import webbrowser
import io
import datetime
import matplotlib.pyplot as plt
import numpy as np
import basic_stat
from selenium import webdriver
import time

url = 'https://www.tripadvisor.in/Attraction_Review-g297687-d13171435-Reviews-Trekmunk-Dehradun_Dehradun_District_Uttarakhand.html'

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# # change it to where you have it
# path = "/home/rohan/Downloads/chromedriver_linux64/chromedriver"
# driver = webdriver.Chrome(path, chrome_options=options)


# to get all the latest reviews and store it in a file

# def get_all_reviews(url):
#     url_temp1 = 'https://www.tripadvisor.in/Attraction_Review-g297687-d13171435-Reviews-or'
#     url_temp2 = '-Trekmunk-Dehradun_Dehradun_District_Uttarakhand.html'
#     page_ind = 0
#     f = open("reviews.txt", "w+")
#     review_count = 0
#     while True:
#         if review_count >= basic_stat.total_reviews:
#             break
#         if page_ind >= 10:
#             url = url_temp1 + str(page_ind) + url_temp2
        
#         wp = requests.get(url)
#         soup = BeautifulSoup(wp.content, "html.parser")
#         reviews = soup.find_all('div', class_='reviewSelector')
#         pre_url = 'https://www.tripadvisor.in'
#         for div in reviews:
#             suff = div.find('a', href=True)
#             if suff is not None:
#                 suff = suff['href']
#                 vis_url = pre_url + suff
#                 result = requests.get(vis_url)
#                 tsoup = BeautifulSoup(result.content, "html.parser")
#                 req = tsoup.find('span', class_='fullText')
#                 if req is not None:
#                     review = req.text
#                     review = review + '\n'
#                     f.write(review)
#                     review_count += 1
#         page_ind += 10
#     f.close()

def word_analysis():
    # get_all_reviews(url)
    pass