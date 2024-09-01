#!/usr/bin/env python3

def print_fibonacci(n):
    if n < 0:
        print("Please enter a positive integer")
        return
    
    fibonacci_sequence = []
    
    if n == 0:
        print(fibonacci_sequence)
        return
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    print(fibonacci_sequence)

# Example usage:
print_fibonacci(10)