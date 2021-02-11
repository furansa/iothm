cmake_minimum_required(VERSION 3.16.3 FATAL_ERROR)

project(events LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)

# CPM packages
set(CPM_DOWNLOAD_VERSION 0.27.2) 
set(CPM_DOWNLOAD_LOCATION "${CMAKE_BINARY_DIR}/cmake/CPM_${CPM_DOWNLOAD_VERSION}.cmake")

if(NOT (EXISTS ${CPM_DOWNLOAD_LOCATION}))
    message(STATUS "Downloading CPM.cmake v${CPM_DOWNLOAD_VERSION}")
    file(DOWNLOAD https://github.com/TheLartians/CPM.cmake/releases/download/v${CPM_DOWNLOAD_VERSION}/CPM.cmake ${CPM_DOWNLOAD_LOCATION})
endif()

include(${CPM_DOWNLOAD_LOCATION})

CPMAddPackage(
    NAME Catch2
    GITHUB_REPOSITORY catchorg/Catch2
    VERSION 2.13.4
)

CPMAddPackage(
    NAME crow
    GITHUB_REPOSITORY CrowCpp/crow
    VERSION 0.1
)

# Executable
add_executable(events src/main.cpp)

# Link dependencies
target_link_libraries(events
    Catch2
    crow
)
