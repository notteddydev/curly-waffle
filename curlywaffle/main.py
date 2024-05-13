"""Module which checks a proposed file path is unique. If unique, returns the proposed file path. If not, concatenates '-1' to the proposed file path, and increments the integer until unique."""

import os


def get_unique_file_path(proposed_file_path, file_extension):
    """If unique, returns the proposed file path. If not, concatenates -{duplicate_number} until unique."""
    if not os.path.isfile(f'{proposed_file_path}{file_extension}'):
        return f'{proposed_file_path}{file_extension}'

    checking_for_duplicates = True
    duplicate_count = 0

    while checking_for_duplicates:
        duplicate_count += 1
        checking_for_duplicates = os.path.isfile(
            f'{proposed_file_path}-{duplicate_count}{file_extension}')

    return f'{proposed_file_path}-{duplicate_count}{file_extension}'
