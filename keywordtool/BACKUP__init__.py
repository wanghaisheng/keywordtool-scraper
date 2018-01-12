import logging
from lxml import html
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
LOGGER.setLevel(logging.CRITICAL)

sources = {'google', 'youtube', 'bing', 'amazon', 'ebay', 'app-store'}

def get_keywords(search_term, source='google', timeout=5):
    """Choose URL based on search type"""
    source = source if source in sources else 'google'
    base_url = ''.join(['https://keywordtool.io/', source])
    
    """Submit search"""
    driver = PhantomJS()
    driver.get(base_url)
    driver.find_element_by_xpath('//input[@id="edit-keyword"]').send_keys(search_term)
    driver.find_element_by_xpath('//button[@id="edit-submit"]').click()
    
    """Wait for bottom of page to load -- some keywords won't be reached without scrolling, and I don't care"""
    element_present = EC.presence_of_element_located((By.XPATH, '//a[@title="Go to next page"]'))
    WebDriverWait(driver, timeout).until(element_present)

    """Use lxml to parse and return keywords"""
    tree = html.fromstring(driver.page_source)
    td = [s.strip().encode('ascii', 'ignore') for s in tree.xpath('//td[@class="col-keywords"]//text()')]
    return [s for s in td if s]
