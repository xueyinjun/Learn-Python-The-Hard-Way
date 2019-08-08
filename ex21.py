#encoding =utf-8


def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subract(a, b):
    print("SUBTRACTING %d-%d" % (a, b))
    return a-b

def multiply(a, b):
    print("MULTIPING %d * %d" % (a, b))
    return a*b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's do some math with just function")

age = add(30, 5)
height = subract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print("Age: %d, Height: %d,Weight: %d,IQ: %d" % (age, height, weight, iq))

#A puzzle for the extra credit,type it in anyway
print("Here is a puzzle")

what = add(age, subract(height, multiply(weight, divide(iq, 2))))

print("That become:",what,"Can you do it by hand?")
