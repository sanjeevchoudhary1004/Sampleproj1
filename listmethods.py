x = [10,20,30,40,50,20]
print(x)
while True:
     p = int(input("Enter serach element"))
     if p in x:
         print("Element found")
         break
     else:
         print("Element not found")