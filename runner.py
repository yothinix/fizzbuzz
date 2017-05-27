import unittest
import datetime
from io import StringIO
from pprint import pprint

import click

from test_fizzbuzz import TestFizzBuzz

start_time = datetime.datetime.now()

stream = StringIO()
runner = unittest.TextTestRunner(stream=stream, verbosity=2)
result = runner.run(unittest.makeSuite(TestFizzBuzz))

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
            status = click.style(' PASS ', bg='green', fg='white', bold=True)
        elif test_instance[3] == 'FAIL':
            status = click.style(' FAIL ', bg='red', fg='white', bold=True)
        elif test_instance[3] == 'ERROR':
            status = click.style(' ERR  ', bg='yellow', fg='white', bold=True)
        else:
            status = click.style(' RUNS ', bg='yellow', fg='white', bold=True)

        test_class = click.style(test_instance[1], fg='white', dim=True)
        click.echo(status + ' ' + test_instance[0] + ' ' + test_class )
    count += 1

click.echo(' ')
pass_text = '{} passed'.format(pass_count)
test_suite_pass = click.style(pass_text, fg='green', bold=True)
title_1 = click.style('Tests: ', bold=True)
title_2 = click.style('Time: ', bold=True)
click.echo(title_1 + '\t\t' + test_suite_pass + ', {}'.format(result.testsRun) + ' total')
click.echo(title_2 + '\t\t' + '{}s'.format((end_time - start_time).total_seconds()))

