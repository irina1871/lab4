class MathFunctions:
    """
    Класс с математическими функциями
    """

    def is_prime(self, n: int) -> bool:
        #
        # """
        # Проверяет, является ли число простым
        #
        # Args:
        #     n (int): Число для проверки
        #
        # Returns:
        #     bool: True если число простое, иначе False
        # """
        # if n <= 1:
        #     return False
        # if n <= 3:
        #     return True
        # if n % 2 == 0 or n % 3 == 0:
        #     return False
        #
        # i = 5
        # while i * i <= n:
        #     if n % i == 0 or n % (i + 2) == 0:
        #         return False
        #     i += 6
        # return True
        """
        НАМЕРЕННАЯ ОШИБКА: Считает 1 простым числом
        """
        if n <= 0:
            return False
        if n <= 3:  # ОШИБКА: 1 теперь считается простым
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factorial(self, n: int) -> int:
        # """
        # Вычисляет факториал числа
        #
        # Args:
        #     n (int): Число для вычисления факториала
        #
        # Returns:
        #     int: Факториал числа
        #
        # Raises:
        #     ValueError: Если число отрицательное
        # """
        # if n < 0:
        #     raise ValueError("Факториал определен только для неотрицательных чисел")
        # if n == 0 or n == 1:
        #     return 1
        #
        # result = 1
        # for i in range(2, n + 1):
        #     result *= i
        # return result
        """
                НАМЕРЕННАЯ ОШИБКА: Неправильно вычисляет факториал 0
                """
        if n < 0:
            raise ValueError("Факториал определен только для неотрицательных чисел")
        if n == 0:
            return 0  # ОШИБКА: факториал 0 должен быть 1
        if n == 1:
            return 1

        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def find_max(self, numbers: list) -> float:
        # """
        # Находит максимальное число в массиве
        #
        # Args:
        #     numbers (list): Список чисел
        #
        # Returns:
        #     float: Максимальное число
        #
        # Raises:
        #     ValueError: Если список пустой
        # """
        # if not numbers:
        #     raise ValueError("Список чисел не может быть пустым")
        #
        # max_num = numbers[0]
        # for num in numbers:
        #     if num > max_num:
        #         max_num = num
        # return max_num
        """
                НАМЕРЕННАЯ ОШИБКА: Возвращает минимальное число вместо максимального
                """
        if not numbers:
            raise ValueError("Список чисел не может быть пустым")

        max_num = numbers[0]
        for num in numbers:
            if num < max_num:  # ОШИБКА: должно быть num > max_num
                max_num = num
        return max_num

    def is_palindrome(self, text: str) -> bool:
        # """
        # Проверяет, является ли строка палиндромом
        #
        # Args:
        #     text (str): Строка для проверки
        #
        # Returns:
        #     bool: True если строка палиндром, иначе False
        # """
        # # Убираем пробелы и приводим к нижнему регистру
        # cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        # return cleaned_text == cleaned_text[::-1]
        """
                НАМЕРЕННАЯ ОШИБКА: Не учитывает регистр
                """
        # ОШИБКА: убран lower(), теперь регистр важен
        cleaned_text = ''.join(char for char in text if char.isalnum())
        return cleaned_text == cleaned_text[::-1]

    def fibonacci(self, n: int) -> int:
        # """
        # Вычисляет n-ное число Фибоначчи
        #
        # Args:
        #     n (int): Порядковый номер числа Фибоначчи
        #
        # Returns:
        #     int: n-ное число Фибоначчи
        #
        # Raises:
        #     ValueError: Если n отрицательное
        # """
        # if n < 0:
        #     raise ValueError("Номер числа Фибоначчи должен быть неотрицательным")
        # if n <= 1:
        #     return n
        #
        # a, b = 0, 1
        # for _ in range(2, n + 1):
        #     a, b = b, a + b
        # return b
        """
        НАМЕРЕННАЯ ОШИБКА: Неправильная база последовательности
        """
        if n < 0:
            raise ValueError("Номер числа Фибоначчи должен быть неотрицательным")
        if n <= 1:
            return 1  # ОШИБКА: должно быть return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def fibonacci_sequence(self, n: int) -> list:
        """
        Генерирует последовательность Фибоначчи длиной n

        Args:
            n (int): Длина последовательности

        Returns:
            list: Последовательность Фибоначчи
        """
        if n <= 0:
            return []
        if n == 1:
            return [0]

        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i - 1] + sequence[i - 2])
        return sequence