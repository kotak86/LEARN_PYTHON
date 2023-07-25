class Set_Means_HashSet:
    def __init__(self):
        # Initialize instance variables here if needed
        self.example_set = {1, 2, 3, 4, 5}

    def set_example(self):
        set_var = {1, 2, 3, 4, 5}
        print("Set Example:", set_var)

    def set_methods_example(self):
        self.example_set.add(6)
        self.example_set.remove(2)
        print("Set Methods Example:", self.example_set)

    def set_operations_example(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        union_set = set1.union(set2)
        intersection_set = set1.intersection(set2)
        print("Set Union Example:", union_set)
        print("Set Intersection Example:", intersection_set)