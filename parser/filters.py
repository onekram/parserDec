from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Filters:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def calendar(self, start1: str = None, start2: str = None, end1: str = None, end2: str = None):
        date_inputs = self.driver.find_elements(By.TAG_NAME, 'p-calendar')
        for date, inp in zip(date_inputs, [start1, start2, end1, end2]):
            if inp is not None:
                date.find_element(By.TAG_NAME, 'input').send_keys(inp)
                date.find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)

    def status(self, attrs: list[str]):
        for name in attrs:
            if name is None:
                continue
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[0]
            elem.click()
            ActionChains(self.driver).pause(1).perform()
            inp = self.driver.find_element(By.TAG_NAME, 'fgis-select-dropdown').find_elements(By.TAG_NAME, 'input')[0]
            inp.send_keys(name)
            ActionChains(self.driver).pause(1).perform()
            inp_select = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options').find_element(By.CLASS_NAME,
                                                                                                 'virtual-list')
            inp_select.click()

    def type_dec(self, attrs: list[str]):
        for name in attrs:
            if name is None:
                continue
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[1]
            elem.click()
            ActionChains(self.driver).pause(1).perform()
            inp = self.driver.find_element(By.TAG_NAME, 'fgis-select-dropdown').find_elements(By.TAG_NAME, 'input')[0]
            inp.send_keys(name)
            ActionChains(self.driver).pause(1).perform()
            inp_select = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options').find_element(By.CLASS_NAME,
                                                                                                 'virtual-list')
            inp_select.click()

    def type_obj_dec(self, attrs: list[str]):
        for name in attrs:
            if name is None:
                continue
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[2]
            elem.click()
            ActionChains(self.driver).pause(1).perform()
            inp = self.driver.find_element(By.TAG_NAME, 'fgis-select-dropdown').find_elements(By.TAG_NAME, 'input')[0]
            inp.send_keys(name)
            ActionChains(self.driver).pause(1).perform()
            inp_select = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options').find_element(By.CLASS_NAME,
                                                                                                         'virtual-list')
            inp_select.click()

    def origin(self, attrs: list[str]):
        for name in attrs:
            if name is None:
                continue
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[3]
            elem.click()
            ActionChains(self.driver).pause(1).perform()
            inp = self.driver.find_element(By.TAG_NAME, 'fgis-select-dropdown').find_elements(By.TAG_NAME, 'input')[0]
            inp.send_keys(name)
            ActionChains(self.driver).pause(1).perform()
            inp_select = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options').find_element(By.CLASS_NAME,
                                                                                                         'virtual-list')
            inp_select.click()

    def RF_product_groups(self, attrs: list[str]):
        if any(attrs):
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[4]
            elem.click()
            ActionChains(self.driver).pause(1).perform()

            for name in attrs:
                if name is None:
                    continue
                inp = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__filter').find_element(By.CLASS_NAME,
                                                                                                     'fgis-selectbox__filter-input')
                inp.send_keys(name)
                ActionChains(self.driver).pause(1).perform()

                try:
                    inp_expand = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options-expand')
                    inp_expand.click()
                    ActionChains(self.driver).pause(1).perform()
                except:
                    pass

                inp_choice = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options-leaf').find_element(
                    By.CLASS_NAME, 'fgis-selectbox__options__name')
                inp_choice.click()
                ActionChains(self.driver).pause(1).perform()
                # inp_select = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options').find_element(By.CLASS_NAME,
                #                                                                                              'virtual-list')
                # inp_select.click()

    def EAS_product_groups(self, attrs: list[str]):
        if any(attrs):
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[5]
            elem.click()
            ActionChains(self.driver).pause(1).perform()

            for name in attrs:
                if name is None:
                    continue
                inp = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__filter').find_element(By.CLASS_NAME,
                                                                                                     'fgis-selectbox__filter-input')
                inp.send_keys(Keys.CONTROL + 'A' + Keys.BACK_SPACE)
                inp.send_keys(name)
                ActionChains(self.driver).pause(1).perform()

                try:
                    inp_expand = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options-expand')
                    inp_expand.click()
                    ActionChains(self.driver).pause(1).perform()
                except:
                    pass

                inp_choice = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options-leaf').find_element(
                    By.CLASS_NAME, 'fgis-selectbox__options__name')
                inp_choice.click()
                ActionChains(self.driver).pause(1).perform()

    def EAS_product_single_list(self, attrs: list[str]):
        if any(attrs):
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[6]
            elem.click()
            ActionChains(self.driver).pause(1).perform()

            for name in attrs:
                if name is None:
                    continue
                inp = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__filter').find_element(By.CLASS_NAME,
                                                                                                     'fgis-selectbox__filter-input')
                inp.send_keys(name)
                ActionChains(self.driver).pause(1).perform()

                try:
                    inp_expand = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options-expand')
                    inp_expand.click()
                    ActionChains(self.driver).pause(1).perform()
                except:
                    pass

                # while:
                #     inp_choice = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options-leaf').find_element(
                #         By.CLASS_NAME, 'fgis-selectbox__options__name')
                #     inp_choice.click()
                ActionChains(self.driver).pause(1).perform()

    def RF_product_sigle_list(self, attrs: list[str]):
        if any(attrs):
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[7]
            elem.click()
            ActionChains(self.driver).pause(1).perform()

            for name in attrs:
                if name is None:
                    continue
                inp = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__filter').find_element(By.CLASS_NAME,
                                                                                                     'fgis-selectbox__filter-input')
                inp.send_keys(name)
                ActionChains(self.driver).pause(1).perform()

                try:
                    inp_expand = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options-expand')
                    inp_expand.click()
                    ActionChains(self.driver).pause(1).perform()
                except:
                    pass

                inp_choice = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options-leaf').find_element(
                    By.CLASS_NAME, 'fgis-selectbox__options__name')
                inp_choice.click()
                ActionChains(self.driver).pause(1).perform()

    def Technical_regulation(self, attrs: list[str]):
        if any(attrs):
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[8]
            elem.click()
            ActionChains(self.driver).pause(1).perform()

            for name in attrs:
                if name is None:
                    continue
                inp = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__filter').find_element(By.TAG_NAME,
                                                                                                                'input')
                inp.send_keys(name)
                ActionChains(self.driver).pause(1).perform()

                inp_select = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options').find_element(By.CLASS_NAME,
                                                                                                             'virtual-list')
                inp_select.click()

    def Application_type(self, attrs: list[str]):
        if any(attrs):
            elem = self.driver.find_elements(By.CLASS_NAME, 'fgis-selectbox__single')[9]
            elem.click()
            ActionChains(self.driver).pause(1).perform()

            for name in attrs:
                if name is None:
                    continue
                inp = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__filter').find_element(By.TAG_NAME,
                                                                                                     'input')
                inp.send_keys(name)
                ActionChains(self.driver).pause(1).perform()

                inp_select = self.driver.find_element(By.CLASS_NAME, 'fgis-selectbox__options').find_element(By.CLASS_NAME,
                                                                                                             'virtual-list')
                inp_select.click()

    def send_filters(self):
        btn = self.driver.find_element(By.XPATH,
                                       '//div[@class="advanced-search__footer d-flex"]/button[@class="btn btn_primary"]')
        btn.click()


if __name__ == '__main__':
    with webdriver.Chrome() as driver:
        driver.get('https://pub.fsa.gov.ru/rds/declaration')
        wb_filter = Filters(driver)
        ActionChains(driver).pause(3).perform()
        wb_filter.calendar('12.12.1212')
        wb_filter.status(['Действует'])
        ActionChains(driver).pause(3).perform()