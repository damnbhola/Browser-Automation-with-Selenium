from typing import List
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from locators.quote_page_locators import QuotePageLocators
from parsers.quote import QuoteParser
# for adding wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotePageLocators.QUOTE
        quote_tags = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(e) for e in quote_tags]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotePageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotePageLocators.TAG_DROPDOWN)
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(QuotePageLocators.SEARCH_BUTTON)

    def get_available_authors(self) -> List[str]:
        return [option.text.strip() for option in self.author_dropdown.options]

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tag_dropdown.options]

    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)

    def search_for_quotes(self, author: str, tag: str):
        self.select_author(author)
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_all_elements_located(
                (By.CSS_SELECTOR, QuotePageLocators.TAG_DROPDOWN_VALUE_OPTION)
            )
        )
        try:
            self.select_tag(tag)
        except NoSuchElementException:
            return f"Message: Author '{author}' does not have a tag '{tag}'."
        else:
            self.search_button.click()
            return self.quotes
