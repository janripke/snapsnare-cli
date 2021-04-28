import click


class ClickCommand(click.MultiCommand):

    def list_commands(self, ctx):
        commands = list()
        commands.append('jamulus:jammers')
        commands.append('icecast:status')
        return commands

    def get_command(self, ctx, cmd_name):
        if cmd_name == "jamulus:jammers":
            from snapsnare_cli.commands.jammers_command import JammersCommand
            return JammersCommand.execute
        if cmd_name == "icecast:status":
            from snapsnare_cli.commands.icecast_status_command import IcecastStatusCommand
            return IcecastStatusCommand.execute
