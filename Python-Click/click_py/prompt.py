import click

@click.command()
@click.option("--name",prompt="Your name",help="Provide your name")
def hello(name):
    click.echo(f"hello,{name}")


if __name__ == '__main__':
    hello()