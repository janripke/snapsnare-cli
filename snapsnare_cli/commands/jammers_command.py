import click
import os
import logging
from snapsnare_cli.commands.command import Command
from snapsnare_cli.system import utils
from snapsnare_cli.scrapers.snapsnare_connect import SnapsnareConnect


class JammersCommand(Command):
    @click.command()
    @click.option('-m', '--htmlstatus', required=False, default='status.html')
    @click.option('-u', '--username', required=True)
    @click.option('-p', '--password', required=True)
    def execute(htmlstatus, username, password):

        identity = {
            'username': username,
            'password': password
        }

        snapsnare_connect = SnapsnareConnect(identity)

        # if no filename is given, status.html is assumed in the folder you are running this script from
        content = utils.load(htmlstatus)

        jammers = {
            'jammers': content
        }

        snapsnare_connect.create_jammers(jammers)
        logging.debug(jammers)
