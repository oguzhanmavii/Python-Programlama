import typer
from time import sleep

def iteration():
    for i in range(1000):
        yield i

def main():
    with typer.progressbar(range(10)) as progress:
        for i in progress:
            sleep(0.1)
    with typer.progressbar(iteration(),length=1000,label="Processing users") as progress:
        for i in progress:
            sleep(0.01)

    with typer.progressbar(iteration(),length=1000, label="Processing another one ") as progress:
        for i in progress:
            sleep(0.01)
            progress.update(250)
    typer.echo("Complete") 


if __name__ =='__main__':
    typer.run(main)                           