import typer

def main(exit_style:str ='Normal',error_code:int=0):
    if exit_style == 'Normal':
        typer.secho(f"Normal typer exit with code  : {error_code}",fg=typer.colors.GREEN)
        raise typer.Exit()

    elif exit_style == 'Error':
        typer.secho(f"Exiting with error code  : {error_code}",fg=typer.colors.RED)
        raise typer.Exit(code=error_code) 

    elif exit_style == 'Abort':
        typer.secho(f"Exiting with abort code  : {error_code}",fg=typer.colors.YELLOW)
        raise typer.Abort()

    else:
        typer.secho(f"just the normal completion!")  


if __name__ =='__main__':
    typer.run(main)
