cmake_minimum_required (VERSION 2.8) 

project (pipeline_evaluator) 

# unit test library include
set(CMAKE_CXX_FLAGS "-Wall -g -std=c++0x -O2")

# unit test executable
add_executable(a.out evaluator.cpp)
add_library(pipeline SHARED evaluator.cpp)

if(UNIX)
add_custom_target(useful COMMAND rm -r CMakeCache.txt CMakeFiles cmake_install.cmake)
endif()

# copy input files to build/input directory
file(GLOB input_files ${CMAKE_HOME_DIRECTORY}/input/*.txt)
file(COPY ${input_files} DESTINATION "${PROJECT_BINARY_DIR}/input")

# create output directory
# file(MAKE_DIRECTORY "${PROJECT_BINARY_DIR}/output")

