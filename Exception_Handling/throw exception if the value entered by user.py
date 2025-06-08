class NegativeValueError(Exception):
    """Custom exception for handling negative values."""
    pass

def get_positive_number():
    try:
        # Ask user for input
        user_input = float(input("Enter a number: "))
        
        # Check if the input is less than zero
        if user_input < 0:
            raise NegativeValueError("The entered value is less than zero. Please enter a non-negative value.")
        
        print(f"You entered: {user_input}")
        
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except NegativeValueError as e:
        print(e)

if __name__ == "__main__":
    get_positive_number()
