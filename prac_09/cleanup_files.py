"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)
            print(new_name)

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()

            # os.chdir('..')  # .. means "up" one directory
            # for dir_name, subdir_list, file_list in os.walk('.'):
            #     print("In", dir_name)
            #     print("\tcontains subdirectories:", subdir_list)
            #     print("\tand files:", file_list)
    os.chdir('..')
    os.chdir('..')
    os.chdir('FilesToSort')
    print(os.listdir('.'))
    # for filename in os.listdir('.'):
    #     # ignore directories, just process files
    #     if not os.path.isdir(filename):
    #         create_directory(filename)
    extension_dictionary = {}
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            get_directory(filename, extension_dictionary)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    # filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    # new_name = ""
    # TODO: step-by-step, consider the problem cases and solve them
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    name = []
    i = 0
    for char in new_name:
        name.append(char)
        if name[i] == "_":
            char = new_name[i + 1].upper()
        i += 1
    return new_name


def create_directory(filename):
    extension = filename.split('.')[1]
    if not os.path.isdir(extension):
        os.mkdir(extension)
    shutil.move(filename, extension)


def get_directory(filename, extension_dictionary):
    extension = filename.split('.')[1]
    if extension not in extension_dictionary.values():
        new_directory = input("What category would you like to sort {} files into? ".format(extension))
    # if not new_directory in extension_dictionary:
        if not os.path.isdir(new_directory):
            os.mkdir(new_directory)
        extension_dictionary[new_directory] = extension
    # shutil.move(filename, new_directory)
    print(extension_dictionary)


main()
