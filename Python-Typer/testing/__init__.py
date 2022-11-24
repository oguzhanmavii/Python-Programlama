import typer
from typing import Optional

app= typer.Typer()

@app.command()
def hello_world(name:str,age:Optional[int]=None):
    typer.echo(f"Hello world: {name}")
    if age >21:
        typer.echo(f"{name} you are an adult!")
    else:
        typer.echo(f"{name} you are a minor!")

if __name__ == '__main__':
    app()            