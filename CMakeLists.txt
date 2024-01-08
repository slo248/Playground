cmake_minimum_required(VERSION 3.10)
project(Playground)

set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE SOURCES "src/*.cpp")

find_package(SFML 2.6 COMPONENTS graphics window system audio REQUIRED)

if(NOT SFML_FOUND)
    include(FetchContent)
    FetchContent_Declare(
        sfml
        GIT_REPOSITORY https://github.com/SFML/SFML.git
        GIT_TAG 2.6.0
    )
    FetchContent_MakeAvailable(sfml)
    set(SFML_LIBRARIES sfml-graphics sfml-window sfml-system sfml-audio)
    set(SFML_INCLUDE_DIR ${sfml_SOURCE_DIR}/include)
endif()

add_executable(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME} ${SFML_LIBRARIES})
target_include_directories(${PROJECT_NAME} PUBLIC include ${SFML_INCLUDE_DIR})

# Testing
include(CTest)

add_executable(MathTest test/MathTest.cpp src/MyMath.cpp)
target_include_directories(MathTest PUBLIC include)
add_test(NAME Test COMMAND MathTest)
