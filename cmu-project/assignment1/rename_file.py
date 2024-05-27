import os # import the os module which has functionality of reading or writing to the filesystem

def replace_spaces_in_filenames(root_dir):   # defining the function
    for dirpath, dirnames, filenames in os.walk(root_dir): # os.walk function traverse a dir tree and generate the file names in the directory tree
        for filename in filenames:
            if ' ' in filename:
                old_file_path = os.path.join(dirpath, filename) # submodule os.path provides functions for interacting with file paths.
                new_filename = filename.replace(' ', '_')
                new_file_path = os.path.join(dirpath, new_filename)
                
                # Ensure new filename does not already exist
                if not os.path.exists(new_file_path):
                    os.rename(old_file_path, new_file_path)
                    print(f'Renamed: "{old_file_path}" to "{new_file_path}"')
                else:
                    print(f'Skipping: "{new_file_path}" already exists.')

# Example usage
root_directory = '/path/to/your/directory'  # giving the path to the root directory. 
replace_spaces_in_filenames(root_directory) # calling the defined function

# To run the script, you can execute it from your command line by doing : python rename_files.py
# NB: Ensure you have the necessary permissions to read and write files in the directory
