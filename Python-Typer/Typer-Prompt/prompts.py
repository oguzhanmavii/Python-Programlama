import typer

def main():
    wdyw= typer.prompt("What do you want?")
    typer.echo(f"I want: {wdyw}")
    do_you_really_want= typer.confirm(f"Do you really want [y/N]:")
    if do_you_really_want:
        typer.echo("You shall have it!")
    else:
        typer.echo("No you shall not have it!")    

    do_you_really_want_abort = typer.confirm(f"Do you really want: {do_you_really_want}",abort=True)
    typer.echo("Only yes reveals it!")

if __name__ == '__main__':
    typer.run(main)

