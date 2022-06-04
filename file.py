from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('./chromedriver')
browser.get(starturl)
time.sleep(10)

def scrape():
    headers = ['V Mag.', 'Proper Name', 'Bayer designation', 'Distance', 'Spectral class']
    planetData = []
    for i in range(0,490):
        #we have to repeat the same code for each page
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        #convert the page into html format.
        for ul_tag in soup.find_all('th', attrs = {'class', 'headerSort'}):
            #where the class of <ul> tag is exoplanet
            li_tags = ul_tag.find_all('td')
            tempList = []
            for index, li_tag in enumerate(li_tags):
                #will return both index and element of that index no.
                if index ==0:
                    tempList.append(li_tag.find_all('a')[0].contents[0])
                    #go inside the a tag, then inside the 0th element of that list
                else:
                    try:
                        tempList.append(li_tag.contents[0])
                    except:
                        tempList.append('')

            planetData.append(tempList)
        
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/thead/tr/th[1]').click()
        
        #xpath will be used to find the element in the webpage and click onit
        time.sleep(3)
    with open('scrape.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetData)


scrape()

