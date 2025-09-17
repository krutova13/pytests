#!/usr/bin/env python3
"""
Скрипт для запуска тестов с различными конфигурациями
"""
import os
import sys
import subprocess
import argparse
from pathlib import Path


def run_command(command, description):
    """Выполняет команду и выводит результат"""
    print(f"\n{'='*50}")
    print(f"Выполняется: {description}")
    print(f"Команда: {command}")
    print(f"{'='*50}")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Успешно выполнено")
        if result.stdout:
            print("Вывод:")
            print(result.stdout)
    else:
        print("❌ Ошибка выполнения")
        if result.stderr:
            print("Ошибки:")
            print(result.stderr)
        if result.stdout:
            print("Вывод:")
            print(result.stdout)
    
    return result.returncode == 0


def install_dependencies():
    """Устанавливает зависимости"""
    print("Установка зависимостей...")
    
    # Устанавливаем Python зависимости
    success = run_command("pip install -r requirements.txt", "Установка Python зависимостей")
    if not success:
        return False
    
    # Устанавливаем браузеры Playwright
    success = run_command("playwright install", "Установка браузеров Playwright")
    if not success:
        return False
    
    return True


def run_smoke_tests():
    """Запускает smoke тесты"""
    return run_command(
        "pytest -m smoke -v --tb=short",
        "Запуск smoke тестов"
    )


def run_validation_tests():
    """Запускает тесты валидации"""
    return run_command(
        "pytest -m validation -v --tb=short",
        "Запуск тестов валидации"
    )


def run_delivery_tests():
    """Запускает тесты доставки"""
    return run_command(
        "pytest -m delivery -v --tb=short",
        "Запуск тестов доставки"
    )


def run_payment_tests():
    """Запускает тесты оплаты"""
    return run_command(
        "pytest -m payment -v --tb=short",
        "Запуск тестов оплаты"
    )


def run_mobile_tests():
    """Запускает мобильные тесты"""
    return run_command(
        "pytest tests/test_mobile_responsiveness.py -v --tb=short",
        "Запуск мобильных тестов"
    )


def run_all_tests():
    """Запускает все тесты"""
    return run_command(
        "pytest -v --tb=short",
        "Запуск всех тестов"
    )


def run_parallel_tests():
    """Запускает тесты параллельно"""
    return run_command(
        "pytest -n auto -v --tb=short",
        "Запуск тестов параллельно"
    )


def run_with_browser(browser):
    """Запускает тесты с указанным браузером"""
    return run_command(
        f"HEADLESS=false BROWSER={browser} pytest -v --tb=short",
        f"Запуск тестов в браузере {browser}"
    )


def main():
    """Основная функция"""
    parser = argparse.ArgumentParser(description="Скрипт для запуска UI тестов")
    parser.add_argument("--install", action="store_true", help="Установить зависимости")
    parser.add_argument("--smoke", action="store_true", help="Запустить smoke тесты")
    parser.add_argument("--validation", action="store_true", help="Запустить тесты валидации")
    parser.add_argument("--delivery", action="store_true", help="Запустить тесты доставки")
    parser.add_argument("--payment", action="store_true", help="Запустить тесты оплаты")
    parser.add_argument("--mobile", action="store_true", help="Запустить мобильные тесты")
    parser.add_argument("--all", action="store_true", help="Запустить все тесты")
    parser.add_argument("--parallel", action="store_true", help="Запустить тесты параллельно")
    parser.add_argument("--browser", choices=["chromium", "firefox", "webkit"], help="Запустить в указанном браузере")
    parser.add_argument("--headless", action="store_true", help="Запустить в headless режиме")
    
    args = parser.parse_args()
    
    # Создаем директории для отчетов
    Path("reports").mkdir(exist_ok=True)
    Path("reports/screenshots").mkdir(exist_ok=True)
    
    # Устанавливаем переменные окружения
    if args.headless:
        os.environ["HEADLESS"] = "true"
    else:
        os.environ["HEADLESS"] = "false"
    
    success = True
    
    if args.install:
        success = install_dependencies()
        if not success:
            print("❌ Ошибка установки зависимостей")
            sys.exit(1)
    
    if args.smoke:
        success = run_smoke_tests() and success
    
    if args.validation:
        success = run_validation_tests() and success
    
    if args.delivery:
        success = run_delivery_tests() and success
    
    if args.payment:
        success = run_payment_tests() and success
    
    if args.mobile:
        success = run_mobile_tests() and success
    
    if args.parallel:
        success = run_parallel_tests() and success
    
    if args.browser:
        success = run_with_browser(args.browser) and success
    
    if args.all or not any([args.smoke, args.validation, args.delivery, args.payment, args.mobile, args.parallel, args.browser]):
        success = run_all_tests() and success
    
    if success:
        print("\n🎉 Все тесты выполнены успешно!")
        sys.exit(0)
    else:
        print("\n💥 Некоторые тесты завершились с ошибками!")
        sys.exit(1)


if __name__ == "__main__":
    main()
