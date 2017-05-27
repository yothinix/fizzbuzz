import click

FOREGROUND = 'white'


def display_status(status):
    if status == 'ok':
        return click.style(' PASS ', bg='green', fg=FOREGROUND, bold=True)
    elif status == 'FAIL':
        return click.style(' FAIL ', bg='red', fg=FOREGROUND, bold=True)
    elif status == 'ERROR':
        return click.style(' ERR  ', bg='yellow', fg=FOREGROUND, bold=True)
    else:
        return click.style(' RUNS ', bg='yellow', fg=FOREGROUND, bold=True)


def print_testcase(status, name, suite):
    display_suite = click.style(suite, fg='white', dim=True)
    click.echo(status + ' ' + name + ' ' + display_suite)


def print_summary(pass_number, total_test, execution_time):
    click.echo(' ')
    pass_text = '{} passed'.format(pass_number)
    test_suite_pass = click.style(pass_text, fg='green', bold=True)
    title_1 = click.style('Tests: ', bold=True)
    title_2 = click.style('Time: ', bold=True)
    click.echo(title_1 + '\t\t' + test_suite_pass + ', {}'.format(total_test) + ' total')
    click.echo(title_2 + '\t\t' + '{}s'.format(execution_time))

