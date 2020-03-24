import os
from conans import ConanFile, CMake, tools


class XXHashConan(ConanFile):
    name = "xxhash"
    version = "3620d0a"
    license = "MIT"
    description = "xxHash - a super-fast hash algorithm in a single C++ header"
    homepage = "https://create.stephan-brumme.com/xxhash/"
    url = "https://github.com/igor-sadchenko/conan-xxhash/"
    generators = "cmake"
    exports = "LICENSE"
    revision_mode = "scm"
    scm = {
        "type": "git",
        "subfolder": "sources",
        "url": "https://github.com/igor-sadchenko/xxhash.git",
        "revision": version,
     }


    def package(self):
        self.copy("LICENSE", dst="licenses", src="sources")
        self.copy("*.h", dst="include", src="sources")
