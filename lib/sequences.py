#!/usr/bin/env python3

def print_fibonacci(length):
    
    fibonacci_seq = []
    if length > 0:
        fibonacci_seq.append(0)
        if length > 1:
            fibonacci_seq.append(1)
            if length > 2:
                for i in range(2, length):
                    fibonacci_seq.append(
                        fibonacci_seq[i-1] + fibonacci_seq[i-2])

    print(fibonacci_seq)
    