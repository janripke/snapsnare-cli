import click
import snapsnare_cli
from snapsnare_cli.commands.click_command import ClickCommand


@click.command(cls=ClickCommand, invoke_without_command=True, no_args_is_help=True)
@click.option('-r', '--revision', is_flag=True, help="Report the version of snapsnare-cli and exit.")
@click.pass_context
def main(ctx, revision):

    if revision:
        print(f"{snapsnare_cli.__title__} version {snapsnare_cli.__version__}")
        ctx.exit()


if __name__ == '__main__':
    main()
