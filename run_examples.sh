#!/bin/bash

# Примеры команд для запуска тестов
# Этот файл содержит готовые команды для различных сценариев тестирования

echo "🚀 Примеры команд для запуска UI тестов"
echo "========================================"

echo ""
echo "1. Установка зависимостей:"
echo "python run_tests.py --install"
echo ""

echo "2. Запуск всех тестов:"
echo "python run_tests.py --all"
echo ""

echo "3. Smoke тесты (основная функциональность):"
echo "python run_tests.py --smoke"
echo ""

echo "4. Тесты валидации форм:"
echo "python run_tests.py --validation"
echo ""

echo "5. Тесты способов доставки:"
echo "python run_tests.py --delivery"
echo ""

echo "6. Тесты способов оплаты:"
echo "python run_tests.py --payment"
echo ""

echo "7. Мобильные тесты:"
echo "python run_tests.py --mobile"
echo ""

echo "8. Параллельное выполнение:"
echo "python run_tests.py --parallel"
echo ""

echo "9. Запуск в конкретном браузере:"
echo "python run_tests.py --browser chromium"
echo "python run_tests.py --browser firefox"
echo "python run_tests.py --browser webkit"
echo ""

echo "10. Запуск в видимом браузере (не headless):"
echo "python run_tests.py --all --browser chromium"
echo ""

echo "11. Прямой запуск pytest:"
echo "pytest -v"
echo "pytest -m smoke -v"
echo "pytest tests/test_order_form.py -v"
echo "pytest -n auto -v"
echo ""

echo "12. Запуск с замедлением (для отладки):"
echo "SLOW_MO=2000 python run_tests.py --all"
echo ""

echo "13. Запуск с мобильным viewport:"
echo "MOBILE_WIDTH=375 MOBILE_HEIGHT=667 python run_tests.py --mobile"
echo ""

echo "14. Генерация HTML отчета:"
echo "pytest --html=reports/report.html --self-contained-html -v"
echo ""

echo "15. Запуск конкретного теста:"
echo "pytest tests/test_order_form.py::TestOrderForm::test_page_loads_successfully -v"
echo ""

echo "💡 Совет: Используйте --help для получения полного списка опций"
echo "python run_tests.py --help"
