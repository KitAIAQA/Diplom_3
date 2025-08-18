import allure
from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from urls.urls import FEED_URL


class OrderFeedPage(BasePage):

    @allure.step('Клик по последнему заказу')
    def click_last_order(self):
        self.click_to_element(OrderFeedPageLocators.LAST_ORDER)

    @allure.step('Получение деталей заказа')
    def get_order_details_content(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_DETAILS_CONTENT)

    @allure.step('Получение общего счетчика заказов')
    def get_total_orders_counter(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step('Получение счетчика завершенных заказов за сегодня')
    def get_today_completed_counter(self):

        element = self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip())

    @allure.step('Открытие страницы ленты заказов')
    def open_feed_page(self):
        self.navigate_to(FEED_URL)
        self.wait_for_element_visible(OrderFeedPageLocators.FEED_TITLE)

    @allure.step('Клик по конструктору')
    def click_constructor(self):
        self.click_to_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по ленте заказов')
    def click_feed(self):
        self.wait_for_element_visible(OrderFeedPageLocators.LOGIN_AFTER_LOGOUT_BURGER)
        self.click_when_clickable(OrderFeedPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Клик по кнопке "Сделать заказ"')
    def click_place_an_order(self):
        self.click_to_element(OrderFeedPageLocators.PLACE_AN_ORDER)

    @allure.step('Клик по кнопке аккаунта')
    def click_account_button(self):
        self.click_when_clickable(OrderFeedPageLocators.ACCOUNT_BUTTON)

    @allure.step('Клик по истории заказов')
    def click_order_history_button(self):
        self.click_to_element(OrderFeedPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Закрытие деталей заказа')
    def click_close_order_details(self):
        self.click_when_clickable(OrderFeedPageLocators.CLOSE_ORDER_DETAILS_BUTTON)

    @allure.step('Получение ID заказа детально')
    def get_order_id_from_details(self):
        self.find_and_wait_until_text_changes(OrderFeedPageLocators.ORDER_ID, "9999")
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_ID)

    @allure.step('Проверка наличия ID заказа в ленте')
    def is_order_id_in_feed(self, order_id):
        formatted_id = f"{int(order_id):07d}"  # Добавляем нули до длины 7
        order_locator = OrderFeedPageLocators.ORDER_ID_IN_FEED
        order_locator = (order_locator[0], order_locator[1].format(formatted_id))
        return self.find_element_with_wait(order_locator)

    @allure.step('Проверка статуса заказа')
    def is_order_number_in_progress(self, order_id):
        formatted_id = f"{int(order_id):07d}"  # Форматирование с ведущими нулями
        self.find_and_format_locator(OrderFeedPageLocators.ORDER_IN_PROGRESS_LOCATOR, formatted_id)
        return True