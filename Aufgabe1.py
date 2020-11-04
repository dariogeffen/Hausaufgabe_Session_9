print ("This program converts kilometers to miles.")
km = int(input ("Please enter the number of km you want to convert to miles: "))
m = 0.621371 * km
print (f'{km} km are {m} miles')
proceed = input ("Do you want to do another calculation?")
while True:
    if proceed== "No":
        print("Cool, thanks for running me. C'ya!")
        break
    else:
        m = 0.621371 * km
        print(f'{km} km are {m} miles')
        proceed = input("Do you want to do another calculation?")


