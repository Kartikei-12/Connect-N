"""
Utility methods for project maintainance, efficiency and enhancement.
Have no relation to actual working of project.
"""


def update_readme():
    """Function to genrate README.md by concatinating README_proxy.md and unit test result
    in reports/ folder"""
    with open("README_proxy.md", "r") as old_readme_file:
        old_readme_txt = old_readme_file.read()

    with open("reports/test_result.html", "r") as html_file:
        html = html_file.read().splitlines()[0:-21]
    html = "\n".join(html).replace("<title>Unittest Results</title>", "")

    with open("README.md", "w") as new_readme_file:
        new_readme_file.write(old_readme_txt + "\n\n\n" + html + "</body></html>")
