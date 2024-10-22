# work in this block of code only and exit automatically after to get rid of f.close()
with open('text.txt', 'r') as f:
    pass
print(f.closed)  ## to check if file is open or not
f = open('text.txt', 'r')  ## we open file text in mode read only
print(f.name)
print(f.mode)
f.close()  ## to close file
#/**************************************************************************/
with open('text.txt', 'r') as file:
    f_contents = f.read()
    f_line = f.readline()  ## assign the first line to the variable and print it
    print(f_line)
    print(f_contents)
#another way to print lines by for loop working with f as array contain file contains
for line in f:
    print(line, end=" ")
#/********************************************************/
# when trying to read an empty file after printing its content it will return empty file only
# printing in a known amount of chars :
with open('text.txt' , 'r') as f :
    size_to_read = 10
    f_content = f.read(size_to_read)
    while len(f_content):
        print(f_content,end=" ")
        f_content = f.read(size_to_read)
    print(f.tell()) # print size of the chars printed
f.seek() # after reading number of chars it return to the first of the file after
