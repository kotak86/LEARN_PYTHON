class For_Loop_With_Condition:
    def __init__(self):
        # Initialize instance variables here if needed
        self.example_string = "Hello, Python!"
        self.example_array = [1, 2, 3, 4, 5]
        self.example_dict = {"name": "John", "age": 30, "city": "New York"}
        self.example_set = {1, 2, 3, 4, 5}

    def for_loop_string(self):
        for char in self.example_string:
            print(char)

    def for_loop_array(self):
        for num in self.example_array:
            print(num)

    def for_loop_dict_keys(self):
        for key in self.example_dict:
            print("Key:", key)

    def for_loop_dict_values(self):
        for value in self.example_dict.values():
            print("Value:", value)

    def for_loop_dict_items(self):
        for key, value in self.example_dict.items():
            print(f"Key: {key}, Value: {value}")

    def for_loop_set(self):
        for item in self.example_set:
            print(item)

    def for_loop_with_range(self):
        for i in range(5):
            print(i)

    def for_loop_with_start_and_end(self):
        for i in range(2, 7):
            print(i)

    def for_loop_with_step(self):
        for i in range(1, 10, 2):
            print(i)

    def for_loop_with_enumerate(self):
        for index, value in enumerate(self.example_array):
            print(f"Index: {index}, Value: {value}")

# Run this script to define the classes and their methods.
if __name__ == "__main__":
    pass
