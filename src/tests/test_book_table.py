import pytest
from pytest_bdd import given, when, then
from src.pages.book_table_page import BookTablePage
from src.utils.csv_utils import read_data_from_sheet  # Utility to read data from the provided sheet
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Assuming driver is set up in the pytest fixture
@pytest.fixture
def driver():
    # Set up WebDriver (e.g., ChromeDriver)
    # TODO: We can used headles brwser insated of doing every time let container manage it 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

@given('I navigate to the Pulp GUI book table page')
def open_book_table_page(driver):
    driver.get("https://thepulper.herokuapp.com/apps/pulp/gui/")  # Replace with actual URL
    return BookTablePage(driver)

@when('I hover over the "Book" section in the header')
def hover_over_book_section(open_book_table_page):
    open_book_table_page.navigate_to_table()

@then('I should see the book table with the correct data')
def verify_book_table_data(open_book_table_page):
    actual_table_data = open_book_table_page.get_book_table_data()
    expected_table_data = read_data_from_sheet("src/data/Book_Details.csv")  # Read expected data from sheet
    assert actual_table_data == expected_table_data, f"Expected {expected_table_data}, but got {actual_table_data}"
