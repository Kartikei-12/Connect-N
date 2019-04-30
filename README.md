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



<!DOCTYPE html>
<html>

<body>
    <div class="container">
        <div class="row">
            <div class="col-xs-12">
                <h2 class="text-capitalize">Unittest Results</h2>
                <p class='attribute'><strong>Start Time: </strong>2019-04-30 18:57:04</p>
                <p class='attribute'><strong>Duration: </strong>20.79 s</p>
                <p class='attribute'><strong>Summary: </strong>Total: 16, Pass: 16</p>
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
                            <td class="col-xs-10">test_play</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                                <button class="btn btn-default btn-xs">View</button>
                            </td>
                        </tr>
                        <tr style="display:none;">
                            <td class="col-xs-9" colspan="3"><p>[[0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]]
[[0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]]
[[0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]]
[[0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]]
[[0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 1 0 0 0]
 [2 0 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 2 1 0 0 0]
 [2 0 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 1 0 0 0 0]
 [1 0 2 1 0 0 0]
 [2 0 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 2 1 0 0 0]
 [2 0 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 1 0 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 2 1 0 0 0]
 [2 0 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0]
 [1 0 1 2 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 2 1 0 0 0]
 [2 0 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 1 0 0 0 0]
 [1 0 1 2 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 2 1 0 0 0]
 [2 0 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 1 2 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 2 1 0 0 0]
 [2 0 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 1 2 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 2 1 0 0 0]
 [2 1 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 1 2 0 0 0]
 [2 0 1 2 0 0 0]
 [1 2 2 1 0 0 0]
 [2 1 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 1 2 0 0 0]
 [1 0 1 2 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 2 1 0 0 0]
 [2 1 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 0 1 2 0 0 0]
 [1 2 1 2 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 2 1 0 0 0]
 [2 1 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 1 2 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 2 1 0 0 0]
 [2 1 2 1 0 0 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 1 2 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 2 1 0 0 0]
 [2 1 2 1 2 0 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 1 2 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 2 1 1 0 0]
 [2 1 2 1 2 0 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 1 2 0 0 0]
 [2 1 1 2 2 0 0]
 [1 2 2 1 1 0 0]
 [2 1 2 1 2 0 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 0 0 0]
 [1 2 1 2 1 0 0]
 [2 1 1 2 2 0 0]
 [1 2 2 1 1 0 0]
 [2 1 2 1 2 0 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 2 0 0]
 [1 2 1 2 1 0 0]
 [2 1 1 2 2 0 0]
 [1 2 2 1 1 0 0]
 [2 1 2 1 2 0 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 2 0 0]
 [1 2 1 2 1 0 0]
 [2 1 1 2 2 0 0]
 [1 2 2 1 1 0 0]
 [2 1 2 1 2 1 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 2 0 0]
 [1 2 1 2 1 0 0]
 [2 1 1 2 2 0 0]
 [1 2 2 1 1 2 0]
 [2 1 2 1 2 1 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 2 0 0]
 [1 2 1 2 1 0 0]
 [2 1 1 2 2 1 0]
 [1 2 2 1 1 2 0]
 [2 1 2 1 2 1 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 2 0 0]
 [1 2 1 2 1 2 0]
 [2 1 1 2 2 1 0]
 [1 2 2 1 1 2 0]
 [2 1 2 1 2 1 0]]
[[0 0 0 0 0 0 0]
 [2 1 1 2 2 1 0]
 [1 2 1 2 1 2 0]
 [2 1 1 2 2 1 0]
 [1 2 2 1 1 2 0]
 [2 1 2 1 2 1 0]]
Winner:  AI
[32m30-04-2019 at 18:57:05[0m: [1m
Winner: <class 'AI'> 2
        Players: [<connect_n.ai.AI object at 0x05CA2B10>, <connect_n.ai.AI object at 0x05CA2B90>]
        Game Sequence: [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]

[0m
</p>
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
                                Total: 10, Pass: 10 -- Duration: 536 ms
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
                            <th>__main__.PygameUtilityTests</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class='success'>
                            <td class="col-xs-10">test_play</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3">
                                Total: 1, Pass: 1 -- Duration: 20.25 s
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div></body></html>