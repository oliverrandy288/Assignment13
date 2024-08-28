import os

def list_directory_contents(path):
    try:
        # List all files and subdirectories in the given path
        with os.scandir(path) as entries:
            print(f"Contents of '{path}':")
            for entry in entries:
                if entry.is_dir():
                    print(f"[DIR] {entry.name}")
                elif entry.is_file():
                    print(f"[FILE] {entry.name}")
                else:
                    print(f"[OTHER] {entry.name}")
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Prompt the user for the directory path
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
