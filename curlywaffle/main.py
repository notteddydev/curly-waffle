"""Module which checks a proposed file path is unique. If unique, returns the proposed file path. If not, concatenates '-1' to the proposed file path, and increments the integer until unique."""

import os


def get_unique_file_path(dest):
    """If unique, returns the proposed file path. If not, concatenates -{duplicate_number}, incrementing duplicate number until unique."""
    file_path, ext = os.path.splitext(dest)
    duplicate_count = 1

    while os.path.exists(dest):
        dest = f'{file_path}-{duplicate_count}{ext}'
        duplicate_count += 1

    return dest
