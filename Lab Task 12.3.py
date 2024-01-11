class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file_content(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.read()
                print(f"File content: {data}")
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage:
file_reader = FileReader('example.txt')
file_reader.read_file_content()
