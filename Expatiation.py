a = input("enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
     print(f"{int(a)}X {i} = {int(a)*i}")
except Exception as e:
   print("sorry some error occured")
print("some imp lines of code")
print("end of program")
