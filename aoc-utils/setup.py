import setuptools

setuptools.setup(
    name="aoc",
    version="2021.12.01",
    author="fourjr",
    url="https://github.com/fourjr/advent-of-code",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['aoc'],
    include_package_data=True,
    install_requires=['advent-of-code-data'],
    python_requires=">=3.8",
)
