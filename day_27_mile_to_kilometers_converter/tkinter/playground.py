def add(*args):
    print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 4, 2, 1, 7, 4, 3))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # the get method is beneficial because if the
        # value doesn't exist than you will
        # receive a 'none' error
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
