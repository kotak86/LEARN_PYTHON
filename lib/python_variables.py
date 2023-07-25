class PythonVariables:
    def __init__(self, x, y="Initialized instance variable"):
        # Initialize instance variables here if needed
        self.version = x
        self.instance_var = y

    def integer_example(self):
        integer_var = 10
        print("Integer Variable:", integer_var)

    def float_example(self):
        float_var = 3.14
        print("Float Variable:", float_var)

    def string_example(self):
        string_var = "Hello, Python!"
        print("String Variable:", string_var)

    def boolean_example(self):
        boolean_var = True
        print("Boolean Variable:", boolean_var)

    def list_example(self):
        list_var = [1, 2, 3, 4, 5]
        print("List Variable:", list_var)

    def tuple_example(self):
        tuple_var = (1, 2, 3, 4, 5)
        print("Tuple Variable:", tuple_var)

    def set_example(self):
        set_var = {1, 2, 3, 4, 5}
        print("Set Variable:", set_var)

    def dictionary_example(self):
        dict_var = {"name": "John", "age": 30, "city": "New York"}
        print("Dictionary Variable:", dict_var)

    def none_example(self):
        none_var = None
        print("None Variable:", none_var)

# Run this script to define the class and its methods.
if __name__ == "__main__":
    pass
