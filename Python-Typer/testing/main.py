from typing import Optional
import typer

app=typer.Typer()

@app.command()
def hello_world(name:str,age:Optional[int]=None):
    typer.echo(f"{name} your age is {age}")
    if age >21:
        typer.echo(f"You are an adult!")
    else:
        typer.echo(f"You are a minor!")

if __name__ == "__main__":
    app()