import typer


app= typer.Typer()


@app.callback
def callback():
    ...

@app.command()
def shoot():
    typer.echo("BFG is unavaible!")  

@app.command()
def load():
    typer.echo("BFG is reloaded!")



from typerpackage import app      