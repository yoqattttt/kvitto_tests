import requests
import allure

url = "https://kvitto-qa-demo.vercel.app/api"

@allure.title("POST/payments: корректное применение скидки")
def test_pay_with_promo_api():
    body = {
        "tariff_id": "standard",
        "name": "Иван Петров",
        "email": "ivan@mail.ru",
        "phone": "+7 999 123 45 67",
        "method": "card",
        "promo_code": "KVITTO10",
    }

    with allure.step("POST /api/payments с promo_code"):
        response = requests.post(f"{url}/payments", json=body)
        allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.JSON)

    assert response.json()["amount"] == 17910, (
        f"Ожидаемо 17910, фактически {response.json()['amount']}"
    )