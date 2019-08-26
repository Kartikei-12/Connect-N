import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="connect-n",
    version="0.0.2",
    author="Kartikei Mittal",
    author_email="kartikeimittal@gmail.com",
    description="A modified version of Connect-4 game implemented with AI using PyGame.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kartikei-12/Connect-N",
    packages=setuptools.find_packages(),
    install_requires=open("requirements.txt", "r").read().split("\n"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
