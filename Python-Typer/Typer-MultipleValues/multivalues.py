import typer
from typing import Tuple

def main(hereos: Tuple[str,str,str] = typer.Option(('Pudge','Drow','Monkey King')),
    names:Tuple[str,str,str]  = typer.Argument(('Pudge','Drow','Monkey King'),help = "Select a hero!")
 ):
    pudge,drow,monkey_king=hereos
    if not pudge or not drow or not monkey_king:
     typer.echo("Heroes not provided!")
    else:
     typer.echo("Hereos are present!")

    typer.echo(names)


if __name__ == '__main__':
     typer.run(main)

