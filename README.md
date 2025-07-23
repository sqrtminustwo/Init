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

Project structure is configured via [`resources/configs`](resources/configs). Example for a C++ project:

```json
{
    "dirs": [
        "src",
        "include", 
        "tests",
        ".vscode"
    ],
    "files_root": "c++",
    "files": [
        {
            "name": "^.*\\.cpp$",
            "src_path": ["src"],
            "dst_path": ["src"]
        },
        {
            "name": "^test.*\\.cpp$",
            "src_path": ["tests"],
            "dst_path": ["tests"]
        },
        {
            "name": "^launch\\.json$",
            "src_path": ["configs"],
            "dst_path": [".vscode"]
        },
        {
            "name": "^CMakePresets\\.json$",
            "src_path": ["configs"],
            "dst_path": []
        },
        {
            "name": "^CMakeLists\\.txt$",
            "src_path": ["configs"],
            "dst_path": []
        },
        {
            "name": "^.*$",
            "src_path": ["github"],
            "dst_path": []
        }
    ]
}
```

- **`dirs`**: Directories to create in the project root.

- **`files_root`**: The folder within `resources/files` that contains language-specific files (e.g. [`resources/files/c++`](resources/files/c++)).

- **`files`**: Files to copy from `resources/files/<files_root>` to the project:
  - **`name`**: Regex pattern to match filenames in `resources/files/<files_root>/<src_path>`.
    > [!TIP]
    > Use `^filename$` for exact matches and escape dots with `\\.`
  
  - **`src_path`**: Source subdirectory within the language folder (empty array `[]` for root).
  
  - **`dst_path`**: Destination path in the project (empty array `[]` for root).

---
