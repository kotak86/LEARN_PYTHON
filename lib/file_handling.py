import json
import yaml

class FileHandling:
    def read_log_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print(f"File not found: {file_path}")

    def read_json_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                print("JSON File Contents:")
                print(data)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Invalid JSON format in the file: {file_path}")

    def read_yaml_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)
                print("YAML File Contents:")
                print(data)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except yaml.YAMLError:
            print(f"Invalid YAML format in the file: {file_path}")

    def write_log_file(self, file_path, content):
        with open(file_path, 'a') as file:
            for l in content:
                file.write(l + "\n")
        print(f"Content successfully written to the log file: {file_path}")

    def write_json_file(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully written to the JSON file: {file_path}")

    def write_yaml_file(self, file_path, data):
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
        print(f"Data successfully written to the YAML file: {file_path}")

# Run this script to define the class and its methods.
if __name__ == "__main__":
    pass
