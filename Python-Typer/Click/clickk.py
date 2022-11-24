import click

@click.command()
@click.option("--age",default=0,help="The age!")
@click.option("--name",default=None,help="Your name!")
def hello(age,name):
    click.echo(f"{name} you are {age} years old!")


if __name__ == '__main__':
    hello()