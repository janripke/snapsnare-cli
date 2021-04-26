import click


class ClickCommand(click.MultiCommand):

    def list_commands(self, ctx):
        commands = list()
        commands.append('markets')
        commands.append('orders')
        commands.append('trades')
        commands.append('journals')
        commands.append('mappings')
        return commands

    def get_command(self, ctx, cmd_name):
        if cmd_name == "jammers":
            from snapsnare_cli.commands.jammers_command import JammersCommand
            return JammersCommand.execute
