import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="FCleverbot",
    version="0.0.0",
    author="F4stZ4p",
    author_email="f4stz4p@gmail.com",
    description="FCleverbot cleverbot.io library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/F4stZ4p/FCleverbot",
    packages=setuptools.find_packages(),
    license="MIT",
    install_requires=requirements,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)