import typer 


def main(
    a: str = typer.Option('Daniel',help="The last name of the person!"),
    b: str = typer.Option(...,help="This is a required option!"),
    c: str = typer.Option(...,help="This will be prompted!",prompt=True),
    d: str = typer.Option(...,help="This will be confirmed!",prompt=True,confirmation_prompt=True),
):
    typer.echo(f"The provided last name is : {a}")
    typer.echo(f"The provided b option is: {b}")
    typer.echo(f"The prompted option is: {c}")
    typer.echo(f"The confirmantion prompted option is: {d}")


if __name__ == '__main__':
    typer.run(main)
