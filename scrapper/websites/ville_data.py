# from scrapper_handler import ScrapperHandler

from scrapper_handler import ScrapperHandler


class VilleDataHandler(ScrapperHandler):
    def __init__(self, driver_path, url) -> None:
        super().__init__(driver_path, url)

    def get_region_urls(self):
        self.driver.get(self.url)
        table = self.driver.find_element_by_xpath("//table")
        terrains_elements = table.find_elements_by_tag_name("a")
        region_urls = []
        for el in terrains_elements:
            region_urls.append(el.get_attribute("href"))
        return region_urls

    def get_departement_urls(self):
        department_urls = []
        for region_url in self.get_region_urls():
            self.driver.get(region_url)

            assertion = self.driver.find_elements_by_xpath(
                "//*[contains(text(), 'Terrains de pétanque Carte Complète, Adresse et Avis par département : ')]"
            )
            if len(assertion) == 0:
                department_urls.append(region_url)
            else:
                departement_elements = self.driver.find_elements_by_tag_name("article")
                departement_ul = departement_elements[0].find_elements_by_tag_name("ul")

                departement_list = departement_ul[0].find_elements_by_tag_name("a")

                for el in departement_list:
                    department_urls.append(el.get_attribute("href"))
        return department_urls

    def get_terrain_urls(self):
        terrain_urls = []
        for departement_url in self.get_departement_urls():
            self.driver.get(departement_url)
            terrains_buttons = self.driver.find_elements_by_id("boutondetail")
            for el in terrains_buttons:
                terrains_lists = el.find_element_by_tag_name("a")
                terrain_urls.append(terrains_lists.get_attribute("href"))
        print(terrain_urls)
        return terrain_urls

    def get_bestsellers_list(self):
        try:
            driver = webdriver.Chrome(self.__driver_path)
        except Exception as e:
            raise e
        driver.get(self.__url)
        time.sleep(1)
        bestsellers_web_element = driver.find_elements_by_class_name("bestsellers")[
            0
        ].text
        bestsellers_list = bestsellers_web_element.split("\n")
        bestseller_assert = bestsellers_list[0]
        assert "Bestsellers (showing last 30 days in all genres)" in bestseller_assert

        bestsellers_list = [x for x in bestsellers_list if "Play All" not in x]
        offset = bestsellers_list.index("Reset")
        bestsellers_list = bestsellers_list[offset + 1 :]
        x = 0
        bestsellers = []
        for i in range(len(bestsellers_list)):
            if i % 3 == 0:
                bestsellers.append(bestsellers_list[i])
        bestsellers = [" ".join(x.split(" - ")) for x in bestsellers]
        return bestsellers
