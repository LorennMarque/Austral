# one.py
print("hello world from one")

def func():
    print("FUNC() IN ONE.py")

print("TOP LEVEL IN ONE.py")


if __name__ == "__main__":
    print("Ran directly")
else:
    print("Ran indirectly. Imported!")