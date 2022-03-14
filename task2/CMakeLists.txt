cmake_minimum_required(VERSION 2.8)
project(Task2)


set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

add_custom_command(
	OUTPUT ${PROJECT_SOURCE_DIR}/A/index.h 
	COMMAND python3 ${PROJECT_SOURCE_DIR}/A/preparing.py ${PROJECT_SOURCE_DIR}/A/index.h
)



add_subdirectory(B)

add_executable(Task2 C/main.cpp)

target_include_directories(Task2 PRIVATE .)


target_link_libraries(Task2 task2)

add_custom_target( RunGenerator DEPENDS A/index.h )
add_dependencies( Task2 RunGenerator )
target_include_directories(Task2 PRIVATE ${CMAKE_BINARY_DIR})
