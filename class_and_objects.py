# class and objects
class Myprogram:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:\t", self.name)
        print("Age:\t", self.age)


if __name__ == "__main__":
    class_object = Myprogram("sameer", 19)
    class_object.display_details()


# end of program
