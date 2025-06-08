def divide_numbers(num1, num2):
    try:
        # Attempt to perform the division
        result = num1 / num2
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")
    else:
        # This block executes if no exceptions are raised
        print(f"The result of {num1} divided by {num2} is {result}.")
    finally:
        # This block always executes, regardless of exceptions
        print("Execution of finally block.")

# Test cases
print("Test Case 1: Normal Division")
divide_numbers(10, 2)  # Should work normally

print("\nTest Case 2: Division by Zero")
divide_numbers(10, 0)  # Should handle the ZeroDivisionError

print("\nTest Case 3: Another Normal Division")
divide_numbers(20, 5)  # Should work normally
