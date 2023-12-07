from botcity.web import By
from botcity.web import WebBot
from typing import Tuple

class BasePage():
    """The BasePage class holds all common functionality across the website.
    """

    def __init__(self, driver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver
    
    def click(self, by_locator: Tuple[str, By]) -> None:
        """ Performs click on web element whose locator is passed to it"""
        self.driver.find_element(*by_locator).click()
    
    def send_keys(self, by_locator: Tuple[str, By], text: str) -> None:
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        self.driver.find_element(*by_locator).send_keys(text)