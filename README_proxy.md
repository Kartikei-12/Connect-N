# Connect - N

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

![!Build:](https://travis-ci.org/Kartikei-12/Connect-N.svg?branch=master)

<hr>

## Introduction

A simple modified version of Connect Four Game implemented with AI in Python using PyGame.

## Project Description

* This repositry contains a simple game made in **python** similar to **Connect 4**, bit modified to work with any Connect length for any board size.
* Currently supports for variable number of players on a two dimentional board.
* Tests for python 3.7.
* Tested on Windows.

## Installation

### Windows

    git clone https://github.com/Kartikei-12/Connect-N
    cd Connect-N-master
    python -m venv venv
    ./venv/Scripts/activate
    pip install -r requirements.txt

### Linux based OS

    git clone https://github.com/Kartikei-12/Connect-N
    cd Connect-N-master
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

## Usage

For simple example run main.py as `python main.py` on windows and `python3 main.py` on Linux/Ubuntu, after activating Virtual environment. 

## System Requirements

* [Python 3](https://www.python.org/)
* [Pip](https://pypi.org/) usually pre-installed with python.
* Python module [PyGame](https://pypi.org/project/pygame/) installable via pip.

## Directory Structure

```

Connect-N/
    .gitignore
    docs/
        doctrees/: doctrees for documentation
        html/: HTML source files dor documentation
        .nojekyll
        /index.html
    connect_n/
        __init__.py
        connect_n.py
        utility.py
        player.py
    reports/
        test_result.html
    LICENSE
    main.py
    tests.py
    utility.py
    default_variables.py
    README.md
    README_proxy.md
    requirements.txt

```

## Documentation

[docs](https://kartikei-12.github.io/Connect-N/html/index.html)

## Bugs / TODO

Docker build failing, pygame not working inside Docker container.

## Contributer(s)

[@Kartikei Mittal](https://github.com/Kartikei-12)
