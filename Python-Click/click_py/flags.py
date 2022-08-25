import click

@click.command()
@click.option('--blue',is_flag=True,help='message in blue color')
@click.option('--red',is_flag=True,help='message in red color')
@click.option('--yellow',is_flag=True,help='message in yellow color')
@click.option('--purple',is_flag=True,help='message in purple color')
def hello(blue,red,yellow,purple):

    if blue:
        click.secho('Hello there',fg='blue')
    elif red:
        click.secho('Hello there',fg='red')    
    elif yellow:
        click.secho('Hello there',fg='yellow')
    elif purple:
        click.secho('Hello there',fg='magenta')    
    else:
        click.secho('Hello there') 

if __name__ == '__main__':
    hello()           