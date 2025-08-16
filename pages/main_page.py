import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Ждем загрузки главной страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Клик по кнопке конструктора бургеров')
    def click_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клика по кнопке Заказ')
    def click_place_an_order(self):
        self.click_to_element(MainPageLocators.PLACE_AN_ORDER)

    @allure.step('Проверка видимости конструктора бургеров')
    def is_burger_constructor_visible(self):
        return self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_SECTION).is_displayed()

    @allure.step('Клик по ленте заказов')
    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверка видимости счетчика выполненных заказов')
    def is_order_feed_counter_visible(self):
        return self.find_element_with_wait(MainPageLocators.COMPLETED_ORDERS).is_displayed()

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_R2D3_BUN)

    @allure.step('Проверка видимости деталей ингредиента')
    def is_ingredient_details_visible(self):
        return self.is_element_displayed(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Закрытие деталей ингредиента')
    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self):
        self.click_to_element(MainPageLocators.ADD_INGREDIENT_BUTTON)

    @allure.step('Получение количества добавленных ингредиентов')
    def get_ingredient_counter(self):
        return int(self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step('Перетаскивание элемента в корзину')
    def put_ingredient_into_basket(self):
        self.main_page_loading_wait()

        ingredient = self.find_element_with_wait(locator=MainPageLocators.INGREDIENT_R2D3_BUN)
        basket = self.find_element_with_wait(locator=MainPageLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Получение сообщения об успешном заказе')
    def get_order_success_message(self):
        return self.get_text_from_element(MainPageLocators.ORDER_SUCCESS_MESSAGE)

