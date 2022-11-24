import typer

app = typer.Typer()
app_command = typer.Typer()

app.add_typer(app_command, name = 'add')

@app_command.command("remote")
def a(address: str = typer.Option(...,help = 'Remote address')):
    typer.echo("Added subcommand and it is working!")
    typer.echo(f"The address is: {address}")

if __name__ == '__main__':
    app()