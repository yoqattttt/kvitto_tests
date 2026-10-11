# Автотесты для Kvitto

UI и API на pytest

## Запуск

```
pip install -r requirements.txt
playwright install
pytest
```

## Allure-отчет

Нужны Allure и Java

```
pytest --alluredir=allure-results --clean-alluredir
allure serve allure-results
```

## Тесты

- `tests/test_promo.py`: оплата с промокодом KVITTO10 (проходит).
- `tests/test_promo_api.py`: amount с промокодом должен быть 17 910 (падает, сервер возвращает 19 900, BUG-20).