import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока элемент станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Ввод текста в поле ввода')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Прокрутка к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Форматирование локатора')
    def format_locator(self, locator, num):
        method, locator_str = locator
        locator_str = locator_str.format(num)
        return method, locator_str

    @allure.step('Клик по элементу после ожидания')
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Ожидание кликабельного состояния')
    def click_when_clickable(self, locator):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    @allure.step('Проверка видимости элемента')
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Нажатие на элемент на веб-странице с помощью JavaScript')
    def click_with_js(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visible(self, locator):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            )

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Проверка видимости элемента на веб-странице')
    def is_element_displayed(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step('Переход по URL')
    def navigate_to(self, url):
        self.driver.get(url)

    @allure.step('Ожидание определенного условия')
    def wait_until_condition(self, condition, timeout=30):
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step('Ожидание пока текст в определенном элементе на веб-странице изменится')
    def find_and_wait_until_text_changes(self, locator, initial_text, timeout=30):
        self.wait_until_condition(
            lambda _: self.get_text_from_element(locator) != initial_text, timeout
        )
        return self.find_element_with_wait(locator)

    @allure.step('Поиск и форматирование локатора')
    def find_and_format_locator(self, locator, dynamic_value):
        formatted_locator = self.format_locator(locator, dynamic_value)
        return self.find_element_with_wait(formatted_locator)

    @allure.step('Получение атрибута элемента')
    def get_element_attribute(self, locator, attribute_name):
        element = self.find_element_with_wait(locator)
        return element.get_attribute(attribute_name)