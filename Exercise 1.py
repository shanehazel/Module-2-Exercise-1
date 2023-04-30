# pseudocode

# make a method
def process ():
    # open numbers.txt file (read), even.txt (append), odd.txt (append)
    with open("numbers.txt") as input_file, open("even.txt", "a") as output_even, open("odd.txt", "a") as output_odd:
        # read numbers.txt line by line
        for line in input_file:
            input_num = int(line)
        # if even,
            # write to even.txt
        # if odd,
            # write to odd.txt