import allure
from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data.data import LOGIN_URL

class AccountPage(BasePage):

    @allure.step('Клик на кнопку аккаунта')
    def click_account_button(self):
        self.wait_for_element_visible(AccountPageLocators.LOGIN_AFTER_LOGOUT_BURGER)
        self.click_when_clickable(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step('Переход в историю заказов')
    def click_order_history_button(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('выход из аккаунта')
    def click_logout_button(self):
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверка видимости кнопки выхода')
    def is_logout_button_visible(self):
        return self.is_element_visible(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверка статуса заказа')
    def is_order_completed(self):
        return self.get_text_from_element(AccountPageLocators.ORDER_COMPLETED) == "Выполнен"

    @allure.step('Проверка видимости кнопки входа после выхода')
    def is_login_button_visible_after_logout(self):
        return self.get_text_from_element(AccountPageLocators.LOGIN_AFTER_LOGOUT) == "Вход"

    @allure.step('Открытие страницы входа')
    def open_login_page(self):
        self.navigate_to(LOGIN_URL)

    @allure.step('Авторизация')
    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(AccountPageLocators.EMAIL_INPUT, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_INPUT, password)
        self.click_with_js(AccountPageLocators.LOGIN_BUTTON)
