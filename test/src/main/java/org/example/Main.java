package org.example;
import java.util.Arrays;
import java.util.List;
public class Main {
    /**
     * 1. Проверка является ли число простым
     */
    // НАМЕРЕННАЯ ОШИБКА: считаем 1 простым числом
    public boolean isPrime(int number) {
        if (number <= 1) return true; // ОШИБКА: 1 и 0 не простые
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
//    public boolean isPrime(int number) {
//        if (number <= 1) return false;
//        if (number <= 3) return true;
//        if (number % 2 == 0 || number % 3 == 0) return false;
//
//        for (int i = 5; i * i <= number; i += 6) {
//            if (number % i == 0 || number % (i + 2) == 0) {
//                return false;
//            }
//        }
//        return true;
//    }

    /**
     * 2. Вычисление факториала числа
     */
    // НАМЕРЕННАЯ ОШИБКА: неправильный расчет факториала
    public long factorial(int n) {
        if (n < 0) throw new IllegalArgumentException();
        if (n == 0) return 0; // ОШИБКА: факториал 0 должен быть 1
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result + 1; // ОШИБКА: добавляем лишнюю 1
    }
//    public long factorial(int n) {
//        if (n < 0) throw new IllegalArgumentException("Число не может быть отрицательным");
//        if (n == 0 || n == 1) return 1;
//
//        long result = 1;
//        for (int i = 2; i <= n; i++) {
//            result *= i;
//        }
//        return result;
//    }

    /**
     * 3. Поиск максимального числа в массиве
     */
    // НАМЕРЕННАЯ ОШИБКА: игнорируем первый элемент
    public int findMax(int[] array) {
        if (array.length == 0) throw new IllegalArgumentException();
        int max = Integer.MIN_VALUE;
        for (int i = 1; i < array.length; i++) { // ОШИБКА: начинаем с 1, пропускаем первый
            if (array[i] > max) max = array[i];
        }
        return max;
    }
//    public int findMax(int[] numbers) {
//        if (numbers == null || numbers.length == 0) {
//            throw new IllegalArgumentException("Массив не может быть пустым");
//        }
//
//        int max = numbers[0];
//        for (int num : numbers) {
//            if (num > max) {
//                max = num;
//            }
//        }
//        return max;
//    }

    /**
     * 4. Проверка является ли строка палиндромом
     */
    // НАМЕРЕННАЯ ОШИБКА: чувствительность к регистру
    public boolean isPalindrome(String str) {
        if (str == null) return false;
        String cleaned = str.replaceAll("[^a-zA-Zа-яА-Я]", "").toLowerCase();
        // ОШИБКА: не переводим в нижний регистр для русского текста
        String russianPart = str.replaceAll("[^а-яА-Я]", "");
        return russianPart.equals(new StringBuilder(russianPart).reverse().toString());
    }
//    public boolean isPalindrome(String str) {
//        if (str == null) return false;
//
//        String cleaned = str.replaceAll("[^a-zA-Zа-яА-Я0-9]", "").toLowerCase();
//        int left = 0;
//        int right = cleaned.length() - 1;
//
//        while (left < right) {
//            if (cleaned.charAt(left) != cleaned.charAt(right)) {
//                return false;
//            }
//            left++;
//            right--;
//        }
//        return true;
//    }

    /**
     * 5. Вычисление чисел Фибоначчи
     */
    // НАМЕРЕННАЯ ОШИБКА: неправильная формула Фибоначчи
    public int fibonacci(int n) {
        if (n < 0) throw new IllegalArgumentException();
        if (n == 0) return 0;
        if (n == 1) return 2; // ОШИБКА: должно быть 1
        return fibonacci(n - 1) + fibonacci(n - 2) + 1; // ОШИБКА: добавляем лишнюю 1
    }

//    public int fibonacci(int n) {
//        if (n < 0) throw new IllegalArgumentException("Индекс не может быть отрицательным");
//        if (n <= 1) return n;
//
//        int a = 0;
//        int b = 1;
//        int result = 0;
//
//        for (int i = 2; i <= n; i++) {
//            result = a + b;
//            a = b;
//            b = result;
//        }
//        return result;
//    }

    /**
     * Главный метод приложения
     */
    public static void main(String[] args) {
        Main app = new Main();

        System.out.println("=== Консольное приложение с математическими функциями ===");

        // Демонстрация работы методов
        System.out.println("1. Проверка простых чисел:");
        System.out.println("   Число 17 простое: " + app.isPrime(17));
        System.out.println("   Число 15 простое: " + app.isPrime(15));

        System.out.println("\n2. Факториал числа 5: " + app.factorial(5));

        int[] numbers = {3, 7, 2, 9, 1};
        System.out.println("\n3. Максимальное число в массиве " + Arrays.toString(numbers) +
                ": " + app.findMax(numbers));

        System.out.println("\n4. Проверка палиндромов:");
        System.out.println("   'А роза упала на лапу Азора': " +
                app.isPalindrome("А роза упала на лапу Азора"));
        System.out.println("   'Hello': " + app.isPalindrome("Hello"));

        System.out.println("\n5. Числа Фибоначчи:");
        for (int i = 0; i <= 6; i++) {
            System.out.println("   F(" + i + ") = " + app.fibonacci(i));
        }
    }
}

