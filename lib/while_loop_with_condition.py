class While_Loop_With_Condition:
    def __init__(self):
        # Initialize instance variables here if needed
        self.example_string = "Hello, Python!"
        self.example_array = [1, 2, 3, 4, 5]
        self.example_dict = {"name": "John", "age": 30, "city": "New York"}
        self.example_set = {1, 2, 3, 4, 5}

    def while_loop_string(self):
        index = 0
        while index < len(self.example_string):
            print(self.example_string[index])
            index += 1

    def while_loop_array(self):
        index = 0
        while index < len(self.example_array):
            print(self.example_array[index])
            index += 1

    def while_loop_dict_keys(self):
        keys = list(self.example_dict.keys())
        index = 0
        while index < len(keys):
            print("Key:", keys[index])
            index += 1

    def while_loop_dict_values(self):
        values = list(self.example_dict.values())
        index = 0
        while index < len(values):
            print("Value:", values[index])
            index += 1

    def while_loop_dict_items(self):
        items = list(self.example_dict.items())
        index = 0
        while index < len(items):
            key, value = items[index]
            print(f"Key: {key}, Value: {value}")
            index += 1

    def while_loop_set(self):
        while self.example_set:
            item = self.example_set.pop()
            print(item)

    def while_loop_with_condition(self):
        i = 0
        while i < 5:
            print(i)
            i += 1

    def while_loop_with_break(self):
        i = 0
        while True:
            print(i)
            i += 1
            if i == 5:
                break

    def while_loop_with_continue(self):
        i = 0
        while i < 5:
            i += 1
            if i == 3:
                continue
            print(i)

    def while_loop_with_else(self):
        i = 0
        while i < 5:
            print(i)
            i += 1
        else:
            print("Loop Finished")

# Run this script to define the classes and their methods.
if __name__ == "__main__":
    pass
