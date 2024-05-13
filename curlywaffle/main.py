"""Module which checks a proposed file path is unique. If unique, returns the proposed file path. If not, concatenates '-1' to the proposed file path, and increments the integer until unique."""

import os


def get_unique_file_path(proposed_file_path_with_ext):
    """If unique, returns the proposed file path. If not, concatenates -{duplicate_number}, incrementing duplicate number until unique."""
    if not os.path.isfile(proposed_file_path_with_ext):
        return proposed_file_path_with_ext

    split = os.path.splitext(proposed_file_path_with_ext)
    file_path = split[0]
    ext = split[1]
    checking_for_duplicates = True
    duplicate_count = 0

    while checking_for_duplicates:
        duplicate_count += 1
        checking_for_duplicates = os.path.isfile(
            f'{file_path}-{duplicate_count}{ext}')

    return f'{file_path}-{duplicate_count}{ext}'
