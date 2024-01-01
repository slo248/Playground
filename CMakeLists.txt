cmake_minimum_required(VERSION 3.10)
project(Playground)

set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE SOURCES "src/*.cpp")

add_executable(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME} PRIVATE
    sfml-graphics-s
    sfml-audio-s
    sfml-window-s
    sfml-system-s
    sfml-network-s
)
