import os

# Specify the directory where the files are located
directory = 'xml/raw'

# Iterate over each file in the directory
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)  # Get the full path to the file
    os.chmod(file_path, 0o777)  # Change the permissions to 777 (rwx for all)
    print(f"Permissions changed for {file}")

directory = 'csv/raw'

# Iterate over each file in the directory
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)  # Get the full path to the file
    os.chmod(file_path, 0o777)  # Change the permissions to 777 (rwx for all)
    print(f"Permissions changed for {file}")