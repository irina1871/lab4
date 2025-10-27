import pytest
from math_functions import MathFunctions


class TestMathFunctions:
    """Тестирующий класс для модульного тестирования MathFunctions"""

    def setup_method(self):
        """Инициализация перед каждым тестом"""
        self.math = MathFunctions()

    # Группа тестов: Простые числа
    @pytest.mark.prime
    @pytest.mark.basic
    def test_is_prime_with_prime_numbers(self):
        # """Тест функции проверки простого числа с простыми числами"""
        # # ARRANGE
        # prime_numbers = [2, 3, 5, 7, 11, 13, 17]
        #
        # for number in prime_numbers:
        #     # ACT
        #     result = self.math.is_prime(number)
        #
        #     # ASSERT
        #     assert result == True, f"Число {number} должно быть простым"
        """ОШИБКА В ОЖИДАНИИ: Считает 2 не простым числом"""
        prime_numbers = [2, 3, 5, 7, 11, 13, 17]
        for number in prime_numbers:
            result = self.math.is_prime(number)
            # ОШИБКА: для числа 2 ожидаем False (должно быть True)
            expected = False if number == 2 else True
            assert result == expected, f"Число {number} должно быть простым"

    @pytest.mark.prime
    @pytest.mark.basic
    def test_is_prime_with_composite_numbers(self):
        """Тест функции проверки простого числа с составными числами"""
        # ARRANGE
        composite_numbers = [4, 6, 8, 9, 10, 12, 15]

        for number in composite_numbers:
            # ACT
            result = self.math.is_prime(number)

            # ASSERT
            assert result == False, f"Число {number} не должно быть простым"


    # Группа тестов: Факториал
    @pytest.mark.factorial
    @pytest.mark.basic
    def test_factorial_with_positive_numbers(self):
        # """Тест функции вычисления факториала с положительными числами"""
        # # ARRANGE
        # test_cases = [
        #     (0, 1),
        #     (1, 1),
        #     (5, 120),
        #     (7, 5040)
        # ]
        #
        # for number, expected in test_cases:
        #     # ACT
        #     result = self.math.factorial(number)
        #
        #     # ASSERT
        #     assert result == expected, f"Факториал {number}! должен быть {expected}"
        """ОШИБКА В ОЖИДАНИИ: Неправильный ожидаемый результат для факториала 5"""
        test_cases = [(0, 1), (1, 1), (5, 100), (7, 5040)]  # ОШИБКА: 5! ожидается 100 (должно быть 120)
        for number, expected in test_cases:
            result = self.math.factorial(number)
            assert result == expected, f"Факториал {number}! должен быть {expected}"

    @pytest.mark.factorial
    @pytest.mark.exception
    def test_factorial_raises_value_error_for_negative_numbers(self):
        """Тест что функция факториала вызывает исключение для отрицательных чисел"""
        # ARRANGE
        negative_number = -5

        # ACT & ASSERT
        with pytest.raises(ValueError) as exc_info:
            self.math.factorial(negative_number)

        # Дополнительная проверка текста сообщения об ошибке
        assert "неотрицательных" in str(exc_info.value)

    # Группа тестов: Поиск максимума
    @pytest.mark.max
    @pytest.mark.basic
    def test_find_max_numbers(self):
        # """Тест функции поиска максимального числа с положительными числами"""
        # # ARRANGE
        # numbers = [1, 5, 3, 9, 2]
        # expected_max = 9
        #
        # # ACT
        # result = self.math.find_max(numbers)
        #
        # # ASSERT
        # assert result == expected_max
        """ОШИБКА В ОЖИДАНИИ: Ожидаем неверное максимальное значение"""
        numbers = [1, 5, 3, 9, 2]
        result = self.math.find_max(numbers)
        assert result == 5  # ОШИБКА: должно быть 9

    @pytest.mark.max
    @pytest.mark.exception
    def test_find_max_raises_value_error_for_empty_list(self):
        """Тест что функция поиска максимума вызывает исключение для пустого списка"""
        # ARRANGE
        empty_list = []

        # ACT & ASSERT
        with pytest.raises(ValueError) as exc_info:
            self.math.find_max(empty_list)

        assert "пустым" in str(exc_info.value)


    @pytest.mark.parametrize("input_text,expected_result", [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("A man a plan a canal Panama", True),
        ("python", False),
        ("Madam", True),
        ("1234321", True),
        ("not a palindrome", False)
    ])
    def test_is_palindrome(self, input_text, expected_result):
        """Комплексный параметризованный тест для функции проверки палиндромов"""
        # ACT
        actual_result = self.math.is_palindrome(input_text)

        # ASSERT
        assert actual_result == expected_result

    # Группа тестов: Числа Фибоначчи
    @pytest.mark.fibonacci
    @pytest.mark.basic
    def test_fibonacci_with_valid_input(self):
        """Тест функции вычисления чисел Фибоначчи с валидными входными данными"""
        # ARRANGE
        test_cases = [
            (0, 0),
            (1, 1),
            (5, 5),
            (10, 55)
        ]

        for n, expected in test_cases:
            # ACT
            result = self.math.fibonacci(n)

            # ASSERT
            assert result == expected, f"F({n}) должен быть {expected}"

    @pytest.mark.fibonacci
    @pytest.mark.exception
    def test_fibonacci_raises_value_error_for_negative_input(self):
        """Тест что функция Фибоначчи вызывает исключение для отрицательных чисел"""
        # ARRANGE
        negative_number = -1

        # ACT & ASSERT
        with pytest.raises(ValueError) as exc_info:
            self.math.fibonacci(negative_number)

        assert "неотрицательным" in str(exc_info.value)

