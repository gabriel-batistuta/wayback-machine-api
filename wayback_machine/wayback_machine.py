from util import requisition
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json

class WaybackMachine:
    def __init__(self):
        self.DOMAIN_URL = 'https://web.archive.org/web/'
        '''
        https://web.archive.org/web/*/https://www.baka-tsuki.org/project/index.php?title=High_School_DxD
        '''
    def get_snapshots(self, url='https://www.baka-tsuki.org/project/index.php?title=High_School_DxD'):
        request_url = self.DOMAIN_URL+'*/'+url
        # url = 'https://web.archive.org/web/*/https://www.baka-tsuki.org/project/index.php?title=High_School_DxD'
        def _find_snapshots(self, request_url):
            DOMAIN_URL = 'https://www.baka-tsuki.org/project/index.php?title=High_School_DxD'
            options = Options()
            driver = webdriver.Chrome(options=options)
            driver.get(request_url)
            driver.maximize_window()
            driver.implicitly_wait(10)
            years_container = driver.find_element(By.ID,'year-labels')
            years = years_container.find_elements(By.CLASS_NAME,'sparkline-year-label')
            snapshot_list = []
            years_list = []
            for i in range(len(years)):
                years[i].click()
                time.sleep(3)
                days_month = driver.find_elements(By.XPATH, f'//a[contains(@href, "{url}")]')
                for j in days_month:
                    source_url = j.get_attribute('href')

                    def check_if_content(source_url):
                        keymap_not_site = ['https://web.archive.org/web/changes/', 'https://web.archive.org/details/', 'https://web.archive.org/web/sitemap/', 'https://web.archive.org/web/*/', 'https://web.archive.org/web/collections']
                        for key in keymap_not_site:
                            if key in source_url:
                                return False
                        return True

                    if source_url not in snapshot_list and check_if_content(source_url) is True:
                        print(f'{source_url}')
                        match = re.search(r'/web/(\d{8}|\d{14})/', source_url)
                        # date of snapshot (YYYY/MM/DD)
                        date = match.group(1)
                        snapshot = {
                            'date_snapshot':date,
                            'source_url':source_url
                        }
                        snapshot_list.append(snapshot)
                        file.write(source_url+'\n')
                years[i] = years[i].text
                years_list.append(years[i])
                file.write(years[i]+'\n\n')
            years_snapshots = []
            for year in years_list:
                snapshots_list = []
                for snapshot in snapshot_list:
                    if year in snapshot['source_url']:
                        snapshots_list.append(snapshot)
                year_obj = {
                    'year_snapshot':year,
                    'snapshots':snapshots_list
                }
                years_snapshots.append(year_obj)
            years_snapshots = {
                'years_snapshots':years_snapshots
            }
        
            return years_snapshots    
            driver.close()
        
        return _find_snapshots(request_url)

if __name__ == __main__:
    wayback = WaybackMachine().get_snapshots()