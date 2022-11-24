import typer


app = typer.Typer()



@app.command()
def main(system: str = typer.Option(...,help='The system that you would like to reboot!')):
    url = 'https://www.'+'{system}'+'.com'
    typer.echo(f"{url}")
    typer.launch(url)


if __name__ == '__main__':
    app()
