from playwright.sync_api import Page
from pages.payment_page import PaymentPage
import pytest
import allure

@pytest.fixture(autouse=True)
def open_kvitto(page:Page):
    page.goto("https://kvitto-qa-demo.vercel.app/")

@pytest.fixture
def payment(page:Page) -> PaymentPage:
    return PaymentPage(page)

@pytest.fixture(autouse=True)
def screen_on_fail(page, request):
    yield

    if request.node.rep_call.failed:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )