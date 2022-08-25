import click


@click.command()
def hello():
    click.echo('hello there python imports click')


if __name__ == '__main__':
    hello()