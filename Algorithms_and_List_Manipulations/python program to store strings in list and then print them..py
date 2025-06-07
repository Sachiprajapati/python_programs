string_list = []

num_strings = int(input("Enter the number of strings you want to store: "))

for _ in range(num_strings):
    string = input("Enter a string: ")
    string_list.append(string)

print("\nStored strings are:")
for string in string_list:
    print(string)
