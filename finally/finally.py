try:
    l = [1,3,5,6,7,8]
    i = int(input("enter the index: "))
    print(l[i])
    
except:
    print("some error occured")
    
finally:
    print("I am always excucuted")
