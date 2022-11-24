import typer
from typing import Optional 
def main(a: str, b:int, c: Optional[float]=3.15):
    typer.echo(f"welcome to typer app !")
    typer.echo(f"The value of <a> is {a} , The value of <b> is {b}")
    typer.echo(f"The optional value of float <c> is {c}")



if __name__ == '__main__':
    typer.run(main)