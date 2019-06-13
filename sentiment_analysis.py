import requests             
from bs4 import BeautifulSoup 
import csv                  
import webbrowser
import io
import datetime
import matplotlib.pyplot as plt
import numpy as np

url = 'https://www.tripadvisor.in/Attraction_Review-g297687-d13171435-Reviews-Trekmunk-Dehradun_Dehradun_District_Uttarakhand.html'

def get_datetime(date_str):
    i = 0
    date = ""
    month = ""
    year = int(date_str[len(date_str) - 4:])
    while i < len(date_str):
        if date_str[i].isnumeric():
            date += date_str[i] 
            i += 1
        else:
            i += 1
            break
    date = int(date)
    months = {"January" : 1, "February" : 2,
              "March" : 3, "April" : 4,
              "May" : 5, "June" : 6, "July" : 7,
              "August" : 8, "September" : 9,
              "October" : 10, "November" : 11,
              "December" : 12}
    while i < len(date_str):
        if date_str[i].isalpha():
            month += date_str[i]
            i += 1
        else:
            break
    month = months[month]
    return datetime.datetime(year, month, date)



def get_review_dates(url, total_reviews):
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
    # for date in review_dates:
    #     print(date)
    return review_dates

# returns dictionary of frequency after plotting
def plot_reviews(rev_dates):
    temp_rev = rev_dates[::-1]
    freq = {}
    x = []
    y = []
    for date in temp_rev:
        if date not in freq:
            freq[date] = 1
            x.append(date)
        else:
            freq[date] += 1
    for date in x:
        y.append(freq[date])
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    plt.plot(x, y)
    plt.xticks(np.arange(0, len(x), 10))
    plt.show()
    return freq

def min_max_days(freq):
    min_days = []
    min_value = float('inf')
    for date in freq:
            min_value = min(min_value, freq[date])
    for date in freq:
        if freq[date] == min_value:
            min_days.append(date)
    max_days = []
    max_value = -1
    for date in freq:
            max_value = max(max_value, freq[date])
    for date in freq:
        if freq[date] == max_value:
            max_days.append(date)
    print('Day(s) with maximum reviews: ')
    for date in max_days:
        print(date)
    print('Day(s) with minimum reviews: ')
    for date in min_days:
        print(date)
    
def week_with_max_rev(rev_dates, freq):

    i = 0
    cur_date = rev_dates[0]
    best_start = None
    optimal = -1
    n = len(rev_dates)
    step = datetime.timedelta(days=7)
    while i < n:
        j = i
        loc_val = 0
        cur_date = get_datetime(rev_dates[i])
        while j < n:
            if (get_datetime(rev_dates[j]) - cur_date) > step:
                break
            if j > 0:
                if rev_dates[j] != rev_dates[j - 1]:
                    loc_val += freq[rev_dates[j]]
            j += 1
        i = j
        if loc_val > optimal:
            best_start = cur_date
            optimal = loc_val
    print("The best week from {} to {} had {} reviews".format(best_start.strftime("%x"), (best_start + step).strftime("%x"), optimal))

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
    rev_dates = get_review_dates(url, total_reviews)
    if len(rev_dates) > 0:
        print('Start date of reviews: {}'.format(rev_dates[total_reviews - 1]))
        print('End date of reviews: {}'.format(rev_dates[0]))
        
    d1 = get_datetime(rev_dates[0])
    d2 = get_datetime(rev_dates[total_reviews - 1])
    no_of_weeks = (d1 - d2).days // 7
    avg_rev = total_reviews / no_of_weeks
    print("Average number of reviews: {}".format(avg_rev))
    freq = plot_reviews(rev_dates)
    week_with_max_rev(rev_dates[::-1], freq)
    min_max_days(freq)


basic_stats(url)
