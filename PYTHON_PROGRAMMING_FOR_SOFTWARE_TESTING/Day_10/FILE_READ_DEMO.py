try:
    file = open(
        r"E:\SEED_PROGRAMING_SDET_COURSE\PYHTON_PROGRAMMING_FOR_SOFTWARE_TESTING\PYTHON_PROGRAMMING_FOR_SOFTWARE_TESTING\Day_10\READ.txt",
        'r')
    print(file.read())
except FileNotFoundError:
    print("The file was not found. Please check the file path.")
