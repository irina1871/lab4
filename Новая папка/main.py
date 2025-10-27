from math_functions import MathFunctions


def main():
    math = MathFunctions()

    print("Демонстрация математических функций")
    print("=" * 40)

    # Демонстрация проверки простых чисел
    print("1. Проверка простых чисел:")
    test_primes = [2, 3, 4, 17, 25]
    for num in test_primes:
        result = math.is_prime(num)
        print(f"   {num} - {'простое' if result else 'не простое'}")

    # Демонстрация вычисления факториала
    print("\n2. Вычисление факториала:")
    test_factorials = [0, 1, 5, 7]
    for num in test_factorials:
        result = math.factorial(num)
        print(f"   {num}! = {result}")

    # Демонстрация поиска максимального числа
    print("\n3. Поиск максимального числа:")
    test_arrays = [
        [1, 2, 3],
        [-1, -5, -3],
        [1.5, 2.7, 0.3]
    ]
    for arr in test_arrays:
        result = math.find_max(arr)
        print(f"   Максимум в {arr} = {result}")

    # Демонстрация проверки палиндромов
    print("\n4. Проверка палиндромов:")
    test_strings = ["racecar", "hello", "A man a plan a canal Panama", "12321"]
    for text in test_strings:
        result = math.is_palindrome(text)
        print(f"   '{text}' - {'палиндром' if result else 'не палиндром'}")

    # Демонстрация чисел Фибоначчи
    print("\n5. Числа Фибоначчи:")
    print("   Отдельные числа:")
    for i in range(10):
        result = math.fibonacci(i)
        print(f"   F({i}) = {result}")

    print("\n   Последовательности:")
    for length in [5, 8]:
        result = math.fibonacci_sequence(length)
        print(f"   Первые {length} чисел: {result}")


if __name__ == "__main__":
    main()