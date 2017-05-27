import unittest
import datetime
from io import StringIO
from pprint import pprint

import click

from display import display_status, print_testcase, print_summary, print_errors, print_failures
from utils import is_pass


start_time = datetime.datetime.now()

stream = StringIO()
runner = unittest.TextTestRunner(stream=stream, verbosity=2)
loader = unittest.TestLoader()
tests = loader.discover(start_dir='./example_project', pattern='test*.py')
result = runner.run(tests)

end_time = datetime.datetime.now()

stream.seek(0)
test_result = stream.read()
text_line = test_result.split('\n')
count = 0
pass_count = 0
for line in text_line:
    if count < result.testsRun:
        test_instance = line.split(' ')
        if is_pass(test_instance[3]):
            pass_count += 1

        print_testcase(
            status=display_status(test_instance[3]),
            name=test_instance[0],
            suite=test_instance[1]
        ) if is_pass(test_instance[3]) else None
    count += 1

print_failures(failures=result.failures)
print_errors(errors=result.errors)

print_summary(
    pass_number=pass_count,
    fail_number=len(result.failures),
    err_number=len(result.failures),
    total_test=result.testsRun,
    execution_time=(end_time - start_time).total_seconds()
)

