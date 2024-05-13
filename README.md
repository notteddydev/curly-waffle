# Python package for providing a unique file path, based on a proposed file path.

If file path argument is unique, the same file path will be returned.

If file path argument is not unique, '-1' will be concatenated onto the file name.

If with '-1' concatenated it is still not unique, the 1 will be incrememnted until a unique file name is encountered.

Example:
```bash
/path/to/dir/unique_file_name.pdf
/path/to/dir/unique_file_name-1.pdf
/path/to/dir/unique_file_name-2.pdf
/path/to/dir/unique_file_name-3.pdf
/path/to/dir/unique_file_name-4.pdf
/path/to/dir/unique_file_name-5.pdf
/path/to/dir/unique_file_name-6.pdf
```