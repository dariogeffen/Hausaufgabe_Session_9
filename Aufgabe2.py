y = int(input("Select a number between 1 and 100: "))
for x in range(1,y+1):
    if (x%5)==0:
        if (x%3)==0:
            print ("fizzbuzz")
        else:
            print("buzz")
    elif (x%3)==0:
        print("fizz")
    else:
        print(f"{x}")

