#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(int x) {
    if (x < 0) {
        return false; // negative numbers are not palindromes
    }

    long int temp = x;
    long int sum = 0;

    while (x > 0) {
        sum = (sum * 10) + (x % 10);
        x = x / 10;
    }

    if (temp == sum) {
        return true;
    } else {
        return false;
    }
}

// Example usage
int main() {
    int number = 121;
    if (isPalindrome(number)) {
        printf("%d is a palindrome.\n", number);
    } else {
        printf("%d is not a palindrome.\n", number);
    }
    return 0;
}
