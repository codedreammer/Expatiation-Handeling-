def fun1():
 try:
     l = [1,3,5,6,7,8]
     i = int(input("enter the index: "))
     print(l[i])
     return 1
 except:
    print("some error occured")
    return 0
 finally:
    print("I am always excucuted")
 
x = fun1()
print(x)


    

