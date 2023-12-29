cmake_minimum_required(VERSION 3.10)
project(Playground)

set(CMAKE_CXX_STANDARD 17)

# Set the SFML_DIR variable to the path of the folder containing the SFMLConfig.cmake file
set(SFML_DIR "./SFML-2.6.1")

# Use the find_package command to locate the SFML library
find_package(SFML 2.6 COMPONENTS graphics audio REQUIRED)

file(GLOB_RECURSE SOURCES "src/*.cpp")

add_executable(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PUBLIC include)

# Link your executable with the SFML libraries
target_link_libraries(${PROJECT_NAME} sfml-graphics sfml-audio)
