import logging
from lxml import html
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
LOGGER.setLevel(logging.CRITICAL)

class KeywordTool(object):
    sources = {'google', 'youtube', 'bing', 'amazon', 'ebay', 'app-store'}
    
    def __init__(self, source='google', timeout=5):
        self.source = source
        self.base_url = None
        self.timeout = timeout
        self.driver = PhantomJS()
        self.driver.get(self.base_url)
    
    def search(self, search_term):
        if self.current_url != self.base_url:
            self.source = self.source  # forces page load
        self.driver.find_element_by_xpath('//input[@id="edit-keyword"]').send_keys(search_term)
        self.driver.find_element_by_xpath('//button[@id="edit-submit"]').click()
    
        """Wait for at least one element to load. In practice, most of them load. You can't get them all without scrolling."""
        element_not_present = EC.invisibility_of_element_located((By.XPATH, '//td[@class="col-keywords"]//div'))
        WebDriverWait(self.driver, self.timeout).until(element_not_present)
    
    def parse(self):
        tree = html.fromstring(self.driver.page_source)
        L = tree.xpath('//td[@class="col-keywords"]//text()')
        L = map(lambda s: s.strip(), ''.join(L).split('\n'))
        return [s for s in L if s]
    
    def get_keywords(self, search_term, source='google'):
        if self.source != source:
            self.source = source
        self.search(search_term)
        return self.parse()
        
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, val):
        self._source = val if val in self.sources else 'google'
        if 'driver' in self.__dict__:
            self.driver.get(self.base_url)
    
    @property
    def base_url(self):
        return ''.join(['https://keywordtool.io/', self.source])
    
    @base_url.setter
    def base_url(self, val):
        pass
    
    @property
    def current_url(self):
        return self.driver.current_url
    
    @current_url.setter
    def current_url(self, val):
        pass