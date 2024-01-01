cmake_minimum_required(VERSION 3.10)
project(Playground)

set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE SOURCES "src/*.cpp")
find_package(SFML COMPONENTS graphics audio window system network REQUIRED)

add_executable(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME}
    sfml-graphics
    sfml-audio
    sfml-window
    sfml-system
    sfml-network
)
