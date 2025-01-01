print("##########################")
print("#       CALCULATOR       #")
print("##########################\n")
number_1 = int(input("Enter First Number:\n"));
number_2 = int(input("Enter Second Number:\n"));
Operation = int(input("Enter Number for the Operation: Addition(1), Subtraction(2), Multiplication(3), Modulous(4), Division(5)\n"));
if Operation == 1:
        print("Output is:", number_1 + number_2)
elif Operation == 2:
        print("Output is:", number_1 - number_2)
elif Operation == 3:
        print("Output is:", number_1 * number_2)
elif Operation == 4:
        print("Output is:", number_1 % number_2)
elif Operation == 5:
        if number_2 == 0:
                print("Division By 0 not possible")
        else:
                print("Output is:", number_1 / number_2)
else:
        print("Invalid Operation Selected");



