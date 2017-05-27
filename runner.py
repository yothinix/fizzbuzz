import unittest
import datetime
from io import StringIO
from pprint import pprint

import click

from display import display_status, print_testcase, print_summary


start_time = datetime.datetime.now()

stream = StringIO()
runner = unittest.TextTestRunner(stream=stream, verbosity=2)
loader = unittest.TestLoader()
tests = loader.discover(start_dir='./example_project', pattern='test*.py')
result = runner.run(tests)

end_time = datetime.datetime.now()

# print('Errors {}'.format(result.errors))
# pprint(result.failures)
stream.seek(0)
test_result = stream.read()
text_line = test_result.split('\n')
count = 0
pass_count = 0
for line in text_line:
    if count < result.testsRun:
        test_instance = line.split(' ')
        if test_instance[3] == 'ok':
            pass_count += 1

        print_testcase(
            status=display_status(test_instance[3]),
            name=test_instance[0],
            suite=test_instance[1]
        )
    count += 1

print_summary(
    pass_number=pass_count,
    total_test=result.testsRun,
    execution_time=(end_time - start_time).total_seconds()
)

