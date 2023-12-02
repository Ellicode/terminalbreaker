import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "tbpy",
    version = "1.3.1",
    author = "Ellicode",
    author_email = "ellicode22@gmail.com",
    description = "Welcome to terminalbreaker!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Ellicode/terminalbreaker",
    project_urls = {
        "Bug Tracker": "https://github.com/Ellicode/terminalbreaker/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)