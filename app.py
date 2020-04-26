from selenium import webdriver
from pages.quote_page import QuotePage, NoSuchElementException

try:
    author = input("Enter the author you'd like quotes of: ")
    tag = input("Enter the tag you want: ")

    chrome = webdriver.Chrome(executable_path="/Users/daman/Downloads/chromedriver/chromedriver")
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotePage(chrome)
    print(page.search_for_quotes(author, tag))
except NoSuchElementException as e:
    print(e)
except Exception as e:
    print(e)
    print("An Unknown Error occurred. Please Try again later...")

'''
for quote in page.quotes:
    print("\n" + quote.content)
    print("- " + quote.author)
    print(quote.tags)
'''
'''
authors = page.get_available_authors()
print("Select one of these authors: [{}]".format(" | ".join(authors)))
author = input("Enter the author you'd like quotes of: ")
page.select_author(author)

tags = page.get_available_tags()
print("Select one of these tags: [{}]".format(" | ".join(tags)))
tag = input("Enter the tag you want: ")
page.select_tag(tag)

page.search_button.click()

quotes = page.quotes
for quote in quotes:
    print(quote)
'''
