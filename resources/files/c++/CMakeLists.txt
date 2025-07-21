# Set CMake version and project name
cmake_minimum_required(VERSION 3.20)  # 3.20+ is safer for modern features
# Set up project name
project(CGuide LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)  # Portable clean standard C++

# Collect source and header files
file(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS src/*.cpp)
file(GLOB_RECURSE HEADERS CONFIGURE_DEPENDS include/*.h)

# Create the executable
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

# Standard include directories (prefer include/ over src/)
target_include_directories(${PROJECT_NAME}
    PRIVATE 
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

# Recommended compiler warnings (portable & strict)
if (MSVC)
    target_compile_options(${PROJECT_NAME} PRIVATE /W4 /permissive-)
else()
    target_compile_options(${PROJECT_NAME} PRIVATE -Wall -Wextra -Wpedantic -Wconversion)
endif()

# Optional: enable link-time optimization if supported
include(CheckIPOSupported)
check_ipo_supported(RESULT result)
if(result)
    set_target_properties(${PROJECT_NAME} PROPERTIES INTERPROCEDURAL_OPTIMIZATION TRUE)
endif()

# For google test
enable_testing()
find_package(GTest REQUIRED)
target_link_libraries(CGuide GTest::gtest GTest::gtest_main pthread)

# Optional: link with stdc++exp only if truly needed (almost never in 2025 compilers)
# target_link_libraries(${PROJECT_NAME} PRIVATE stdc++exp)