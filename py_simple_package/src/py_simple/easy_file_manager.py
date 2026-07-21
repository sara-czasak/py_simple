import os


VALID_EXTENSIONS = ['txt', 'md', 'log', 'csv']


class InvalidExtension(Exception):
    """Exception raised for invalid extension"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def make_blank_file(filename: str, file_extension: str):
    """
        Creates a blank file in current working directory.

        Args:
            filename (str): The name of the file to be created.
            file_extension (str): The extension of the file to be created without including '.'. Allowed extensions are: ['txt', 'csv', 'md', 'log']

        Example:
            make_blank_file("new_file", "txt")
        """
    if file_extension.lower() in VALID_EXTENSIONS:
        file = f"{filename}.{file_extension.lower()}"
        with open(file, 'w', encoding='utf-8'):
            pass
    else:
        raise InvalidExtension(f"\n'{file_extension}' is not a valid extension. Please enter a valid extension and try again.\nVALID EXTENSIONS: {VALID_EXTENSIONS}")


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
    if ext in VALID_EXTENSIONS:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(line + '\n')
    else:
        raise InvalidExtension(f"\n'{ext}' is not a valid extension. Please enter a valid extension and try again.\nVALID EXTENSIONS: {VALID_EXTENSIONS}")
