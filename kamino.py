#!/usr/bin/python
import printlogo
import click

@click.command()
@click.option('--url', prompt='your swagger url',
              help='The person to greet.')

def hello(url):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('Hello %s!' % url)

if __name__ == '__main__':
    hello()