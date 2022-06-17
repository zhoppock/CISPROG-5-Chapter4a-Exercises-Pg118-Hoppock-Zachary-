print("Exercise 1")
data = "Python rules!"
print(" > String:", data)
#a
print(data.split())
#b
print(data.upper())
#c
print(data.find("rules"))
#d
print(data.replace('!','?'))

print("\nExercise 2")
data = "Python rules!"
print(" > String:", data)
#a
print(data.endswith('i'))
#b
print(" totally ".join(data.split()))