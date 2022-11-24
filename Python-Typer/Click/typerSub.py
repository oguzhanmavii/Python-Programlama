import typer
import click

@click.group()
def cli():
    ...


@click.command()
def init():
    click.echo("Initiliazing!")

@click.command()
def drop():
    click.echo("Dropping!")

app = typer.Typer()


@app.command()
def sub():
    typer.echo("Typer is now included in the click main ")



typer_click_object = typer.main.get_command(app)
cli.add_command(typer_click_object,"sub")


if __name__ == '__main__':
    cli()

