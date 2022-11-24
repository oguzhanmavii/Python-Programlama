import typer,os
from pathlib import Path

APP_NAME = "cli__appdir"

def main():
    app_dir = typer.get_app_dir(APP_NAME)
    config_file= os.path.sep.join([app_dir,APP_NAME,'config',f'{APP_NAME}.config'])
    typer.echo(app_dir)
    typer.echo(config_file)

if __name__ == '__main__':
    typer.run(main)    