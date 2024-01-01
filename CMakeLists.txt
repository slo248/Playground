cmake_minimum_required(VERSION 3.10)
project(Playground)

set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE SOURCES "src/*.cpp")

set(SFML_DIR "${CMAKE_SOURCE_DIR}/SFML/lib/cmake/SFML")
find_package(SFML 2.6 COMPONENTS graphics audio)

add_executable(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE "SFML/include")
target_link_libraries(${PROJECT_NAME} sfml-graphics sfml-audio)
