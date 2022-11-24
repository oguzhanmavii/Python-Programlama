import typer
from uuid import UUID
from enum import Enum

class Animals(str, Enum):
    dog = "Bab",
    cat = "Zorro"

def main(a: int = typer.Argument(...,min=0,max=100),
    b: int = typer.Option(..., min=50, max = 150),
    c: bool = typer.Option(False, '--force'),
    d: UUID = 'd48edaa6-871a-4082-a196-4daab372d4a1',
    e: Animals = Animals.dog,
):
    typer.echo(f"The int is between 0 and 100 : {a}")
    typer.echo(f"The int is between 50 and 150 : {b}")
    if c:
        typer.echo(f"It is forced!")
    else:
        typer.echo(f"No so forced!")
    typer.echo(f"The value of d is: {d}")
    typer.echo(f"The value of e is: {e}")
    
if __name__ == '__main__':
    typer.run(main)