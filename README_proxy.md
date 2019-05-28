# Connect-N

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
[![Build Status](https://travis-ci.org/Kartikei-12/Connect-N.svg?branch=master)](https://travis-ci.org/Kartikei-12/Connect-N)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4a053ff3c19247958b88183242723d23)](https://www.codacy.com/app/Kartikei-12/Connect-N?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Kartikei-12/Connect-N&amp;utm_campaign=Badge_Grade)
![Codecov](https://img.shields.io/codecov/c/github/Kartikei-12/Connect-N.svg)
<hr>

## Introduction

A simple modified version of Connect Four Game implemented with AI in Python using PyGame.

## Project Description

*  This repositry contains a simple game made in **python** similar to **Connect 4**.
*  A bit modified to work with any connect length for any board size.
*  Currently supports for variable number of players on a two dimentional board.
*  Only **three** players supported in GUI mode.
*  For more players add new colours `COLOR` variable in connect_n/pygame_utility.py file.
*  ID 1 is reserved for AI.
*  Currently only supports single AI player in a game.
*  Tests for python 3.7.
*  Tested on Windows.

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

For simple example,

Run main.py as `python main.py` on **windows** with virtual environment(`./venv/Scripts/activate`).

Run main.py as `python3 main.py` on **Ubuntu/Linux** with virtual environment(`source /venv/Scripts/activate`).

## System Requirements

*  [Python 3](https://www.python.org/)
*  [Pip](https://pypi.org/) usually pre-installed with python, check with `pip3 --version`.
*  Python module [PyGame](https://pypi.org/project/pygame/) installable via pip.

## Directory Structure

    Connect-N/
        .gitignore
        docs/
            doctrees/: doctrees for documentation
            html/: HTML source files dor documentation
            .nojekyll
            index.html
        connect_n/
            __init__.py
            ai.py
            web.py
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
        .travis.yml
        .coverage
        Dockerfile

## TODO

*  Create web interface.

## Documentation

[docs](https://kartikei-12.github.io/Connect-N/html/index.html)

## Limitation

GUI **NOT** working inside docker, because no support for pygame inside Docker.
**Workaround**: Code automatically switches to command line interface without raising error connect_n/connect_n.py.

## Contributer(s)

[@Kartikei Mittal](https://github.com/Kartikei-12)

## You are wanted!

Looking for any algorithm which may be useful for designing AI for turn based games with more than two players.
