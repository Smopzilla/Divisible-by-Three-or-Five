#!/usr/bin/env python
# Peri
# 2021.12.13
# Final Exam Part II
# FinalProject.py
# Using Mu 1.1.0.beta.3
# Loop through range of numbers received by user and determine
# if numbers are evenly divisible by 3, 5, or both.

# Create function
def mod_3_5():
    while True:
        try:
            # Get starting value
            start_num = int(input("Please enter starting value: "))
            break
        except ValueError:
            # Catch an error
            print("Enter a non-floating number only!")
            continue

    while True:
        try:
            # Get ending value
            end_num = int(input("Please enter ending value: ")) + 1
            # Check if number is higher than starting value
            if end_num <= start_num:
                print("Enter a number higher than", str(start_num) + "!")
                continue
        except ValueError:
            # Catch an error
            print("Enter a non-floating number only!")
            continue
        break

    for x in range(start_num, end_num):
        if x % 3 == 0:
            if x % 5 == 0:
                print(x, "--Both")
            else:
                print(x, "--3")
        elif x % 5 == 0:
            print(x, "--5")
        else:
            print(x)

# Specify function
def main():
    mod_3_5()

# Call main
if __name__ == "__main__":
    main()
