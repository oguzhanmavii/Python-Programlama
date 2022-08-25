
import click


@click.group()
def cli():
  pass


@cli.command(name='gen')
def generic():
    click.echo('Hello there')


@cli.command(name='wel')
def welcome():
    click.echo('Welcome')


if __name__ == '__main__':
    cli()