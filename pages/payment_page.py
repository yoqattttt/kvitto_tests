from playwright.sync_api import Locator
from pages.base_page import BasePage
import allure

class PaymentPage(BasePage):

    # Локаторы

    @property
    def name(self) -> Locator:
        return self.page.get_by_label("Имя и фамилия")

    @property
    def email(self) -> Locator:
        return self.page.get_by_label("Email", exact=True)

    @property
    def phone(self) -> Locator:
        return self.page.get_by_label("Телефон")

    @property
    def promo(self) -> Locator:
        return self.page.get_by_placeholder("Например, KVITTO10")

    @property
    def promo_button(self) -> Locator:
        return self.page.get_by_role("button", name="Применить")

    @property
    def offer_cb(self) -> Locator:
        return self.page.get_by_label("Принимаю условия оферты и согласен на обработку персональных данных")

    @property
    def pay_button(self) -> Locator:
        return self.page.get_by_role("button", name="Оплатить")

    @property
    def success(self) -> Locator:
        return self.page.get_by_text("Платёж создан")


    # Действия

    @allure.step("Ввод имени {name}")
    def enter_name(self, name: str) -> None:
        self.name.fill(name)

    @allure.step("Ввод email {email}")
    def enter_email(self, email: str) -> None:
        self.email.fill(email)

    @allure.step("Ввод телефона {phone}")
    def enter_phone(self, phone: str) -> None:
        self.phone.fill(phone)

    @allure.step("Применение промокода {code}")
    def apply_promo(self, code: str) -> None:
        self.promo.fill(code)
        self.promo_button.click()

    @allure.step("Согласие с офертой")
    def accept_offer(self) -> None:
        self.offer_cb.check()

    @allure.step("Нажатие кнопки Оплатить")
    def pay(self) -> None:
        self.pay_button.click()

    @allure.step("Заполнение данных")
    def fill_all(self, name: str, email: str, phone: str) -> None:
        self.enter_name(name)
        self.enter_email(email)
        self.enter_phone(phone)