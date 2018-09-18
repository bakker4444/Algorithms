package com.dindin;

public class Main {

    public static void main(String[] args) {
        System.out.println(isPerfectNumber(6));
        System.out.println(isPerfectNumber(28));
        System.out.println(isPerfectNumber(5));
        System.out.println(isPerfectNumber(-1));
    }

    public static boolean isPerfectNumber (int number) {
        if (number < 1) {
            return false;
        }
        int sum = 0;
        int count = 1;
        while (count < number) {
            if (number % count == 0) {
                sum += count;
            }
            count++;
        }
        return sum == number ? true : false;
    }

}
