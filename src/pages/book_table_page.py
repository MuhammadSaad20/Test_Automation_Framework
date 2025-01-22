from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class BookTablePage(BasePage):
    BOOK_MENU_LOCATOR = (By.ID, "menu-books-menu")  # Adjust according to the actual ID
    TABLE_OPTION_LOCATOR = (By.XPATH, "//li[@id='menu-books-list']")
    BOOK_TABLE_LOCATOR = (By.ID, "bookslisttable")  # Adjust based on actual table ID

    def __init__(self, driver):
        super().__init__(driver)  # Call the parent constructor to initialize the driver

    def navigate_to_table(self):
        self.hover(self.BOOK_MENU_LOCATOR)  # Hover over the 'Book' section
        self.click(self.TABLE_OPTION_LOCATOR)  # Click on 'Table' option
        # Assertion to verify that the table page has loaded (you can adjust the locator)
        self.wait_for_element(self.BOOK_TABLE_LOCATOR)  # Wait for the table to load
        assert self.driver.current_url == "https://thepulper.herokuapp.com/apps/pulp/gui/reports/books/table/navigation"  # Replace with the actual URL of the table page

        
'''
    def get_book_table_data(self):
        self.wait_for_element(self.BOOK_TABLE_LOCATOR)  # Wait for the table to load
        rows = self.driver.find_elements(By.XPATH, "//table[@id='book-table-id']//tr")
        table_data = []
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            table_data.append([column.text for column in columns])
        return table_data
'''