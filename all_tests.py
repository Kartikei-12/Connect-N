"""Runs all tests"""

# Python module(s)
import unittest
from HtmlTestRunner import HTMLTestRunner

def main():
    """Test cases"""
    test_runner = HTMLTestRunner(
        verbosity=3,
        descriptions=True,
        open_in_browser=False,
        combine_reports=True,
        report_name="test_result",
        add_timestamp=False,
    )
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    test_runner.run(test_suite)
    
if __name__ == "__main__":
    main()
