#with arguments and with return type
def find_cube(number):
    return number ** 3
num = int(input("enter the number:"))
cube_result = find_cube(num)
print("The cube of {} is:", cube_result)
