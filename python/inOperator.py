name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

for i in [0, 1, 2]:
    print("hello, world")

for i in range(3):
    print("hello, world")


for i in range(4):
    print("?", end="")
print()

for i in range(3):
    for j in range(3):
        print("#", end="")
    print()