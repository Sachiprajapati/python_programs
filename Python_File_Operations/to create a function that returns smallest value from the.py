
def find_smallest_value(file_name):
    try:
        with open(file_name, 'r') as file:
            numbers = []

            for line in file:
                line_numbers = line.split()
                numbers.extend([int(num) for num in line_numbers])

            if numbers:
                return min(numbers)
            else:
                return None 
    except ValueError:
        return "The file contains non-numeric data."
    except FileNotFoundError:
        return "The file was not found."

file_name = r"D:\5th sem\python\22BEIT30165\set 7\num.txt"

smallest_value = find_smallest_value(file_name)
if smallest_value is not None:
    print(f"The smallest value in the file is: {smallest_value}")
else:
    print("The file is empty or contains invalid data.")
