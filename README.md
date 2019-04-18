# Connect - N
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
<hr>

## Introduction

A simple modified version of Connect Four Game implemented with AI in Python using PyGame.

## Project Description

This repositry contains a simple game made in **python** similar to **Connect 4**, bit modified to work with any Connect length for any board size.

Currently supports only two player on a two dimintional board.

## System Requirements

* [Python 3](https://www.python.org/)
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
    LICENSE
    README.md
    main.py
    tests.py
    default_variables.py
    requirements.txt

```

## Documentation

[docs](https://kartikei-12.github.io/Connect-N/html/index.html)

## Contributer(s)

[@Kartikei Mittal](https://github.com/Kartikei-12)



<!DOCTYPE html>
<html>
<head>
    <title>Unittest Results</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-xs-12">
                <h2 class="text-capitalize">Unittest Results</h2>
                <p class='attribute'><strong>Start Time: </strong>2019-04-18 21:50:13</p>
                <p class='attribute'><strong>Duration: </strong>6 ms</p>
                <p class='attribute'><strong>Summary: </strong>Total: 7, Pass: 7</p>
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
                            <td class="col-xs-10">test_init</td>
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
                                Total: 7, Pass: 7 -- Duration: 6 ms
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div></body>
</html