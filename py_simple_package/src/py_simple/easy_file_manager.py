"""
easy_file_manager is meant to simplify working with files.
"""

import os


VALID_EXTENSIONS = ['txt', 'md', 'log', 'csv']


class InvalidExtension(Exception):
    """Exception raised for invalid extension"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def _is_valid_extension(extension):
    """Check if extension is valid"""
    return extension in VALID_EXTENSIONS


def is_file_there(filename: str):
    """
        Check if file exists in current working directory.

        Args:
            filename (str): Name of the file to be checked.

        Returns:
            bool: True if file exists in current working directory or False if not.

        Example:
            is_file_there("new_file.txt")
        """
    return os.path.isfile(filename)


def make_blank_file(filename: str, file_extension: str):
    """
        Creates a blank file in current working directory. If file already exists, nothing is done.

        Args:
            filename (str): The name of the file to be created.
            file_extension (str): The extension of the file to be created without including '.'.
            Allowed extensions are: ['txt', 'csv', 'md', 'log']

        Example:
            make_blank_file("new_file", "txt")
        """
    if _is_valid_extension(file_extension.lower()):
        file = f"{filename}.{file_extension.lower()}"
        if is_file_there(file):
            print(f"File {file} already exists in current working directory.")
        else:
            with open(file, 'w', encoding='utf-8'):
                pass
    else:
        raise InvalidExtension(f"""
        \n'{file_extension}' is not a valid extension.
        Please enter a valid extension and try again.
        \nVALID EXTENSIONS: {VALID_EXTENSIONS}""")


def add_a_line(filename: str, line: str):
    """
        Add line to existing file.
        If file does not exist, create it.

        Args:
            filename (str): File to write to. Allowed extensions are: ['txt', 'csv', 'md', 'log']
            line (str): Line to write.

        Example:
            add_a_line("new_file.txt", "hello world!")
        """
    ext = filename.split('.')[-1].lower()
    if _is_valid_extension(ext):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(line + '\n')
    else:
        raise InvalidExtension(f"""\n'{ext}' is not a valid extension.
        Please enter a valid extension and try again.
        \nVALID EXTENSIONS: {VALID_EXTENSIONS}""")


def read_file_to_list(filename: str):
    """
        Reads lines of existing file to list.

        Args:
            filename (str): File to read from. Allowed extensions are: ['txt', 'csv', 'md', 'log']

        Returns:
            list: List of lines.

        Example:
            read_file_to_list("new_file.txt")
        """
    ext = filename.split('.')[-1].lower()
    if _is_valid_extension(ext):
        clean_lines = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for line in lines:
                clean_lines.append(line.strip())
            return clean_lines
        except FileNotFoundError:
            print(f"\nFile '{filename}' not found.")
            return []
    else:
        raise InvalidExtension(
            f""""\n'{ext}' is not a valid extension.
            Please enter a valid extension and try again.\n
            VALID EXTENSIONS: {VALID_EXTENSIONS}""")


def remove_file(filename: str):
    """
        Removes file from current working directory.

        Args:
            filename (str): File to delete. Allowed extensions are: ['txt', 'csv', 'md', 'log']

        Example:
            remove_file("new_file.txt")
        """
    ext = filename.split('.')[-1].lower()
    if _is_valid_extension(ext):
        if is_file_there(filename):
            os.remove(filename)
        else:
            print(f"File {filename} does not exist!")
    else:
        raise InvalidExtension(f"""\n'{ext}' is not a valid extension.
        Please enter a valid extension and try again.\n
        VALID EXTENSIONS: {VALID_EXTENSIONS}""")


def rename_file(old_name: str, new_name: str):
    """
        Rename file in the current working directory.

        Args:
            old_name (str): File to rename. Allowed extensions are: ['txt', 'csv', 'md', 'log']
            new_name (str): New name for file. Allowed extensions are: ['txt', 'csv', 'md', 'log']

        Example:
            rename_file("old_name.txt", "new_name.txt")
        """
    ext_old = old_name.split('.')[-1].lower()
    ext_new = new_name.split('.')[-1].lower()
    if _is_valid_extension(ext_old) and _is_valid_extension(ext_new):
        if is_file_there(old_name):
            if not is_file_there(new_name):
                os.rename(old_name, new_name)
            else:
                print(f"File '{new_name}' already exists in current working directory.")
        else:
            print(f"File {old_name} does not exist in current working directory.")
    else:
        raise InvalidExtension(
            f"""\n'{ext_old}' or '{ext_new}' is not a valid extension.
            Please enter a valid extension and try again.
            \nVALID EXTENSIONS: {VALID_EXTENSIONS}""")
