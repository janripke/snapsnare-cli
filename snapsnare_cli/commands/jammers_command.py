import click
import os
import logging
import pprint
from paprika_connector.connectors.connector_factory import ConnectorFactory
from snapsnare_cli.commands.command import Command
from snapsnare_cli.repositories.jammer.jammer_repository import JammerRepository
from snapsnare_cli.system import utils
from snapsnare_cli.scrapers.snapsnare_connect import SnapsnareConnect


class JammersCommand(Command):
    @click.command()
    @click.option('-m', '--htmlstatus', required=False, default='htmlstatus.html')
    @click.option('-u', '--username', required=True)
    @click.option('-p', '--password', required=True)
    def execute(htmlstatus, username, password):

        identity = {
            'username': username,
            'password': password
        }

        snapsnare_connect = SnapsnareConnect(identity)

        # use the environment variable JAMULUS home to find the location of the html status file.
        # the html status file contains the list of online jammers.
        # if no path is given /opt/jamulus is assumed (for testing purposes)
        jamulus_home = os.environ.get('JAMULUS_HOME', os.path.join(f'{os.sep}opt', 'jamulus'))
        content = utils.load(jamulus_home, htmlstatus)

        jammers = {
            'jammers': content
        }

        snapsnare_connect.create_jammers(jammers)
        logging.debug(jammers)