# CppInit

A simple Python script to initialize C++ project templates.

---

## Installation

### Windows

1. Clone the repository:
```bash
git clone https://github.com/sqrtminustwo/CppInit
```

2. (Optional) Create a folder for custom scripts and add it to your PATH:
```
System > Advanced System Settings > Environment Variables > PATH
```

3. Create `cppinit.bat` inside your scripts folder with the following content:  
*(Replace `your\path\to` with the actual path where `cppinit.py` is located)*

```bat
@echo off
python "your\path\to\cppinit.py" %*
```

> [!CAUTION]
> Do not remove `%*`, it's required to forward arguments.

#### Usage
```bash
cppinit ProjectName
```


### Linux (Ubuntu Example)

1. Clone the repository:
```bash
git clone https://github.com/sqrtminustwo/CppInit
```

2. Add the following alias to your `.bashrc`:
```bash
alias cppinit="python /your/path/to/cppinit.py"
```

#### Usage
```bash
cppinit ProjectName
```

---

## Configuration

Project structure is configured via [`resources/config.json`](resources/config.json). Example:

```json
{
    "dirs": [
        "src",
        "resources"
    ],
    "files": [
        {
            "name": "main.cpp",
            "path": ["src"]
        },
        {
            "name": "CMakeLists.txt",
            "path": []
        }
    ]
}
```

- `dirs`: Directories to create in the project root.
- `files`: Files to copy from `resources/files`.  
  - `name`: File name in `resources/files`
  - `path`: Path inside the project (empty array `[]` for root directory).

---
