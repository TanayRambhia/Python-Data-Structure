txt = "hello, i am tanay."
x = txt.capitalize()
print (x)

txt = "Hello, I am Tanay!"
x = txt.casefold()
print(x)

txt = "banana"
x = txt.center(20)
print(x)

txt = "Hello Tanay, Tanay loves to tudy"
x = txt.count("Tanay")
print(x)

txt = "My name is Tanay"
x = txt.encode()
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Tanay12"
x = txt.isalnum()
print(x)

txt = "Tanay"
x = txt.isalpha()
print(x)

txt = "Tanay123"
x = txt.isascii()
print(x)

myTuple = ("Tanay", "Ravi", "Vayu")
x = ",".join(myTuple)
print(x)

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

txt = "     Tanay     "
x = txt.lstrip()
print("Hello ", x)

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "Hello, I am Tanay."
x = txt.rfind("Tanay")
print(x)

txt = "Hello, I am Tanay."
x = txt.rindex("Tanay")
print(x)

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)


txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "Hello my friends"
x = txt.upper()
print(x)