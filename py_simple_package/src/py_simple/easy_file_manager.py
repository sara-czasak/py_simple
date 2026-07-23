"""
easy_file_manager is meant to simplify working with files.
"""

import os
import shutil


VALID_EXTENSIONS = ['txt', 'md', 'log', 'csv']


class InvalidExtension(Exception):
    """Exception raised for invalid extension"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def _is_valid_extension(extension):
    """Check if extension is valid"""
    return extension in VALID_EXTENSIONS


def _get_extension(filename: str) -> str:
    """Extract the lowercased extension from a filename."""
    return filename.split('.')[-1].lower()


def is_file_there(filename: str) -> bool:
    """
    Check if file exists in current working directory.

    Args:
        filename (str): Name of the file to be checked.

    Returns:
        bool: True if file exists, False otherwise.

    Example:
        is_file_there("new_file.txt")
    """
    return os.path.isfile(filename)


def make_blank_file(filename: str, file_extension: str):
    """
    Creates a blank file in current working directory.
    If file already exists, nothing is done.

    Args:
        filename (str): The name of the file to be created.
        file_extension (str): The extension without '.'.
            Allowed: ['txt', 'csv', 'md', 'log']

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
        raise InvalidExtension(
            f"\n'{file_extension}' is not a valid extension.\n"
            f"Please enter a valid extension and try again.\n"
            f"\nVALID EXTENSIONS: {VALID_EXTENSIONS}"
        )


def add_a_line(filename: str, line: str):
    """
    Add line to existing file. If file does not exist, create it.

    Args:
        filename (str): File to write to.
        line (str): Line to write.

    Example:
        add_a_line("new_file.txt", "hello world!")
    """
    ext = _get_extension(filename)
    if _is_valid_extension(ext):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(line + '\n')
    else:
        raise InvalidExtension(
            f"\n'{ext}' is not a valid extension.\n"
            f"Please enter a valid extension and try again.\n"
            f"\nVALID EXTENSIONS: {VALID_EXTENSIONS}"
        )


def read_file_to_list(filename: str) -> list:
    """
    Reads lines of existing file to list.

    Args:
        filename (str): File to read from.

    Returns:
        list: List of lines.

    Example:
        read_file_to_list("new_file.txt")
    """
    ext = _get_extension(filename)
    if _is_valid_extension(ext):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"\nFile '{filename}' not found.")
            return []
    else:
        raise InvalidExtension(
            f"\n'{ext}' is not a valid extension.\n"
            f"Please enter a valid extension and try again.\n"
            f"\nVALID EXTENSIONS: {VALID_EXTENSIONS}"
        )


def remove_file(filename: str):
    """
    Removes file from current working directory.

    Args:
        filename (str): File to delete.

    Example:
        remove_file("new_file.txt")
    """
    ext = _get_extension(filename)
    if _is_valid_extension(ext):
        if is_file_there(filename):
            os.remove(filename)
        else:
            print(f"File {filename} does not exist!")
    else:
        raise InvalidExtension(
            f"\n'{ext}' is not a valid extension.\n"
            f"Please enter a valid extension and try again.\n"
            f"\nVALID EXTENSIONS: {VALID_EXTENSIONS}"
        )


def rename_file(old_name: str, new_name: str):
    """
    Rename file in the current working directory.

    Args:
        old_name (str): Current filename.
        new_name (str): New filename.

    Example:
        rename_file("old_name.txt", "new_name.txt")
    """
    ext_old = _get_extension(old_name)
    ext_new = _get_extension(new_name)
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
            f"\n'{ext_old}' or '{ext_new}' is not a valid extension.\n"
            f"Please enter a valid extension and try again.\n"
            f"\nVALID EXTENSIONS: {VALID_EXTENSIONS}"
        )


def list_files(extension: str = None) -> list:
    """
    List files in the current working directory that have valid extensions.
    Optionally filter by a specific extension.

    Args:
        extension (str, optional): Filter by extension (e.g., 'txt').
            If None, all valid extension files are listed.

    Returns:
        list: Sorted list of filenames matching the filter.

    Example:
        list_files()
        list_files("txt")
    """
    if extension is not None and not _is_valid_extension(extension.lower()):
        raise InvalidExtension(
            f"\n'{extension}' is not a valid extension.\n"
            f"\nVALID EXTENSIONS: {VALID_EXTENSIONS}"
        )

    matches = []
    for fname in os.listdir('.'):
        if os.path.isfile(fname):
            ext = _get_extension(fname)
            if _is_valid_extension(ext):
                if extension is None or ext == extension.lower():
                    matches.append(fname)
    return sorted(matches)


def copy_file(source: str, destination: str):
    """
    Copy a file to a new location or name.

    Args:
        source (str): File to copy.
        destination (str): Destination path or filename.

    Example:
        copy_file("notes.txt", "notes_backup.txt")
    """
    ext_src = _get_extension(source)
    ext_dst = _get_extension(destination)
    if not _is_valid_extension(ext_src):
        raise InvalidExtension(
            f"\n'{ext_src}' is not a valid extension.\n"
            f"\nVALID EXTENSIONS: {VALID_EXTENSIONS}"
        )
    if not _is_valid_extension(ext_dst):
        raise InvalidExtension(
            f"\n'{ext_dst}' is not a valid extension.\n"
            f"\nVALID EXTENSIONS: {VALID_EXTENSIONS}"
        )
    if not is_file_there(source):
        print(f"File '{source}' does not exist.")
        return
    if is_file_there(destination):
        print(f"File '{destination}' already exists — not overwriting.")
        return
    shutil.copy2(source, destination)
