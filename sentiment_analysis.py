import requests             
from bs4 import BeautifulSoup 
import csv                  
import webbrowser
import io

url = 'https://www.tripadvisor.in/Attraction_Review-g297687-d13171435-Reviews-Trekmunk-Dehradun_Dehradun_District_Uttarakhand.html'


def review_dates(url, total_reviews):
    url_temp1 = 'https://www.tripadvisor.in/Attraction_Review-g297687-d13171435-Reviews-or'
    url_temp2 = '-Trekmunk-Dehradun_Dehradun_District_Uttarakhand.html'
    review_dates = []
    page_ind = 0
    while True:
        if len(review_dates) >= total_reviews:
            break
        if page_ind >= 10:
            url = url_temp1 + str(page_ind) + url_temp2
        page_ind += 10
        result = requests.get(url)
        # print(len(review_dates))
        if result.status_code != 200:
            break
        src = result.content
        soup = BeautifulSoup(src, "html.parser")
        spans = soup.find_all('span', {'class' : 'ratingDate'})
        for span in spans:
            try:
                review_dates.append(span.attrs['title'])
            except:
                continue
    print('Start date of reviews: {}'.format(review_dates[total_reviews - 1]))
    print('End date of reviews: {}'.format(review_dates[0]))


def basic_stats(url):
    result = requests.get(url)
    if result.status_code != 200:
        print('Could not fetch data!!!!')
        return
    src = result.content
    soup = BeautifulSoup(src, "html.parser")
    total_reviews = -1
    span = soup.find_all('span', {'class' : 'reviews_header_count'})
    if len(span) > 0:
        s = span[0].text
        total_reviews = s[1 : len(s) - 1]
    if total_reviews != -1:
        print("Total Reviews: {}".format(total_reviews))
    total_reviews = int(total_reviews)
    review_dates(url, total_reviews)

basic_stats(url)