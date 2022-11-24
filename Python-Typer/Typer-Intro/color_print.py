import typer
from typing import Optional


def main(name:str, optional:Optional[str]="Mavi"):
    string_style = typer.style(name,fg=typer.colors.BRIGHT_RED,bold=True)
    string_style2= typer.style(optional,fg=typer.colors.BRIGHT_BLUE,bold= True)
    message = f"welcome "
    typer.echo(message + string_style + string_style2)
    typer.echo(string_style2)
    typer.secho(f"The Other way {name}",fg=typer.colors.CYAN)
    typer.echo(f"This goes to stantart error !")



if __name__ =='__main__':
    typer.run(main)
