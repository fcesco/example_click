from services import predictions

import click


@click.group()
def cli():
    """cli tool"""
    pass


@cli.command()
def run_predictions():
    predictions.main()


if __name__ == "__main__":
    cli()
