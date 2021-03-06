import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="draup_django",
    version="1.0.0",
    author="Arpit | Teja | Kashish",
    author_email="arpit@zinnov.com",
    description=" Django Utility - Draup Labs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Draup-Zinnov/draup_django",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)