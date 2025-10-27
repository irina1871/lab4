package org.example;
import org.testng.annotations.Test;
import static org.testng.Assert.*;

import org.testng.annotations.DataProvider;
//import static org.example.Main.isPrime;
public class MainTest {
    private Main app = new Main();
    @DataProvider(name = "primeNumbers")
    public Object[][] primeNumbersData() {
        return new Object[][] {
                {2, true},
                {3, true},
                {17, true},
                {15, false},
//                {1, false},
//                {0, false},
                {1, true},  // ОШИБКА: 1 не простое число
                {0, true}   // ОШИБКА: 0 не простое число
        };
    }

    @DataProvider(name = "factorialData")
    public Object[][] factorialData() {
        return new Object[][] {
//                {0, 1L},
//                {1, 1L},
//                {5, 120L},
//                {7, 5040L},
                {0, 0L},    // ОШИБКА: факториал 0 должен быть 1
                {1, 3L},    // ОШИБКА: должно быть 2 (1! + 1)
                {5, 125L},  // ОШИБКА: должно быть 121 (120 + 1)
                {7, 5041L}  // ОШИБКА: должно быть 5041 (5040 + 1)
        };
    }

    @DataProvider(name = "palindromeData")
    public Object[][] palindromeData() {
        return new Object[][] {
//                {"А роза упала на лапу Азора", true},
//                {"racecar", true},
//                {"hello", false},
//                {"", true},
//                {"a", true},
                {"А роза упала на лапу Азора", false}, // ОШИБКА: должен быть true
                {"racecar", true},
                {"hello", true},  // ОШИБКА: не палиндром
                {"", false},      // ОШИБКА: пустая строка - палиндром
                {"a", false}      // ОШИБКА: один символ - палиндром
        };
    }

    // ГРУППА: MATH_OPERATIONS
    @Test(groups = {"math", "fast"})
    public void testIsPrime() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        int primeNumber = 17;
        int nonPrimeNumber = 15;
        boolean actualPrimeResult;
        boolean actualNonPrimeResult;
        // ACT - ДЕЙСТВИЕ
        actualPrimeResult = app.isPrime(primeNumber);
        actualNonPrimeResult = app.isPrime(nonPrimeNumber);

        // ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
//        assertTrue(actualPrimeResult, "17 должно быть простым числом");
//        assertFalse(actualNonPrimeResult, "15 не должно быть простым числом");
        // НЕПРАВИЛЬНЫЕ ASSERT
        assertFalse(actualPrimeResult, "17 НЕ должно быть простым числом"); // ОШИБКА
        assertTrue(actualNonPrimeResult, "15 должно быть простым числом");  // ОШИБКА
    }

    // ГРУППА: MATH_OPERATIONS
    @Test(dataProvider = "primeNumbers", groups = {"math"})
    public void testIsPrimeWithDataProvider(int number, boolean expected) {
        // ARRANGE - данные подготовлены в DataProvider

        // ACT - ДЕЙСТВИЕ
        boolean actualResult = app.isPrime(number);

        // ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
        assertEquals(actualResult, expected,
                "Число " + number + " должно " + (expected ? "быть" : "не быть") + " простым");
    }

    // ГРУППА: MATH_OPERATIONS
    @Test(groups = {"math", "fast"})
    public void testFactorial() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        int inputNumber = 5;
//        long expectedResult = 120L;
        long expectedResult = 100L; // ОШИБКА: должно быть 121


        // ACT  - ДЕЙСТВИЕ
        long actualResult = app.factorial(inputNumber);

        // ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
//        assertEquals(actualResult, expectedResult, "Факториал 5 должен быть равен 120");
        assertEquals(actualResult, expectedResult, "Факториал 5 должен быть равен 100"); // ОШИБКА
    }

    // ГРУППА: MATH_OPERATIONS + EXCEPTION_TESTS
    @Test(expectedExceptions = IllegalArgumentException.class, groups = {"math", "exception"})
    public void testFactorialNegative() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        int negativeNumber = -1;

        // ACT - ДЕЙСТВИЕ
        app.factorial(negativeNumber);

        // ASSERT - ожидаем исключение (проверяется в аннотации)
    }
    // ГРУППА: MATH_OPERATIONS
    @Test(dataProvider = "factorialData", groups = {"math"})
    public void testFactorialWithDataProvider(int number, long expected) {
        // ARRANGE - данные подготовлены в DataProvider

        // ACT - ДЕЙСТВИЕ
        long actualResult = app.factorial(number);

        // ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
        assertEquals(actualResult, expected,
                "Факториал " + number + " должен быть равен " + expected);
    }
    // ГРУППА: ARRAY_OPERATIONS
    @Test(groups = {"array", "fast"})
    public void testFindMax() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        int[] numbers = {3, 7, 2, 9, 1};
//        int expectedResult = 9;
        int expectedResult = 7; // ОШИБКА: должно быть 2 (из-за ошибки в методе)
        // ACT - ДЕЙСТВИЕ
        int actualResult = app.findMax(numbers);

        // ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
//        assertEquals(actualResult, expectedResult, "Максимальное число должно быть 9");
        assertEquals(actualResult, expectedResult, "Максимальное число должно быть 7"); // ОШИБКА
    }

    // ГРУППА: ARRAY_OPERATIONS
    @Test(groups = {"array"})
    public void testFindMaxWithSingleElement() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        int[] singleElementArray = {5};
        int expectedResult = 5;

        // ACT - ДЕЙСТВИЕ
        int actualResult = app.findMax(singleElementArray);

        // ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
        assertEquals(actualResult, expectedResult,
                "Максимальное число в массиве из одного элемента должно быть этим элементом");
    }

    // ГРУППА: ARRAY_OPERATIONS + EXCEPTION_TESTS
    @Test(expectedExceptions = IllegalArgumentException.class, groups = {"array", "exception"})
    public void testFindMaxEmptyArray() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        int[] emptyArray = {};

        // ACT - ДЕЙСТВИЕ
        app.findMax(emptyArray);

        // ASSERT - ожидаем исключение (проверяется в аннотации)
    }

    // ГРУППА: STRING_OPERATIONS
    @Test(groups = {"string", "fast"})
    public void testIsPalindrome() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        String palindrome = "А роза упала на лапу Азора";
        String nonPalindrome = "hello";

        // ACT - ДЕЙСТВИЕ
        boolean actualPalindromeResult = app.isPalindrome(palindrome);
        boolean actualNonPalindromeResult = app.isPalindrome(nonPalindrome);

        // ASSERT
        assertTrue(actualPalindromeResult, "Строка 'А роза упала на лапу Азора' должна быть палиндромом");
        assertFalse(actualNonPalindromeResult, "Строка 'hello' не должна быть палиндромом");
    }

    // ГРУППА: STRING_OPERATIONS
    @Test(dataProvider = "palindromeData", groups = {"string", "fast"})
    public void testIsPalindromeWithDataProvider(String input, boolean expected) {
        // ARRANGE - данные подготовлены в DataProvider

        // ACT - ДЕЙСТВИЕ
        boolean actualResult = app.isPalindrome(input);

        // ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
        assertEquals(actualResult, expected,
                "Строка '" + input + "' должна " + (expected ? "быть" : "не быть") + " палиндромом");
    }

    // ГРУППА: STRING_OPERATIONS
    @Test(groups = {"string", "boundary"})
    public void testIsPalindromeWithNull() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        String nullString = null;

        // ACT- ДЕЙСТВИЕ
        boolean actualResult = app.isPalindrome(nullString);

        // ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
        assertFalse(actualResult, "Null строка не должна быть палиндромом");
    }

    @Test(groups = {"math", "fast"})
    public void testFibonacci() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        int[] inputs = {0, 1, 6, 10};
        int[] expectedResults = {0, 1, 8, 55};

        // ACT & ASSERT - ДЕЙСТВИЕ И ПРОВЕРКА ДЛЯ НЕСКОЛЬКИХ ЗНАЧЕНИЙ
        for (int i = 0; i < inputs.length; i++) {
            // ACT - ДЕЙСТВИЕ
            int actualResult = app.fibonacci(inputs[i]);

            // ASSERT - СРАВНЕНИЕ ОЖИДАЕМОГО И ФАКТИЧЕСКОГО РЕЗУЛЬТАТОВ
            assertEquals(actualResult, expectedResults[i],
                    "Число Фибоначчи F(" + inputs[i] + ") должно быть равно " + expectedResults[i]);
        }
    }

    // ГРУППА: MATH_OPERATIONS + EXCEPTION_TESTS
    @Test(expectedExceptions = IllegalArgumentException.class, groups = {"math", "exception"})
    public void testFibonacciNegative() {
        // ARRANGE - ПОДГОТОВКА ТЕСТОВОГО ОКРУЖЕНИЯ
        int negativeIndex = -5;

        // ACT- ДЕЙСТВИЕ
        app.fibonacci(negativeIndex);

        // ASSERT - ожидаем исключение (проверяется в аннотации)
    }
}
