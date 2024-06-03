# The definition of the function that takes an Int input and returns that many terms of the Fibonacci Series.
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


# Main function that takes the input from the user, handles errors, passes the input to the fibonacci function and prints the returned output.
def main():
    while True:
        try:
            n = int(input("Enter the number of Fibonacci numbers to generate: "))
            if n > 0:
                fib_sequence = fibonacci(n)
                print(f"The first {n} values of the Fibonacci series are:")
                print(fib_sequence)
                break
            else:
                print("Please enter a positive integer.")
            
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
