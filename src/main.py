import os
import sys

current_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
print(current_directory)
sys.path.insert(0, current_directory)
print(sys.path)

# Import the PythonVariables class from PythonVariables.py
from lib.python_variables import PythonVariables
from lib.list_means_array import List_Means_Array
from lib.dict_means_hashtable import Dict_Means_HashTable
from lib.set_means_hashset import Set_Means_HashSet
from lib.for_loop_with_condition import For_Loop_With_Condition
from lib.while_loop_with_condition import While_Loop_With_Condition
from lib.file_handling import FileHandling



def main():
    # run_python_variables_class()
    run_list_means_array_class()
    run_dict_means_hashtable_class()
    run_set_means_hashset_class()
    run_for_loop_with_condition_class()
    run_while_loop_with_condition_class()
    run_file_handling_class()


def run_file_handling_class():
    file_handler = FileHandling()

    # Read from log file
    log_file_path = "data/example.log"
    file_handler.read_log_file(log_file_path)

    # Read from JSON file
    json_file_path = "data/example.json"
    file_handler.read_json_file(json_file_path)

    # Read from YAML file
    yaml_file_path = "data/example.yaml"
    file_handler.read_yaml_file(yaml_file_path)

    # Write to log file
    log_content = [
    "TIME STAMP: server1: Process1 : Design1 ; Log Entry 1",
    "TIME STAMP: server2: Process2 : Design2 ; Log Entry 2",
    "TIME STAMP: server3: Process3 : Design3 ; Log Entry 3",
    # Add more lines here as needed
]

    new_log_file_path = "data/example_new.log"
    file_handler.write_log_file(new_log_file_path, log_content)

    # Write to JSON file
    new_json_file_path = "data/example_new.json"
    json_data = {"name": "John", "age": 30, "city": "New York"}
    file_handler.write_json_file(new_json_file_path, json_data)

    # Write to YAML file
    new_yaml_file_path = "data/example_new.yaml"
    yaml_data = {"name": "Alice", "age": 25, "city": "London"}
    file_handler.write_yaml_file(new_yaml_file_path, yaml_data)

def run_while_loop_with_condition_class():
    # Create an instance of While_Loop_With_Condition class (the __init__ method will be automatically called)
    while_loop_examples = While_Loop_With_Condition()

    # Call the functions to demonstrate different while loop scenarios
    while_loop_examples.while_loop_string()
    while_loop_examples.while_loop_array()
    while_loop_examples.while_loop_dict_keys()
    while_loop_examples.while_loop_dict_values()
    while_loop_examples.while_loop_dict_items()
    while_loop_examples.while_loop_set()
    while_loop_examples.while_loop_with_condition()
    while_loop_examples.while_loop_with_break()
    while_loop_examples.while_loop_with_continue()
    while_loop_examples.while_loop_with_else()

def run_for_loop_with_condition_class():
    # Create an instance of For_Loop_With_Condition class (the __init__ method will be automatically called)
    for_loop_examples = For_Loop_With_Condition()

    # Call the functions to demonstrate different for loop scenarios
    for_loop_examples.for_loop_string()
    for_loop_examples.for_loop_array()
    for_loop_examples.for_loop_dict_keys()
    for_loop_examples.for_loop_dict_values()
    for_loop_examples.for_loop_dict_items()
    for_loop_examples.for_loop_set()
    for_loop_examples.for_loop_with_range()
    for_loop_examples.for_loop_with_start_and_end()
    for_loop_examples.for_loop_with_step()
    for_loop_examples.for_loop_with_enumerate()


def run_dict_means_hashtable_class():
    # Create an instance of Dict_Means_HashTable class (the __init__ method will be automatically called)
    dict_examples = Dict_Means_HashTable()

    # Access the example_dict from __init__ method
    print("Instance Variable - example_dict:", dict_examples.example_dict)

    # Call the functions to demonstrate different dictionary examples
    dict_examples.dictionary_example()
    dict_examples.access_dict_elements()
    dict_examples.dict_methods_example()
    dict_examples.dict_keys_and_values_example()


def run_set_means_hashset_class():
    # Create an instance of Set_Means_HashSet class (the __init__ method will be automatically called)
    set_examples = Set_Means_HashSet()

    # Access the example_set from __init__ method
    print("Instance Variable - example_set:", set_examples.example_set)

    # Call the functions to demonstrate different set examples
    set_examples.set_example()
    set_examples.set_methods_example()
    set_examples.set_operations_example()


def run_list_means_array_class():
    list_examples = List_Means_Array()

    # Access the example_list from __init__ method
    print("Instance Variable - example_list:", list_examples.example_list)

    # Call the functions to demonstrate different list examples
    list_examples.integer_example()
    list_examples.float_example()
    list_examples.string_example()
    list_examples.mixed_list_example()
    list_examples.nested_list_example()
    list_examples.list_comprehension_example()
    list_examples.list_slices_example()
    list_examples.list_methods_example()
    list_examples.list_concatenation_example()
    list_examples.list_length_example()



def run_python_variables_class():
    # Create an instance of the PythonVariables class (the __init__ method will be automatically called)

    python_vars = PythonVariables(1.1, y="Python Instance")

    # Access the instance variable from __init__ method
    print(python_vars.instance_var)

    # Call the functions to demonstrate each variable type
    python_vars.integer_example()
    python_vars.float_example()
    python_vars.string_example()
    python_vars.boolean_example()
    python_vars.list_example()
    python_vars.tuple_example()
    python_vars.set_example()
    python_vars.dictionary_example()
    python_vars.none_example()


if __name__ == "__main__":
    main()
