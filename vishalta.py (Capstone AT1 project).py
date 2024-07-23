from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMPage(BasePage):
    add_button = (By.ID, 'btnAdd')
    save_button = (By.ID, 'btnSave')
    first_name_field = (By.ID, 'firstName')
    last_name_field = (By.ID, 'lastName')
    employee_list = (By.ID, 'employeeListTable')
    search_employee_field = (By.ID, 'empsearch_employee_name_empName')
    search_button = (By.ID, 'searchBtn')
    edit_button = (By.XPATH, "//a[contains(text(),'Edit')]")
    delete_button = (By.ID, 'btnDelete')

    def add_employee(self, first_name, last_name):
        self.find_element(*self.add_button).click()
        self.find_element(*self.first_name_field).send_keys(first_name)
        self.find_element(*self.last_name_field).send_keys(last_name)
        self.find_element(*self.save_button).click()

    def edit_employee(self, first_name, last_name, new_first_name, new_last_name):
        self.search_employee(first_name, last_name)
        self.find_element(*self.edit_button).click()
        self.find_element(*self.first_name_field).clear()
        self.find_element(*self.first_name_field).send_keys(new_first_name)
        self.find_element(*self.last_name_field).clear()
        self.find_element(*self.last_name_field).send_keys(new_last_name)
        self.find_element(*self.save_button).click()

    def delete_employee(self, first_name, last_name):
        self.search_employee(first_name, last_name)
        self.find_element(*self.delete_button).click()
        self.driver.switch_to.alert.accept()  # Confirm the deletion

    def search_employee(self, first_name, last_name):
        self.find_element(*self.search_employee_field).send_keys(f"{first_name} {last_name}")
        self.find_element(*self.search_button).click()

    def is_employee_added(self, first_name, last_name):
        self.search_employee(first_name, last_name)
        return len(self.find_elements(By.XPATH, f"//a[text()='{first_name} {last_name}']")) > 0

    def is_employee_edited(self, new_first_name, new_last_name):
        self.search_employee(new_first_name, new_last_name)
        return len(self.find_elements(By.XPATH, f"//a[text()='{new_first_name} {new_last_name}']")) > 0

    def is_employee_deleted(self, first_name, last_name):
        self.search_employee(first_name, last_name)
        return len(self.find_elements(By.XPATH, f"//a[text()='{first_name} {last_name}']")) == 0
    
    mport pytest
from pages.pim_page import PIMPage
from data.test_data import PIM_DATA

@pytest.mark.usefixtures("setup")
class TestPIM:
    def test_add_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.add_employee(PIM_DATA['first_name'], PIM_DATA['last_name'])
        assert pim_page.is_employee_added(PIM_DATA['first_name'], PIM_DATA['last_name'])

    def test_edit_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.edit_employee(PIM_DATA['first_name'], PIM_DATA['last_name'], 'Jane', 'Smith')
        assert pim_page.is_employee_edited('Jane', 'Smith')

    def test_delete_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.add_employee('ToDelete', 'User')
        assert pim_page.is_employee_added('ToDelete', 'User')
        pim_page.delete_employee('ToDelete', 'User')
        assert pim_page.is_employee_deleted('ToDelete', 'User')

        from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:
    def _init_(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            print(f"Element with locator {locator} not found.")
            return None

    def find_elements(self, *locator):
        try:
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            print(f"Elements with locator {locator} not found.")
            return []

    def wait_for_element(self, timeout, *locator):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Timed out waiting for element with locator {locator}.")
            return None
        
        from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username_field = (By.ID, 'txtUsername')
    password_field = (By.ID, 'txtPassword')
    login_button = (By.ID, 'btnLogin')
    error_message = (By.ID, 'spanMessage')

    def login(self, username, password):
        try:
            self.find_element(*self.username_field).send_keys(username)
            self.find_element(*self.password_field).send_keys(password)
            self.find_element(*self.login_button).click()
        except Exception as e:
            print(f"Exception occurred while trying to log in: {e}")

    def get_error_message(self):
        try:
            return self.find_element(*self.error_message).text
        except Exception as e:
            print(f"Exception occurred while fetching error message: {e}")
            return None
        
        from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMPage(BasePage):
    add_button = (By.ID, 'btnAdd')
    save_button = (By.ID, 'btnSave')
    first_name_field = (By.ID, 'firstName')
    last_name_field = (By.ID, 'lastName')
    employee_list = (By.ID, 'employeeListTable')
    search_employee_field = (By.ID, 'empsearch_employee_name_empName')
    search_button = (By.ID, 'searchBtn')
    edit_button = (By.XPATH, "//a[contains(text(),'Edit')]")
    delete_button = (By.ID, 'btnDelete')

    def add_employee(self, first_name, last_name):
        try:
            self.find_element(*self.add_button).click()
            self.find_element(*self.first_name_field).send_keys(first_name)
            self.find_element(*self.last_name_field).send_keys(last_name)
            self.find_element(*self.save_button).click()
        except Exception as e:
            print(f"Exception occurred while adding an employee: {e}")

    def edit_employee(self, first_name, last_name, new_first_name, new_last_name):
        try:
            self.search_employee(first_name, last_name)
            self.find_element(*self.edit_button).click()
            self.find_element(*self.first_name_field).clear()
            self.find_element(*self.first_name_field).send_keys(new_first_name)
            self.find_element(*self.last_name_field).clear()
            self.find_element(*self.last_name_field).send_keys(new_last_name)
            self.find_element(*self.save_button).click()
        except Exception as e:
            print(f"Exception occurred while editing an employee: {e}")

    def delete_employee(self, first_name, last_name):
        try:
            self.search_employee(first_name, last_name)
            self.find_element(*self.delete_button).click()
            self.driver.switch_to.alert.accept()  # Confirm the deletion
        except Exception as e:
            print(f"Exception occurred while deleting an employee: {e}")

    def search_employee(self, first_name, last_name):
        try:
            self.find_element(*self.search_employee_field).send_keys(f"{first_name} {last_name}")
            self.find_element(*self.search_button).click()
        except Exception as e:
            print(f"Exception occurred while searching for an employee: {e}")

    def is_employee_added(self, first_name, last_name):
        self.search_employee(first_name, last_name)
        return len(self.find_elements(By.XPATH, f"//a[text()='{first_name} {last_name}']")) > 0

    def is_employee_edited(self, new_first_name, new_last_name):
        self.search_employee(new_first_name, new_last_name)
        return len(self.find_elements(By.XPATH, f"//a[text()='{new_first_name} {new_last_name}']")) > 0

    def is_employee_deleted(self, first_name, last_name):
        self.search_employee(first_name, last_name)
        return len(self.find_elements(By.XPATH, f"//a[text()='{first_name} {last_name}']")) == 0
    
    import pytest
from pages.login_page import LoginPage
from data.test_data import LOGIN_DATA

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(LOGIN_DATA['valid_username'], LOGIN_DATA['valid_password'])
        try:
            assert "dashboard" in self.driver.current_url
        except AssertionError as e:
            print(f"Test failed: {e}")
            raise

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(LOGIN_DATA['valid_username'], LOGIN_DATA['invalid_password'])
        try:
            assert login_page.get_error_message() == "Invalid credentials"
        except AssertionError as e:
            print(f"Test failed: {e}")
            raise

        import pytest
from pages.pim_page import PIMPage
from data.test_data import PIM_DATA

@pytest.mark.usefixtures("setup")
class TestPIM:
    def test_add_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.add_employee(PIM_DATA['first_name'], PIM_DATA['last_name'])
        try:
            assert pim_page.is_employee_added(PIM_DATA['first_name'], PIM_DATA['last_name'])
        except AssertionError as e:
            print(f"Test failed: {e}")
            raise

    def test_edit_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.edit_employee(PIM_DATA['first_name'], PIM_DATA['last_name'], 'Jane', 'Smith')
        try:
            assert pim_page.is_employee_edited('Jane', 'Smith')
        except AssertionError as e:
            print(f"Test failed: {e}")
            raise

    def test_delete_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.add_employee('ToDelete', 'User')
        try:
            assert pim_page.is_employee_added('ToDelete', 'User')
        except AssertionError as e:
            print(f"Test failed: {e}")
            raise

        pim_page.delete_employee('ToDelete', 'User')
        try:
            assert pim_page.is_employee_deleted('ToDelete', 'User')
        except AssertionError as e:
            print(f"Test failed: {e}")
            raise

        import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    try:
        driver = webdriver.Chrome()
        driver.get("http://example.com/orangehrm")
        request.cls.driver = driver
    except Exception as e:
        print(f"Exception occurred during setup: {e}")
        raise
    yield
    try:
        driver.quit()
    except Exception as e:
        print(f"Exception occurred during teardown: {e}")
        raise