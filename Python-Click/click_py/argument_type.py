import click

@click.command()
@click.argument('name',default='quest')
@click.argument('age',type=int)
def hello_click(name,age):
    click.echo(f'{name} is {age} years old')

if __name__ == '__main__':
    hello_click()