from conan import ConanFile
from conan.tools.cmake import CMakeDeps


class SiloRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    requires = [
    ]

    default_options = {
    }

    def generate(self):
        deps = CMakeDeps(self)
        deps.set_property("abseil", "cmake_find_mode", "both")
        deps.set_property("boost", "cmake_find_mode", "both")
        deps.set_property("gtest", "cmake_find_mode", "both")
        deps.set_property("hwloc", "cmake_find_mode", "both")
        deps.set_property("mimalloc", "cmake_find_mode", "both")
        deps.set_property("nlohmann_json", "cmake_find_mode", "both")
        deps.set_property("pcre2", "cmake_find_mode", "both")
        deps.set_property("poco", "cmake_find_mode", "both")
        deps.set_property("re2", "cmake_find_mode", "both")
        deps.set_property("roaring", "cmake_find_mode", "both")
        deps.set_property("spdlog", "cmake_find_mode", "both")
        deps.set_property("simdjson", "cmake_find_mode", "both")
        deps.set_property("yaml-cpp", "cmake_find_mode", "both")
        deps.set_property("zstd", "cmake_find_mode", "both")
        deps.generate()
