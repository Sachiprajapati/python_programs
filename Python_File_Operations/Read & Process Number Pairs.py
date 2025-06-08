
def process_numbers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            numbers = line.split()
            if len(numbers) == 2:  
                try:
                    num1 = int(numbers[0])
                    num2 = int(numbers[1])

                    addition = num1 + num2
                    multiplication = num1 * num2

                    outfile.write(f"{num1} {num2} | Addition: {addition} | Multiplication: {multiplication}\n")
                except ValueError:
                    outfile.write("Invalid number pair found.\n")

input_file = r"D:\5th sem\python\22BEIT30165\set 7\numbers.txt"  # replace with you txt file address
output_file = r"D:\5th sem\python\22BEIT30165\set 7\results.txt"

process_numbers(input_file, output_file)

print(f"Results have been written to {output_file}")
