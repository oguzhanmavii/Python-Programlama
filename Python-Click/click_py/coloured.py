import click


@click.command()
def coloured():
    click.secho('Hello there', fg="blue", bold=True)


if __name__ == '__main__':
    coloured()