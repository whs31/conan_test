from conan import ConanFile


class ConanTest(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    name = "conan_test"
    version = "0.1.0"

    def requirements(self):
        self.requires("spdlog/1.11.0")