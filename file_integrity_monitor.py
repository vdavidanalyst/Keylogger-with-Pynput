import hashlib
import os

A = 'collect new baseline?'
B = 'Begin monitoring files with saved baseline?'

print('What would you like to do?')
response = input('Enter A or B: ')

if response.upper() == 'A':
    # Calculate hash from the target files and store in baseline.txt
    directory = '/path/to/directory'  # Replace with the directory path
    hashes = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
                hash_object = hashlib.sha256(content)
                file_hash = hash_object.hexdigest()
                hashes.append(file_hash)

    with open('baseline.txt', 'w') as f:
        for file_hash in hashes:
            f.write(file_hash + '\n')

    print('Baseline created successfully.')

elif response.upper() == 'B':
    # Begin monitoring of files with saved baseline.txt
    with open('baseline.txt', 'r') as f:
        baseline_hashes = [line.strip() for line in f]

    directory = '/path/to/directory'  # Replace with the directory path

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
                hash_object = hashlib.sha256(content)
                file_hash = hash_object.hexdigest()

            if file_hash not in baseline_hashes:
                print(f'File {file_path} has been modified.')

else:
    print('Invalid response. Please enter A or B.')

''' 
The os module is imported to list the files in the directory and construct the file paths.
The directory variable is set to the path of the directory you want to monitor.
When selecting option A, the code iterates over all the files in the directory, calculates their hashes, and stores them in baseline.txt.
When selecting option B, the code reads the baseline hashes from baseline.txt and compares them with the current hashes of the files in the directory. If a file's hash is different from the baseline, it prints a message indicating that the file has been modified.
Make sure to replace '/path/to/directory' with the actual path of the directory you want to monitor.
Note that this code assumes that the files in the directory are the ones you want to monitor. If there are subdirectories within the target directory and you want to include files from those subdirectories as well, you may need to modify the code accordingly to traverse the directory recursively.
'''