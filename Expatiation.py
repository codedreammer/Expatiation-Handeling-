'''
a = input("enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
     print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
   print("Invaild Input!")
print("some imp lines of code")
print("end of program")

# more example 
try:
    num =int(input("enter an integer:"))
    a = [6,3]
    print(a[num])
except ValueError:
    print("number entered is not an integer")

except IndexError:
    print("Index Error")

try:
    num = int(input("enter an integer: "))
    a = [1,100]
    print(a[num])
except ValueError:
    print("value error")

except IndexError:
    print("index error")
'''
a = input("enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
     print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
   print("Invaild Input!")
print("some imp lines of code")
print("end of program") 





