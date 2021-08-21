from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    # book suggests adding a comma at the end of print statement like
    # print(line_count, f.readline()),
    # however, that's only effective in python 2.7
    # for python 3 you would do this:
    # print(line_count, f.readline(), end = "")

    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# test if readline is incremental, in fact it is
# current_file.seek(0)
# print(current_file.readline())
# print(current_file.readline())
# print(current_file.readline())
