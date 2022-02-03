# class
class Robot:
    # method
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    # method
    def introduce_self(self):
        print(f"My name is {self.name}")


# "instantiation (the process of creating an object from a class)"
# object
r1 = Robot("Bob", "pink", 20)
r2 = Robot("Dave", "green", 30)

r1.introduce_self()
r2.introduce_self()