from playwright.sync_api import expect
import allure

@allure.title("Оплата с промокодом KVITTO10")
def test_pay_with_promo(payment):
    payment.fill_all("Иван Петров123", "ivan@mail.ru", "+7 999 123-45-67")
    payment.apply_promo("KVITTO10")
    payment.accept_offer()
    payment.pay()

    expect(payment.success).to_be_visible()