import pytest
from selenium.webdriver.common.by import By


@pytest.mark.sanity
class TestFirst:

    def test_chrome_tile(self, setup):
        menu_links = self.driver.find_element(By.ID, "link")
        assert menu_links.is_displayed() == True
