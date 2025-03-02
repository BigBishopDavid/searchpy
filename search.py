import os

def search_string_in_files(directory, search_string):
    matching_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    if search_string in f.read():
                        matching_files.append(file_path)
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")
    
    return matching_files

# Example usage
directory_to_search = r"C:\xampp\htdocs\application"  # Change this to your target directory
string_to_find = "purchase_code"  # Change this to your target string

matching_files = search_string_in_files(directory_to_search, string_to_find)

if matching_files:
    print("Files containing the string:")
    for file in matching_files:
        print(file)
else:
    print("No matching files found.")
