cmake_minimum_required(VERSION 3.27)
project(conan_test)

find_package(spdlog REQUIRED)

add_executable(conan_test main.cpp)

target_link_libraries(conan_test PRIVATE spdlog::spdlog)
