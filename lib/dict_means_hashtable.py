
class Dict_Means_HashTable:
    def __init__(self):
        # Initialize instance variables here if needed
        self.example_dict = {"name": "John", "age": 30, "city": "New York"}

    def dictionary_example(self):
        dict_var = {"name": "John", "age": 30, "city": "New York"}
        print("Dictionary Example:", dict_var)

    def access_dict_elements(self):
        print("Name:", self.example_dict["name"])
        print("Age:", self.example_dict["age"])
        print("City:", self.example_dict["city"])

    def dict_methods_example(self):
        self.example_dict["occupation"] = "Engineer"
        del self.example_dict["city"]
        print("Dictionary Methods Example:", self.example_dict)

    def dict_keys_and_values_example(self):
        keys = self.example_dict.keys()
        values = self.example_dict.values()
        print("Dictionary Keys Example:", keys)
        print("Dictionary Values Example:", values)



# Run this script to define the classes and their methods.
if __name__ == "__main__":
    pass
