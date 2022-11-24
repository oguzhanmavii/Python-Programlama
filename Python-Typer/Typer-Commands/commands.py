import typer

def callback():
    typer.echo("This is the callback function in action!")

app= typer.Typer(callback=callback)

@app.command()
def update():
    typer.echo("This is a simple command without arguments or options")
    typer.echo("This will update the system !")




@app.command()
def upgrade(system: str = 'localhost'):
    typer.echo(f"The <{system}> will be upgraded!")


@app.command()
def reboot(system: str = typer.Option(...,help='The system that you would like to reboot!')):
    typer.echo(f"The <{system}> will be restarted!")


if __name__ == '__main__':
    app()
        
