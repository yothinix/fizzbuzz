import click
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter

FOREGROUND = 'white'
LEXER = get_lexer_by_name('py3tb')


def display_status(status):
    if status == 'ok':
        return click.style(' PASS ', bg='green', fg=FOREGROUND, bold=True)
    elif status == 'FAIL':
        return click.style(' FAIL ', bg='red', fg=FOREGROUND, bold=True)
    elif status == 'ERROR':
        return click.style(' ERR  ', bg='yellow', fg=FOREGROUND, bold=True)
    else:
        return click.style(' RUNS ', bg='yellow', fg=FOREGROUND, bold=True)


def display_test_name(name, status='ok'):
    if status == 'FAIL':
        return click.style(name, fg='red')
    elif status == 'ERROR':
        return click.style(name, fg='yellow')
    else:
        return click.style(name, fg='white')


def print_testcase(status, name, suite):
    display_suite = click.style(suite, fg='white', dim=True)
    click.echo(status + ' ' + name + ' ' + display_suite)


def print_summary(pass_number, fail_number, err_number, total_test, execution_time):
    click.echo(' ')
    test_pass = click.style('{} passed, '.format(pass_number), fg='green', bold=True)
    test_fail = click.style('{} failed, '.format(fail_number), fg='red', bold=True)
    test_err = click.style('{} error, '.format(err_number), fg='yellow', bold=True)
    run_stat = test_pass + test_fail + test_err
    title_1 = click.style('Tests: ', bold=True)
    title_2 = click.style('Time: ', bold=True)
    click.echo(title_1 + '\t\t' + run_stat + ' {}'.format(total_test) + ' total')
    click.echo(title_2 + '\t\t' + '{}s'.format(execution_time))


def print_failures(failures):
    for fail in failures:
        desc = fail[0].__str__().split(' ')
        name, suite = desc[0], desc[1]
        print_testcase(display_status('FAIL'), display_test_name(name, 'FAIL'), suite)
        click.echo(click.style(highlight(fail[1], LEXER, Terminal256Formatter()), dim=True))


def print_errors(errors):
    for err in errors:
        desc = err[0].__str__().split(' ')
        name, suite = desc[0], desc[1]
        print_testcase(display_status('ERROR'), display_test_name(name, 'ERROR'), suite)
        click.echo(click.style(highlight(err[1], LEXER, Terminal256Formatter()), dim=True))

