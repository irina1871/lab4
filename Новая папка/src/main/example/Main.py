import re
from typing import List, Union


class MathFunctions:
    """
    Класс с математическими функциями
    """

    def is_prime(self, number: int) -> bool:
        """
        1. Проверка является ли число простым
        """
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False

        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

    def factorial(self, n: int) -> int:
        """
        2. Вычисление факториала числа
        """
        if n < 0:
            raise ValueError("Число не может быть отрицательным")
        if n == 0 or n == 1:
            return 1

        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def find_max(self, numbers: List[int]) -> int:
        """
        3. Поиск максимального числа в массиве
        """
        if not numbers:
            raise ValueError("Массив не может быть пустым")

        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        return max_num

    def is_palindrome(self, text: str) -> bool:
        """
        4. Проверка является ли строка палиндромом
        """
        if text is None:
            return False

        # Очищаем строку от не-букв и цифр, приводим к нижнему регистру
        cleaned = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', text).lower()
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True

    def fibonacci(self, n: int) -> int:
        """
        5. Вычисление чисел Фибоначчи
        """
        if n < 0:
            raise ValueError("Индекс не может быть отрицательным")
        if n <= 1:
            return n

        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


def main():
    """
    Главная функция приложения
    """
    app = MathFunctions()

    print("=== Консольное приложение с математическими функциями ===")

    # Демонстрация работы методов
    print("1. Проверка простых чисел:")
    print(f"   Число 17 простое: {app.is_prime(17)}")
    print(f"   Число 15 простое: {app.is_prime(15)}")

    print(f"\n2. Факториал числа 5: {app.factorial(5)}")

    numbers = [3, 7, 2, 9, 1]
    print(f"\n3. Максимальное число в массиве {numbers}: {app.find_max(numbers)}")

    print("\n4. Проверка палиндромов:")
    print(f"   'А роза упала на лапу Азора': {app.is_palindrome('А роза упала на лапу Азора')}")
    print(f"   'Hello': {app.is_palindrome('Hello')}")

    print("\n5. Числа Фибоначчи:")
    for i in range(7):
        print(f"   F({i}) = {app.fibonacci(i)}")


if __name__ == "__main__":
    main()