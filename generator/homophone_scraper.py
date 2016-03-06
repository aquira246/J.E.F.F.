import sys
import string
import requests
import json
import time 
from bs4 import BeautifulSoup
from selenium import webdriver

def getMaxPageNumber(bsSource):
    # Pagnination keeps track of the page numbers
    pagination = bsSource.find('ul', {"class" : "pagination"})

    # Pagination does not exist because its only a single page
    if not pagination:
        return 1

    paginationList = pagination.findAll('li')

    # Get second to last one because last one is next page
    return int(paginationList[-2].text)

def getAllHomophonesFromLetter(browser, letter):
    homophonesPerLetter = []

    pageNumber = 1
    while True:
        url = "http://www.homophone.com/search?page=" + str(pageNumber) + \
         "&q=" + str(letter)
        browser.get(url)

        # Default lxml because idc about the parser
        bs = BeautifulSoup(browser.page_source, "lxml")

        # If its the first page, try to find the max page number
        if pageNumber == 1:
            maxPageNumber = getMaxPageNumber(bs)

        # If its past the last page, stop
        if pageNumber == maxPageNumber + 1:
            break

        # Find all cards
        for card in bs.findAll('div', {"class" : "card"}):
            cardWords = []

            # Find all words in the card
            for word in card.findAll('a', {"class" : "btn"}):
                sys.stdout.write(word.text + ',')
                cardWords.append(word.text)

            # Make sure that its non zero
            if len(cardWords) != 0:
                homophonesPerLetter.append(cardWords)
            
            sys.stdout.write('\n')

        # Go to next page
        pageNumber = pageNumber + 1

        time.sleep(1)
    return homophonesPerLetter

def getHomophonesFromWebpage():
    homophones = []
    browser = webdriver.Firefox()

    # Go through every letter of the alphabet
    for letter in list(string.ascii_lowercase):
        homophones.extend(getAllHomophonesFromLetter(browser, letter))

        time.sleep(1)
    browser.close()
    return homophones

def main():
    print json.dumps(getHomophonesFromWebpage())
    return 0

if __name__ == "__main__":
    sys.exit(main())
    
