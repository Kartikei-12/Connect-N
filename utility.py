"""Utility methods for project maintainance, efficiency and enhancement.
Have no relation to actual working of project"""


def update_readme():
    """Function to genrate README.md by concatinating README_proxy.md and unit test result
    in reports/ folder"""

    temp = """<head>
    <title>Unittest Results</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
</head>"""

    with open("README_proxy.md", "r") as old_readme_file:
        old_readme_txt = old_readme_file.read()

    with open("reports/test_result.html", "r") as html_file:
        html = html_file.read().splitlines()[0:-21]
    html = "\n".join(html).replace(temp, "")

    with open("README.md", "w") as new_readme_file:
        new_readme_file.write(old_readme_txt + "\n\n\n" + html + "</body></html>")
