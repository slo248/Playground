file(GLOB_RECURSE MYMATH_SOURCES "*.cpp")
file(GLOB_RECURSE MYMATH_HEADERS "*.h")
add_library(mymath STATIC ${MYMATH_SOURCES} ${MYMATH_HEADERS})
target_include_directories(mymath PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
