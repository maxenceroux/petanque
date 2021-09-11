from selenium import webdriver
from os import path
import time

class ScrapperHandler:
    def __init__(self, driver_path, url) -> None:
        self.driver_path = driver_path
        self.url = url
        try:
            path.isfile(self.driver_path)
        except Exception as e:
            print(f"Driver not in path: {e}")
            raise e
        try:
            self.driver = webdriver.Chrome(self.driver_path)
        except Exception as e:
            raise e

    def scrape_terrains(self):
        return False