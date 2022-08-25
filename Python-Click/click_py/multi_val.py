import click

@click.command()
@click.option('--data',required=True,type=(str,int,str))
def output(data):
    click.echo(f'name:{data[0]} age:{data[1]} work:{data[2]}')


if __name__ == '__main__':
    output()        