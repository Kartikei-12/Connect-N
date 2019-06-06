# Connect-N

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
[![Build Status](https://travis-ci.org/Kartikei-12/Connect-N.svg?branch=master)](https://travis-ci.org/Kartikei-12/Connect-N)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4a053ff3c19247958b88183242723d23)](https://www.codacy.com/app/Kartikei-12/Connect-N?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Kartikei-12/Connect-N&amp;utm_campaign=Badge_Grade)
![Codecov](https://img.shields.io/codecov/c/github/Kartikei-12/Connect-N.svg)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
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
*  Tests in python 3.7 on Windows OS(by developer).
*  API: used [flask](http://flask.pocoo.org/) for API development.
*  Using [flask-migrate](https://pypi.org/project/Flask-Migrate/) for database migration.

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

## Direct Usage

For simple example,

Run main.py as `python main.py` on **windows** with virtual environment(`./venv/Scripts/activate`).

Run main.py as `python3 main.py` on **Ubuntu/Linux** with virtual environment(`source /venv/Scripts/activate`).

## API

### API Setup(One time)

    git clone https://github.com/Kartikei-12/Connect-N
    cd Connect-N-master
    python -m venv venv
    ./venv/Scripts/activate
    pip install -r requirements.txt
    cd connect_n/api/
    pip install -r requirements.txt
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    cd ../../

### API Usage

Run server with `flask run` in `Connect-N/connect_n/api` directory.

API Call: In new terminal do `http http://127.0.0.1:5000/test`

## System Requirements

*  [Python 3](https://www.python.org/)
*  [Pip](https://pypi.org/) usually pre-installed with python, check with `pip3 --version`.
*  Python module [PyGame](https://pypi.org/project/pygame/) installable via pip.

## TODO

*  Create web interface.

## Documentation

[docs](https://kartikei-12.github.io/Connect-N/html/index.html)

## Limitation

GUI **NOT** working inside docker, because no support for pygame inside Docker.
**Workaround**: Code automatically switches to command line interface without raising error connect_n/connect_n.py.

## Contributer(s)

[@Kartikei Mittal](https://github.com/Kartikei-12)

## You are wanted

Looking for any algorithm which may be useful for designing AI for turn based games with more than two players.

## Additional Resources

* Flask Totorial:
  * [Youtube](https://www.youtube.com/watch?v=Z1RJmh_OqeA)
  * [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* freecodecamp [tutorial](https://www.youtube.com/watch?v=8392NJjj8s0)

## Acknowledgment

*  Thanks to [Miguel Grinberg](https://github.com/miguelgrinberg) for excelent resource on flask and how to learn it.
*  Thanks to [freecodecamp](https://www.freecodecamp.org/) for the great beginning boost.

