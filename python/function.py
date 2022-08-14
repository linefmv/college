def main():
    for i in range(3):
        meow()

def meow():
    print("meow")

main()


def main():
    meow(1)

def meow(n):
    for i in range(n):
        print("meow")

main()



def main():
    height = get_height()
    for i in range(height):
        print("#")
  
def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                break
        except ValueError:
            print("That's not an integer!")
    return n
  
main()