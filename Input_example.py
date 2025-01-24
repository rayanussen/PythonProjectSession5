name = input("What is your name?")
print("Hello", name)
age = input("how old are you "+name+"?")
print(name+"based on my calculations, you were born in "+str(2024-int(age)))

# write this in a simpler way

age2= input(f"How old are you{name}?")
age2= int(age2)
print(f"{name},you were born in {2024-age2}")