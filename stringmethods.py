x = "lokeshit python"
print(x)
print(x.capitalize())
print(x.title())
print(x.upper())
print(x.lower())
print(x.isupper())
print(x.islower())
print(x.isalpha())
print(x.isdigit())

y = "12345"
print(y)
print(y.isdigit())

z = "python@is@a@opensource@language"
print(z)
words = z.split("@")
for w in words:
    print(w,w.upper(),len(w))