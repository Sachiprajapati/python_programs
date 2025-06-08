
with open(r"D:\set 7\sample.txt", 'r') as file:

    print("Using read():")
    content = file.read()
    print(content)
    
with open(r"D:\set 7\sample.txt", 'r') as file:
    
    print("\nUsing readlines():")
    content_list = file.readlines()
    print(content_list)

with open(r"D:\set 7\sample.txt", 'r') as file:
    
    print("\nUsing readline():")
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()
