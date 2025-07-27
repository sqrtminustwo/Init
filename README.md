# Init

A simple Python script to initialize project templates.

---

## Installation

### Windows

1. Clone the repository:
```bash
git clone https://github.com/sqrtminustwo/Init
```

2. (Optional) Create a folder for custom scripts and add it to your `PATH`:  
`System > Advanced System Settings > Environment Variables > PATH`

3. Create `p_init.bat` inside your scripts folder with the following content:  
*(Replace `your\path\to` with the actual path where `p_init.py` is located)*

```bat
@echo off
python "your\path\to\p_init.py" %*
```

Or with a predefined config:
```bat
@echo off
python "your\path\to\p_init.py" "configname" %*
```

> [!CAUTION]
> Do not remove `%*`. It is required to forward arguments (`%*` stands for a variable number of arguments in case the number changes in the future).

#### Usage
```bash
p_init ConfigName ProjectName
```

Or if you initialized the `.bat` with a config:
```bash
cppinit ProjectName
```

---

### Linux (Ubuntu Example)

1. Clone the repository:
```bash
git clone https://github.com/sqrtminustwo/Init
```

2. Add the following alias to your `.bashrc`:
```bash
alias p_init="python /your/path/to/p_init.py"
```

Or with a predefined config:
```bash
alias cppinit="python /your/path/to/p_init.py configname"
```

#### Usage
```bash
p_init ConfigName ProjectName
```

Or if you initialized the alias with a config:
```bash
cppinit ProjectName
```

---

## Configuration

Project structure is configured via [`resources/configs`](resources/configs). Example for a C++ project ([`full config from example`](resources/configs/cpp_glfw_win.json)):

```json
{
  "files_root": "c++",

  "structure": {
    "default": {
      "dirs": [
        ["src"],
        ["include"],
        ["tests"]
      ],
      "files": [
        {
          "src_name": "main_glfw.cpp",
          "dst_name": "main.cpp",
          "src_path": ["GLFW", "src"],
          "dst_path": ["src"]
        },
        {
          "name": "^test.*\\.cpp$",
          "src_path": ["tests"],
          "dst_path": ["tests"]
        },
        {
          "name": "^CMakePresets\\.json$",
          "src_path": ["configs"],
          "dst_path": []
        },
        {
          "src_name": "GLFW_CMakeLists.txt",
          "dst_name": "CMakeLists.txt",
          "src_path": ["configs"],
          "dst_path": []
        }
      ]
    },

    "glfw": {
      "dirs": [
        ["external", "include", "GLFW"],
        ["external", "lib"]
      ],
      "files": [
        {
          "name": "^.*$",
          "src_path": ["GLFW", "include"],
          "dst_path": ["external", "include", "GLFW"]
        },
        {
          "name": "^libglfw3\\.a$",
          "src_path": ["GLFW", "lib"],
          "dst_path": ["external", "lib"]
        }
      ]
    }
  }
}
```

### Files

- **`files_root`**: Subfolder inside `resources/files` that holds language-specific files  
  _(e.g., `c++` in [`resources/files/c++`](resources/files/c++))_

### Structure

Structure can contain a variable number of keys, and you can choose the names yourself (the names of the keys inside the structure are ignored). The key-object pairs in the structure are created purely for better readability and organization of the config.

- **`dirs`**: List of directories (as paths) to create in the project root.

- **`files`**: Describes how files are copied from `resources/files/<files_root>` to the project.

  ### File Matching and Naming:
  - **`name`**: Regular expression to match filenames inside `resources/files/<files_root>/<src_path>`.  
    > Use `^filename$` for exact matches and escape dots as `\\.`

  - **`src_name`**: Exact name of a file in `resources/files/<files_root>/<src_path>`.  
  - **`dst_name`**: Name to use for the copied file in the destination path.  
    > If `name` is specified, `src_name` and `dst_name` are ignored.  
    > `src_name` and `dst_name` do not support regex.

  ### File Paths:
  - **`src_path`**: Path (as an array of folders) under the language folder to find the source file.  
    > Use an empty array `[]` for the root.

  - **`dst_path`**: Path (as an array of folders) within the project where the file will be copied.  
    > Use an empty array `[]` to copy into the project root.

---
