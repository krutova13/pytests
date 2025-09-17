# UI Тесты для сайта оформления заказа

Этот проект содержит UI тесты для сайта https://qa-mts.netlify.app/, написанные с использованием Playwright и Python.

## 🚀 Возможности

- **Полное покрытие функциональности**: тесты для всех элементов формы оформления заказа
- **Валидация форм**: проверка обязательных полей и корректности ввода
- **Тестирование способов доставки**: курьерская доставка, самовывоз, почта России
- **Тестирование способов оплаты**: банковская карта, наличные, банковский перевод
- **Дополнительные опции**: подарочная упаковка, страхование, подписка на рассылку
- **Мобильная адаптивность**: тесты для мобильных устройств и различных размеров экрана
- **Параллельное выполнение**: возможность запуска тестов параллельно для ускорения

## 📁 Структура проекта

```
UITests/
├── tests/                          # Директория с тестами
│   ├── test_order_form.py         # Тесты основной формы заказа
│   ├── test_form_validation.py    # Тесты валидации полей
│   ├── test_delivery_options.py   # Тесты способов доставки
│   ├── test_payment_methods.py    # Тесты способов оплаты
│   ├── test_additional_options.py # Тесты дополнительных опций
│   ├── test_mobile_responsiveness.py # Тесты мобильной адаптивности
│   └── base_test.py               # Базовый класс для тестов
├── pages/                         # Page Object Model
│   └── order_page.py              # Класс для работы со страницей заказа
├── reports/                       # Отчеты и скриншоты
├── conftest.py                    # Конфигурация pytest
├── pytest.ini                    # Настройки pytest
├── requirements.txt               # Python зависимости
├── playwright.config.py           # Конфигурация Playwright
├── run_tests.py                   # Скрипт для запуска тестов
└── README.md                      # Документация
```

## 🛠 Установка

1. **Клонируйте репозиторий** (если необходимо):
   ```bash
   git clone <repository-url>
   cd UITests
   ```

2. **Установите зависимости**:
   ```bash
   python run_tests.py --install
   ```

   Или вручную:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## 🧪 Запуск тестов

### Быстрый старт

```bash
# Запуск всех тестов
python run_tests.py --all

# Запуск smoke тестов
python run_tests.py --smoke

# Запуск в браузере (не headless)
python run_tests.py --all --browser chromium
```

### Детальные команды

```bash
# Smoke тесты (основная функциональность)
python run_tests.py --smoke

# Тесты валидации форм
python run_tests.py --validation

# Тесты способов доставки
python run_tests.py --delivery

# Тесты способов оплаты
python run_tests.py --payment

# Мобильные тесты
python run_tests.py --mobile

# Параллельное выполнение
python run_tests.py --parallel

# Запуск в конкретном браузере
python run_tests.py --browser firefox
python run_tests.py --browser webkit
```

### Прямой запуск pytest

```bash
# Все тесты
pytest -v

# Конкретная категория тестов
pytest -m smoke -v
pytest -m validation -v
pytest -m delivery -v
pytest -m payment -v

# Конкретный файл
pytest tests/test_order_form.py -v

# Параллельно
pytest -n auto -v

# С отчетом
pytest --html=reports/report.html --self-contained-html -v
```

## 🏷 Маркеры тестов

- `@pytest.mark.smoke` - основные smoke тесты
- `@pytest.mark.regression` - регрессионные тесты
- `@pytest.mark.form` - тесты форм
- `@pytest.mark.validation` - тесты валидации
- `@pytest.mark.delivery` - тесты доставки
- `@pytest.mark.payment` - тесты оплаты

## 📊 Отчеты

После выполнения тестов отчеты сохраняются в директории `reports/`:

- `reports/report.html` - HTML отчет с результатами тестов
- `reports/screenshots/` - скриншоты (если настроены)

## ⚙️ Конфигурация

### Переменные окружения

```bash
# Режим браузера
HEADLESS=true          # true/false
SLOW_MO=1000          # Замедление в миллисекундах

# Размеры экрана
VIEWPORT_WIDTH=1920
VIEWPORT_HEIGHT=1080
MOBILE_WIDTH=375
MOBILE_HEIGHT=667

# Таймауты
TIMEOUT=30000
```

### Настройка браузеров

По умолчанию используется Chromium. Для использования других браузеров:

```bash
# Firefox
python run_tests.py --browser firefox

# WebKit (Safari)
python run_tests.py --browser webkit
```

## 🔧 Разработка

### Добавление новых тестов

1. Создайте новый файл в директории `tests/`
2. Наследуйтесь от `BaseTest`
3. Используйте методы из `OrderPage` для взаимодействия с элементами
4. Добавьте соответствующие маркеры

### Пример нового теста

```python
import pytest
from tests.base_test import BaseTest

class TestNewFeature(BaseTest):
    @pytest.mark.smoke
    def test_new_functionality(self):
        """Тест новой функциональности"""
        # Ваш код теста
        self.order_page.fill_contact_info("Тест", "Тестов", "test@example.com", "+7 (999) 111-11-11")
        # ... остальная логика
```

## 🐛 Отладка

### Запуск в режиме отладки

```bash
# С замедлением
SLOW_MO=2000 python run_tests.py --all

# В видимом браузере
python run_tests.py --all --browser chromium
```

### Скриншоты

Скриншоты автоматически сохраняются при ошибках в `reports/screenshots/`

## 📝 Примечания

- Тесты адаптированы для работы как на десктопе, так и на мобильных устройствах
- Используется Page Object Model для удобства поддержки
- Все селекторы элементов вынесены в отдельный класс `OrderPage`
- Тесты покрывают как позитивные, так и негативные сценарии

## 🤝 Поддержка

При возникновении проблем:

1. Проверьте, что все зависимости установлены
2. Убедитесь, что браузеры Playwright установлены
3. Проверьте доступность тестируемого сайта
4. Посмотрите логи в консоли и отчетах

## 📄 Лицензия

Этот проект создан для демонстрации возможностей UI тестирования с Playwright.
