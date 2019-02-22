import os

filepath = input("Enter the path to the file :")   #taking the path of the input file from the user

try:
    input_text = open(filepath, "r")       #Opening the input file in read mode
except IOError:
    print("File not found")
    print("Please provide te correct path to the file like (ex:/home/kunal/Desktop/InfosysProjects/Project/input.txt)")

filename = os.path.splitext(filepath)[0]   #Getting the file name
output_filename = filename + "Scrambled"   #Name for the output filename using the input filename with joining Scrambled
output_text = open(output_filename, "w")   #Opening the output file in the read mode

# Function to shuffle the chars around
def shuffle(word):
    if len(word) == 1:
        return word
    else:
        half = int(len(word) / 2)
        # First half in reverse
        first = word[:half][::-1]
        # Last half in reverse
        last = word[half:len(word)][::-1]

        # First + Last in reverse
        return str(first + last)[::-1]

# Function to scramble the word
def scramble(word):
    if len(word) < 3:
        return word

    first = word[:1]
    last = word[-1:]
    mid = word[1:-1]

    if last == "." or last == ",":
        last = word[-2:]
        mid = word[1:-2]

    return str(first) + str(shuffle(mid)) + str(last)

# Read the input and write the scrambled words to the output
for line in input_text:
    line = line.strip()
    new_line = ""

    for word in line.split(" "):
        new_line += scramble(word) + " "

    print(new_line,file = output_text)

print("Words Scrambled File Successfully created")
