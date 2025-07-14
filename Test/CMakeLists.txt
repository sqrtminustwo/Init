# Project name + cmake version
cmake_minimum_required(VERSION 3.15)
project(ProjectName)

# Set version
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# All .cpp files
add_executable(UnsignedBigInteger
    src/main.cpp
)

# To use "Name.h" instead of "src/BlaBla/Name.h"
target_include_directories(ProjectName PRIVATE src/Folder)
# To use experimental C++23 features
target_link_libraries(ProjectName PRIVATE stdc++exp)