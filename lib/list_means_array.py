
class List_Means_Array:
    def __init__(self):
        # Initialize instance variables here if needed
        self.example_list = [1, 2, 3, 4, 5]

    def integer_example(self):
        integer_list = [1, 2, 3, 4, 5]
        print("Integer List Example:", integer_list)

    def float_example(self):
        float_list = [3.14, 2.71, 1.618]
        print("Float List Example:", float_list)

    def string_example(self):
        string_list = ["apple", "banana", "orange"]
        print("String List Example:", string_list)

    def mixed_list_example(self):
        mixed_list = [1, "hello", 3.14, True]
        print("Mixed List Example:", mixed_list)

    def nested_list_example(self):
        nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print("Nested List Example:", nested_list)

    def list_comprehension_example(self):
        nums = [1, 2, 3, 4, 5]
        squared_nums = [num**2 for num in nums]
        print("List Comprehension Example:", squared_nums)

    def list_slices_example(self):
        original_list = [1, 2, 3, 4, 5]
        slice_example = original_list[1:4]
        print("List Slices Example:", slice_example)

    def list_methods_example(self):
        fruits = ["apple", "banana", "orange"]
        fruits.append("grape")
        fruits.insert(1, "kiwi")
        fruits.remove("banana")
        print("List Methods Example:", fruits)

    def list_concatenation_example(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        combined_list = list1 + list2
        print("List Concatenation Example:", combined_list)

    def list_length_example(self):
        my_list = [1, 2, 3, 4, 5]
        length = len(my_list)
        print("List Length Example:", length)

# Run this script to define the class and its methods.
if __name__ == "__main__":
    pass
