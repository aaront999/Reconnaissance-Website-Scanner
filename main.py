import os

# creates a directory if it does not exist
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# writes data to the file path
def write_file(file_path, data):
    file = write_file(file_path, 'w')
    file.write(data)
    file.close()