package com.dindin;

public class Main {

    public static void main(String[] args) {
//        numberToWords(123);
//        for (int i = 1; i < 100000000; i *= 2) {
//            System.out.println("Current i : " + i);
//            System.out.println(getDigitCount(i));
//        }
        System.out.println(reverse(-2));
        numberToWords(123);
        numberToWords(100);
        numberToWords(0);
        numberToWords(-2);
    }

    public static final String INVALID_VALUE_MESSAGE="Invalid Value";

    public static void numberToWords (int number) {
        if (number < 0) {
            System.out.println(INVALID_VALUE_MESSAGE);
        }
        int digitCount = getDigitCount(number);
        int reversed = reverse(number);
        while (digitCount > 0) {
            int lastDigit = reversed % 10;
            switch (lastDigit) {
                case 1:
                    System.out.println("One");
                    break;
                case 2:
                    System.out.println("Two");
                    break;
                case 3:
                    System.out.println("Three");
                    break;
                case 4:
                    System.out.println("Four");
                    break;
                case 5:
                    System.out.println("Five");
                    break;
                case 6:
                    System.out.println("Six");
                    break;
                case 7:
                    System.out.println("Seven");
                    break;
                case 8:
                    System.out.println("Eight");
                    break;
                case 9:
                    System.out.println("Nine");
                    break;
                default:
                    System.out.println("Zero");
                    break;
            }
            digitCount--;
            reversed /= 10;
        }
    }

    public static int reverse (int number) {
        boolean isNegative = number < 0 ? true : false;
        number = Math.abs(number);
        int newNumber = 0;
        while (number >= 1) {
            newNumber += number % 10;
            newNumber *= 10;
            number /= 10;
        }
        return isNegative ? -1 * newNumber / 10 : newNumber / 10;
    }

    public static int getDigitCount (int number) {
        if (number < 0) {
            return -1;
        }
        if (number == 0) {
            return 1;
        }
        int count = 0;
        while (number >= 1) {
            number /= 10;
            count++;
        }
        return count;
    }

}
