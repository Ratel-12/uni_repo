import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class ShopAppTester(unittest.TestCase):   

    def setUp(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

        self.driver.get("http://localhost:3000")
        self.driver.maximize_window()
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        buttons = self.driver.find_elements("xpath", "//button")
        while len(buttons):
            buttons[0].click()
            buttons = self.driver.find_elements("xpath", "//button")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        time.sleep(0.5)

    def test_app_title(self):
        self.assertTrue(self.driver.title == "React App")

    def test_nav_menu_present(self):
        self.assertFalse(len(self.driver.find_elements("xpath", "//nav")) == 0)

    def test_products_title(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        titles = self.driver.find_elements("xpath", "//h1")
        n_titles_found = 0
        for title in titles:
            if title.get_attribute("innerHTML") == "Products":
                n_titles_found += 1
        self.assertTrue(n_titles_found == 1)

    def test_cart_title(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        titles = self.driver.find_elements("xpath", "//h1")
        n_titles_found = 0
        for title in titles:
            if title.get_attribute("innerHTML") == "Shopping Cart":
                n_titles_found += 1
        self.assertTrue(n_titles_found == 1)

    def test_payments_title(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Payments" in link.get_attribute("innerHTML"):
                link.click()
                break
        titles = self.driver.find_elements("xpath", "//h1")
        n_titles_found = 0
        for title in titles:
            if title.get_attribute("innerHTML") == "Payments":
                n_titles_found += 1
        self.assertTrue(n_titles_found == 1)

    def test_nav_menu_links(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        n_nav_links_found = 0
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                n_nav_links_found += 1
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                n_nav_links_found += 1
            if "Payments" in link.get_attribute("innerHTML"):
                n_nav_links_found += 1
        self.assertTrue(n_nav_links_found == 3)

    def test_product_list(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        items = self.driver.find_elements("xpath", "//div[p and button]")
        n_correct_items_found = 0
        for item in items:
            if "Cod" in item.get_attribute("innerHTML"):
                n_correct_items_found += 1
            if "Coke" in item.get_attribute("innerHTML"):
                n_correct_items_found += 1
            if "Bread" in item.get_attribute("innerHTML"):
                n_correct_items_found += 1
        self.assertTrue(n_correct_items_found == 3)

    def test_button_present(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Payments" in link.get_attribute("innerHTML"):
                link.click()
                break
        buttons = self.driver.find_elements("xpath", "//button")
        self.assertTrue(len(buttons) == 1)

    def test_button_text(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Payments" in link.get_attribute("innerHTML"):
                link.click()
                break
        buttons = self.driver.find_elements("xpath", "//button")
        has_correct_text = False
        for button in buttons:
            if "Pay" in button.get_attribute("innerHTML"):
                has_correct_text = True
        self.assertTrue(has_correct_text)

    def test_routing1(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        self.assertTrue(self.driver.current_url == "http://localhost:3000/")
    
    def test_routing2(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        self.assertTrue(self.driver.current_url == "http://localhost:3000/cart")
    
    def test_routing3(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Payments" in link.get_attribute("innerHTML"):
                link.click()
                break
        self.assertTrue(self.driver.current_url == "http://localhost:3000/payments")

    def test_remove_all(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        buttons = self.driver.find_elements("xpath", "//button")
        for button in buttons:
            button.click()
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        buttons = self.driver.find_elements("xpath", "//button")
        while len(buttons):
            buttons[0].click()
            buttons = self.driver.find_elements("xpath", "//button")
        self.assertTrue(len(buttons) == 0)

    def test_remove_one(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        buttons = self.driver.find_elements("xpath", "//button")
        for button in buttons:
            button.click()
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        buttons = self.driver.find_elements("xpath", "//button")
        prev_len = len(buttons)
        if prev_len:
            buttons[0].click()
        buttons = self.driver.find_elements("xpath", "//button")
        curr_len = len(buttons)
        self.assertTrue(prev_len - curr_len == 1)

    def test_single_coke(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        product_divs = self.driver.find_elements("xpath", "//div[p and button]")
        for item in product_divs:
            if "Coke" in item.get_attribute("innerHTML"):
                button = item.find_element("xpath", ".//button")
                button.click()
                break
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        cart_items = self.driver.find_elements("xpath", "//div[p and button]")
        hits = 0
        for item in cart_items:
            if "Coke" in item.get_attribute("innerHTML"):
                hits += 1
        self.assertTrue(hits == 1)

    def test_single_bread(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        product_divs = self.driver.find_elements("xpath", "//div[p and button]")
        for item in product_divs:
            if "Bread" in item.get_attribute("innerHTML"):
                button = item.find_element("xpath", ".//button")
                button.click()
                break
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        cart_items = self.driver.find_elements("xpath", "//div[p and button]")
        hits = 0
        for item in cart_items:
            if "Bread" in item.get_attribute("innerHTML"):
                hits += 1
        self.assertTrue(hits == 1)

    def test_single_cod(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        product_divs = self.driver.find_elements("xpath", "//div[p and button]")
        for item in product_divs:
            if "Cod" in item.get_attribute("innerHTML"):
                button = item.find_element("xpath", ".//button")
                button.click()
                break
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        cart_items = self.driver.find_elements("xpath", "//div[p and button]")
        hits = 0
        for item in cart_items:
            if "Cod" in item.get_attribute("innerHTML"):
                hits += 1
        self.assertTrue(hits == 1)

    def test_double_coke(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        product_divs = self.driver.find_elements("xpath", "//div[p and button]")
        for item in product_divs:
            if "Coke" in item.get_attribute("innerHTML"):
                button = item.find_element("xpath", ".//button")
                button.click()
                button.click()
                break
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        cart_items = self.driver.find_elements("xpath", "//div[p and button]")
        hits = 0
        for item in cart_items:
            if "Coke" in item.get_attribute("innerHTML"):
                hits += 1
        self.assertTrue(hits == 2)

    def test_double_bread(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        product_divs = self.driver.find_elements("xpath", "//div[p and button]")
        for item in product_divs:
            if "Bread" in item.get_attribute("innerHTML"):
                button = item.find_element("xpath", ".//button")
                button.click()
                button.click()
                break
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        cart_items = self.driver.find_elements("xpath", "//div[p and button]")
        hits = 0
        for item in cart_items:
            if "Bread" in item.get_attribute("innerHTML"):
                hits += 1
        self.assertTrue(hits == 2)

    def test_double_cod(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Products" in link.get_attribute("innerHTML"):
                link.click()
                break
        product_divs = self.driver.find_elements("xpath", "//div[p and button]")
        for item in product_divs:
            if "Cod" in item.get_attribute("innerHTML"):
                button = item.find_element("xpath", ".//button")
                button.click()
                button.click()
                break
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "Shopping Cart" in link.get_attribute("innerHTML"):
                link.click()
                break
        cart_items = self.driver.find_elements("xpath", "//div[p and button]")
        hits = 0
        for item in cart_items:
            if "Cod" in item.get_attribute("innerHTML"):
                hits += 1
        self.assertTrue(hits == 2)
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
