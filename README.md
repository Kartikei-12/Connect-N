# Connect - N

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![!Build:](https://travis-ci.org/Kartikei-12/Connect-N.svg?branch=master)

<hr>

## Introduction

A simple modified version of Connect Four Game implemented with AI in Python using PyGame.

## Project Description

* This repositry contains a simple game made in **python** similar to **Connect 4**,a bit modified to work with any Connect length for any board size.
* Currently supports for variable number of players on a two dimentional board.
* Only **three** players supported in GUI mode, for more players just add new colours `COLOR` and `C_LIST` variable in connect_n/pygame_utility.py
* ID 1 is reserved for AI.
* Currently only supports single AI player in a game.
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
        ai.py
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
    Dockerfile

```

## TODO

* Implement score method in ai.py
* Make AI actually work.

## Documentation

[docs](https://kartikei-12.github.io/Connect-N/html/index.html)

## Limitation

GUI **NOT** working inside docker, because no support for pygame inside Docker.

## Contributer(s)

[@Kartikei Mittal](https://github.com/Kartikei-12)



<!DOCTYPE html>
<html>
<head>
    
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-xs-12">
                <h2 class="text-capitalize">Unittest Results</h2>
                <p class='attribute'><strong>Start Time: </strong>2019-04-25 17:11:16</p>
                <p class='attribute'><strong>Duration: </strong>15 ms</p>
                <p class='attribute'><strong>Summary: </strong>Total: 14, Pass: 14</p>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 col-sm-10 col-md-10">
                <table class='table table-hover table-responsive'>
                    <thead>
                        <tr>
                            <th>__main__.AITests</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class='success'>
                            <td class="col-xs-10">test_horizontal_score</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_negative_digonal_score</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_positive_digonal_score</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_string_score</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_vertical_score</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3">
                                Total: 5, Pass: 5 -- Duration: 0 ms
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 col-sm-10 col-md-10">
                <table class='table table-hover table-responsive'>
                    <thead>
                        <tr>
                            <th>__main__.ConnectNTests</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class='success'>
                            <td class="col-xs-10">test_add_player</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_horizontal_winning_move</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_is_valid_move</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_make_move</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_negative_digonal_winning_move</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_positive_digonal_winning_move</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_simulate</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_version</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr class='success'>
                            <td class="col-xs-10">test_vertical_winning_move</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3">
                                Total: 9, Pass: 9 -- Duration: 15 ms
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div></body></html>