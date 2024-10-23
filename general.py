import os

# function creates a directory if it does not exist
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# function writes data to the file path
# opens the file in write mode ('w'). The 'with' statement ensures the file is closed after writing
def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
