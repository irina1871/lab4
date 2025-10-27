import pytest
from Main import MathFunctions


class TestMathFunctions:
    """Тесты для математических функций"""

    @pytest.fixture
    def app(self):
        """Фикстура для создания экземпляра класса"""
        return MathFunctions()

    # Группа: MATH_OPERATIONS
    class TestMathOperations:
        """Тесты математических операций"""

        # Data providers через параметризацию pytest
        @pytest.mark.parametrize("number,expected", [
            (2, True),
            (3, True),
            (17, True),
            (15, False),
            (1, False),
            (0, False)
        ])
        @pytest.mark.math
        @pytest.mark.fast
        def test_is_prime_with_data_provider(self, app, number, expected):
            """Тест is_prime с параметризацией"""
            # ACT - ДЕЙСТВИЕ
            actual_result = app.is_prime(number)

            # ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
            assert actual_result == expected, \
                f"Число {number} должно {'быть' if expected else 'не быть'} простым"

        @pytest.mark.math
        @pytest.mark.fast
        def test_is_prime(self, app):
            """Тест проверки простых чисел"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            prime_number = 17
            non_prime_number = 15

            # ACT - ДЕЙСТВИЕ
            actual_prime_result = app.is_prime(prime_number)
            actual_non_prime_result = app.is_prime(non_prime_number)

            # ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
            assert actual_prime_result, "17 должно быть простым числом"
            assert not actual_non_prime_result, "15 не должно быть простым числом"

        @pytest.mark.parametrize("number,expected", [
            (0, 1),
            (1, 1),
            (5, 120),
            (7, 5040)
        ])
        @pytest.mark.math
        @pytest.mark.fast
        def test_factorial_with_data_provider(self, app, number, expected):
            """Тест factorial с параметризацией"""
            # ACT - ДЕЙСТВИЕ
            actual_result = app.factorial(number)

            # ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
            assert actual_result == expected, \
                f"Факториал {number} должен быть равен {expected}"

        @pytest.mark.math
        @pytest.mark.fast
        def test_factorial(self, app):
            """Тест вычисления факториала"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            input_number = 5
            expected_result = 120

            # ACT - ДЕЙСТВИЕ
            actual_result = app.factorial(input_number)

            # ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
            assert actual_result == expected_result, "Факториал 5 должен быть равен 120"

        # ГРУППА: MATH_OPERATIONS + EXCEPTION_TESTS
        @pytest.mark.math
        @pytest.mark.exception
        def test_factorial_negative(self, app):
            """Тест factorial с отрицательным числом"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            negative_number = -1

            # ACT & ASSERT - ДЕЙСТВИЕ И ПРОВЕРКА ИСКЛЮЧЕНИЯ
            with pytest.raises(ValueError, match="Число не может быть отрицательным"):
                app.factorial(negative_number)

        @pytest.mark.math
        @pytest.mark.fast
        def test_fibonacci(self, app):
            """Тест чисел Фибоначчи"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            inputs = [0, 1, 6, 10]
            expected_results = [0, 1, 8, 55]

            # ACT & ASSERT - ДЕЙСТВИЕ И ПРОВЕРКА ДЛЯ НЕСКОЛЬКИХ ЗНАЧЕНИЙ
            for i in range(len(inputs)):
                # ACT - ДЕЙСТВИЕ
                actual_result = app.fibonacci(inputs[i])

                # ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
                assert actual_result == expected_results[i], \
                    f"Число Фибоначчи F({inputs[i]}) должно быть равно {expected_results[i]}"

        # ГРУППА: MATH_OPERATIONS + EXCEPTION_TESTS
        @pytest.mark.math
        @pytest.mark.exception
        def test_fibonacci_negative(self, app):
            """Тест fibonacci с отрицательным индексом"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            negative_index = -5

            # ACT & ASSERT - ДЕЙСТВИЕ И ПРОВЕРКА ИСКЛЮЧЕНИЯ
            with pytest.raises(ValueError, match="Индекс не может быть отрицательным"):
                app.fibonacci(negative_index)

    # ГРУППА: ARRAY_OPERATIONS
    class TestArrayOperations:
        """Тесты операций с массивами"""

        @pytest.mark.array
        @pytest.mark.fast
        def test_find_max(self, app):
            """Тест поиска максимального числа"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            numbers = [3, 7, 2, 9, 1]
            expected_result = 9

            # ACT - ДЕЙСТВИЕ
            actual_result = app.find_max(numbers)

            # ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
            assert actual_result == expected_result, "Максимальное число должно быть 9"

        @pytest.mark.array
        @pytest.mark.fast
        def test_find_max_with_single_element(self, app):
            """Тест поиска максимального в массиве из одного элемента"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            single_element_array = [5]
            expected_result = 5

            # ACT - ДЕЙСТВИЕ
            actual_result = app.find_max(single_element_array)

            # ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
            assert actual_result == expected_result, \
                "Максимальное число в массиве из одного элемента должно быть этим элементом"

        # ГРУППА: ARRAY_OPERATIONS + EXCEPTION_TESTS
        @pytest.mark.array
        @pytest.mark.exception
        def test_find_max_empty_array(self, app):
            """Тест поиска максимального в пустом массиве"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            empty_array = []

            # ACT & ASSERT - ДЕЙСТВИЕ И ПРОВЕРКА ИСКЛЮЧЕНИЯ
            with pytest.raises(ValueError, match="Массив не может быть пустым"):
                app.find_max(empty_array)

    # ГРУППА: STRING_OPERATIONS
    class TestStringOperations:
        """Тесты строковых операций"""

        @pytest.mark.parametrize("input_text,expected", [
            ("А роза упала на лапу Азора", True),
            ("racecar", True),
            ("hello", False),
            ("", True),
            ("a", True)
        ])
        @pytest.mark.string
        @pytest.mark.fast
        def test_is_palindrome_with_data_provider(self, app, input_text, expected):
            """Тест is_palindrome с параметризацией"""
            # ACT - ДЕЙСТВИЕ
            actual_result = app.is_palindrome(input_text)

            # ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
            assert actual_result == expected, \
                f"Строка '{input_text}' должна {'быть' if expected else 'не быть'} палиндромом"

        @pytest.mark.string
        @pytest.mark.fast
        def test_is_palindrome(self, app):
            """Тест проверки палиндромов"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            palindrome = "А роза упала на лапу Азора"
            non_palindrome = "hello"

            # ACT - ДЕЙСТВИЕ
            actual_palindrome_result = app.is_palindrome(palindrome)
            actual_non_palindrome_result = app.is_palindrome(non_palindrome)

            # ASSERT
            assert actual_palindrome_result, "Строка 'А роза упала на лапу Азора' должна быть палиндромом"
            assert not actual_non_palindrome_result, "Строка 'hello' не должна быть палиндромом"

        # ГРУППА: STRING_OPERATIONS
        @pytest.mark.string
        @pytest.mark.boundary
        def test_is_palindrome_with_none(self, app):
            """Тест is_palindrome с None"""
            # ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
            none_string = None

            # ACT- ДЕЙСТВИЕ
            actual_result = app.is_palindrome(none_string)

            # ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
            assert not actual_result, "None строка не должна быть палиндромом"

    # Дополнительные boundary тесты
    @pytest.mark.math
    @pytest.mark.boundary
    def test_is_prime_boundary(self, app):
        """Тест boundary случаев для простых чисел"""
        assert not app.is_prime(2147483646), "MAX_VALUE-1 не должно быть простым"

    @pytest.mark.math
    @pytest.mark.boundary
    def test_factorial_boundary(self, app):
        """Тест boundary случаев для факториала"""
        # В Python нет автоматического переполнения для целых чисел,
        # но проверим большие значения
        result = app.factorial(20)
        assert result > 0, "Факториал 20 должен быть положительным числом"

    @pytest.mark.array
    @pytest.mark.boundary
    def test_find_max_with_negative_numbers(self, app):
        """Тест поиска максимального с отрицательными числами"""
        negative_numbers = [-5, -2, -10, -1]
        assert app.find_max(negative_numbers) == -1