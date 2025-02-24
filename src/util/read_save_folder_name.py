'''This module lists all the sub-folders in a folder and saves them in a csv file.   This csv file is used to create the face embeddings for all the faces in the dataset/train directory.'''

import os 
from imutils import paths

# Create a set to store the sub-folder names
sub_folder_names=set()

def read_save_folder_name(dir_path, csv_file_path):
    '''Reads all the sub-folder names in a folder and saves them in a csv file
    
    Args:
        dir_path: Path to the folder
        csv_file_path: Path to the csv file
    
    Returns:
        None
    '''
    global sub_folder_names

    # Get all the sub-folder names in the folder
    imagePaths = list(paths.list_images(dir_path))

    for img_path in imagePaths:
        # Get the sub-folder name
        sub_folder_name=img_path.rsplit('/', 1)[0]
        sub_folder_name=sub_folder_name.rsplit('/', 1)[1]
        sub_folder_names.add(sub_folder_name)

    # Save the sub-folder names in a csv file
    with open(csv_file_path, 'w') as f:
        # Write the header
        f.write('name, \n')
        for item in sub_folder_names:
            f.write(f'{item}, \n')


read_save_folder_name('dataset/train/pics_dlib_glb/', 'reports/dataset_names.csv')

