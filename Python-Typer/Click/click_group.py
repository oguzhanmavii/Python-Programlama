import click

@click.group()
def cli():
    pass

@click.command()
def init():
    click.echo("Initializing...")


@click.command()
def drop():
    click.echo("Dropping...")



cli.add_command(init)
cli.add_command(drop)

if __name__ == '__main__':
    cli()