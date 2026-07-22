# Py_simple 🚀
**Making Python feel like plain English.**

I created `Py_simple` as a wrapper package to help beginners and developers perform common tasks using simple, intuitive functions. My goal is to remove the need for memorizing complex flags or writing repetitive boilerplate code.

---

## 🛠️ Module Menu
*Select a module below to see how to use it!*

<details>
<summary><span style="font-size: 1.75em; font-weight: 800;">📂 Easy File Manager</span></summary>

## 📂 Easy File Manager

The `easy_file_manager` module simplifies how you interact with files in your current working directory.

### Supported File Types
To keep things safe and simple, this module currently supports:
`txt`, `csv`, `md`, `log`

### Quick Start
```python
from py_simple import make_blank_file, add_a_line, read_file_to_list

# 1. Create a new file without 'with open()'
make_blank_file("my_notes", "txt")

# 2. Add a line of text (handles newlines automatically!)
add_a_line("my_notes.txt", "Learning Python is fun!")

# 3. Read a file directly into a clean list
notes = read_file_to_list("my_notes.txt")
print(notes) # Output: ['Learning Python is fun!']
```

### API Reference

#### `make_blank_file(filename, extension)`
Creates an empty file. If the file already exists, it warns you instead of overwriting it.

#### `is_file_there(filename)`
Returns `True` if a file exists, `False` if it doesn't.

#### `add_a_line(filename, line)`
Appends a single line to a file. If the file doesn't exist, it creates it for you.

#### `read_file_to_list(filename)`
Opens a file and returns every line as an item in a list, with whitespace stripped away.

#### `remove_file(filename)`
Safely deletes a file after checking if it exists.

#### `rename_file(old_name, new_name)`
Safely changes a filename. It won't let you rename a file if the new name is already taken!
</details>

<details>
<summary><span style="font-size: 1.75em; font-weight: 800;">🕰️ Easy Date Formatter</span></summary>

## 🕰️ Easy Date Formatter

The `easy_date_formatter` module takes the guesswork out of Python's `datetime` module. No more memorizing `%d`, `%m`, or `%Y` codes!

### Quick Start
```python
from py_simple import get_pretty_date, past_dd_mm_yyyy

# 1. Get a human-readable date
print(get_pretty_date()) 
# Output: Monday, July 20, 2026

# 2. Get a date from 7 days ago in a specific format
last_week = past_dd_mm_yyyy(7)
print(last_week) 
# Output: 13-07-2026
```

### API Reference
All functions return a **string**. Functions starting with `past_` require a `num_days_ago` (integer) argument.

#### Human-Friendly Dates
- `get_pretty_date()`: Returns `Weekday, Month Day, Year`.
- `get_past_pretty_date(days)`: Returns a past date in the same pretty format.

#### Hyphenated Formats (DD-MM-YYYY or MM-DD-YYYY)
- `dd_mm_yyyy()` / `past_dd_mm_yyyy(days)`
- `mm_dd_yyyy()` / `past_mm_dd_yyyy(days)`

#### Slashed Formats (DD/MM/YYYY or MM/DD/YYYY)
- `slash_dd_mm_yyyy()` / `past_slash_dd_mm_yyyy(days)`
- `slash_mm_dd_yyyy()` / `past_slash_mm_dd_yyyy(days)`
- 
</details>

---


## 🤝 Contributing
I would love to have your help in making Python simpler for everyone! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to suggest new features or report bugs.

## ⚖️ License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it! See the [LICENSE](LICENSE.md) file for the full legal text.
