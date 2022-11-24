import click
import typer

app = typer.Typer()

@app.command()
def top():
    typer.echo("Click is now a subapp of typer!")

@app.callback()
def callback():
    typer.echo("This is the typer app including click subapp!")

@click.command()
@click.option("--name", help = "Your name!", prompt = "Enter your name:")
def hello(name):
    click.echo(f"You are {name}!")

typer_click_object = typer.main.get_command(app)
typer_click_object.add_command(hello,"hello")

if __name__ == '__main__':
    typer_click_object()