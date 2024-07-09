class MyClass:
    # Class variable
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        # Instance variable
        self.instance_variable = instance_variable

    # Method
    def display_variables(self):
        print(f"Instance Variable: {self.instance_variable}")
        print(f"Class Variable: {MyClass.class_variable}")

# Create an instance of MyClass
obj = MyClass("I am an instance variable")

# Call the method
obj.display_variables()