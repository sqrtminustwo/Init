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
        "resources"
    ],
    "files_root": "c++",
    "files": [
        {
            "name": "main.cpp"
            "path": ["src"],
        },
        {
            "name": "CMakeLists.txt",
            "path": []
        },
        {
            "name": ".gitignore",
            "path": []
        }
    ]
}
```

- `dirs`: Directories to create in the project root.
- `files_root`: [`resources/files`](resources/files) can have multiple folders with any name. The name of the folder with files for the project (based on language) should be specified here.
- `files`: Files to copy from `resources/files/files_root`.  
  - `name`: File name in `resources/files/files_root`
  - `path`: Path inside the project (empty array `[]` for the root directory).

---
