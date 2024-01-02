cmake_minimum_required(VERSION 3.10)
project(Playground)

set(CMAKE_CXX_STANDARD 17)

find_package(SFML 2.6 COMPONENTS graphics audio window system network REQUIRED)

file(GLOB_RECURSE SOURCES "src/*.cpp")

add_executable(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE ${SFML_INCLUDE_DIR})
target_link_libraries(${PROJECT_NAME} PRIVATE
    sfml-graphics
    sfml-audio
    sfml-window
    sfml-system
    sfml-network
)
