from conan.packager import ConanMultiPackager
import os, re


def get_value_from_recipe(search_string):
    with open("conanfile.py", "r") as conanfile:
        contents = conanfile.read()
        result = re.search(search_string, contents)
    return result

def get_name_from_recipe():
    return get_value_from_recipe(r'''name\s*=\s*["'](\S*)["']''').groups()[0]

def get_version_from_recipe():
    return get_value_from_recipe(r'''version\s*=\s*["'](\S*)["']''').groups()[0]


if __name__ == "__main__":
    header_only = False
    name = get_name_from_recipe()
    version = get_version_from_recipe()
    reference = "{0}/{1}".format(name, version)
    username = "zetcpp"
    upload_remote = "https://api.bintray.com/conan/{0}/conan/".format(username)

    builder = ConanMultiPackager(
        stable_branch_pattern="stable/*",
        upload_only_when_stable=True,
        username=username,
        login_username=username,
        reference=reference,
        upload=upload_remote,
        remotes=upload_remote,
        build_policy="missing",
        visual_toolsets={'16':['v142']},
        visual_versions=['16'],
        password="551fb60cc5e011e11873bc92cc0d112ef6471155"
    )

    if header_only:
        filtered_builds = []
        for settings, options, env_vars, build_requires, reference in builder.items:
            if settings["compiler"] == "gcc":
                filtered_builds.append([settings, options, env_vars, build_requires])
                break
        builder.builds = filtered_builds

    builder.add_common_builds()
    builder.run()
