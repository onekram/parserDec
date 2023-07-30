from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from parser.filters import Filters



class User_Parsing:
    def __init__(self, fil: dict[str, str | None]):
        self.fil = fil
        self.url = 'https://pub.fsa.gov.ru/rds/declaration'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'


    def start_parsing(self, num: int, headless: bool = False):
        options = webdriver.ChromeOptions()
        options.add_argument(f'--user-agent={self.user_agent}')
        if headless:
            options.add_argument('--headless')
        with webdriver.Chrome(options=options) as driver:
            driver.get(url=self.url)
            wb_filters = Filters(driver)
            ActionChains(driver).pause(1).perform()
            try:
                wb_filters.calendar(*self.fil['date1'], *self.fil['date2'])
                wb_filters.status([self.fil['status']])
                wb_filters.type_dec([self.fil['type_dec']])
                wb_filters.type_obj_dec([self.fil['type_obj_dec']])
                wb_filters.origin([self.fil['origin']])
                wb_filters.RF_product_groups([self.fil['rf_prod']])
                wb_filters.EAS_product_groups([self.fil['es_prod']])
                wb_filters.EAS_product_single_list([self.fil['es_list']])
                wb_filters.RF_product_sigle_list([self.fil['rf_list']])
                wb_filters.Technical_regulation([self.fil['tech']])
                wb_filters.Application_type([self.fil['type']])
                ActionChains(driver).pause(1).perform()
                wb_filters.send_filters()
                ActionChains(driver).pause(20).perform()
            except Exception as ex:
                return type(ex)
            else:
                return True