cmake_minimum_required(VERSION 3.10)
project(Playground)

set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE SOURCES "src/*.cpp")

add_executable(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PUBLIC include)

# Testing
include(CTest)

add_executable(MathTest test/MathTest.cpp src/MyMath.cpp)
target_include_directories(MathTest PUBLIC include)
add_test(NAME Test COMMAND MathTest)
