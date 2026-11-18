# File and Folder Manager

A simple menu-driven command-line tool written in Python for managing files and folders. It supports full CRUD operations (Create, Read, Update, Delete) on both files and folders, using only the Python standard library.

## Features

| Option | Action | What it does |
|--------|--------|--------------|
| 1 | Create a folder | Creates a new folder with the name you enter |
| 2 | Read files and folders | Lists everything in the current directory, including subfolders |
| 3 | Update the folder | Renames an existing folder |
| 4 | Delete the folder | Deletes a folder and all of its contents |
| 5 | Create a file | Creates a new file and writes text into it |
| 6 | Read a file | Prints the contents of a file |
| 7 | Update a file | Rename the file, append text, or overwrite its content |
| 8 | Delete a file | Deletes a file |
| 0 | Exit | Quits the program |

## Requirements

- Python 3.6 or higher
- No external packages needed (uses `pathlib` and `shutil` from the standard library)

## How to Run

1. Save the code as `main.py`.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

4. Type a number from the menu and press Enter.

## Example Session

```
-----Options : -----
1. Create a folder
2. Read files and folders
3. Update the Folder
4. Delete the folder
5. Create a file
6. Read a file
7. Update a file
8. Delete a file
0. Exit
Please Choose your input :- 1
Please tell your folder name :- notes
Folder created successfully
```

## How It Works

- **`pathlib.Path`** is used to check whether files or folders exist and to rename or delete them.
- **`shutil.rmtree`** is used to delete a folder together with everything inside it.
- Each operation is its own function, wrapped in `try/except` so errors are printed instead of crashing the program.
- A `while True` loop shows the menu repeatedly until you choose `0`.

## Warnings

- **Deleting a folder is permanent.** `shutil.rmtree` removes the folder and everything inside it without moving it to the Recycle Bin.
- **Deleting a file is permanent** as well.
- All paths are relative to the directory you run the script from.

## Known Issues and Possible Improvements

- Entering a non-number at the main menu causes a `ValueError` crash. Wrap `int(input(...))` in a `try/except`.
- The main menu uses separate `if` statements. Using `if / elif / else` would be cleaner and allow an "Invalid option" message.
- In `delete_file()`, `p.exists` is missing its parentheses and should be `p.exists()`.
- `read_file_folder()` uses `Path(" ")` (with a space). Use `Path(".")` to refer to the current directory reliably.
- `rglob('*')` lists all nested items. Use `iterdir()` if you only want the top level.
- The unused `import os` can be removed.
- Appending to a file always adds a leading space (`" " + data`). A newline may be more useful.

## Project Structure

```
File and Folder Handling/
├── main.py
└── README.md
```

## License

Free to use for learning and personal projects.
