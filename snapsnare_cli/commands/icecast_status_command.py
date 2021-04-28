import click
import logging
from pprint import pprint
from snapsnare_cli.commands.command import Command
from snapsnare_cli.scrapers.snapsnare_connect import SnapsnareConnect
from snapsnare_cli.scrapers.icecast_connect import IcecastConnect


class IcecastStatusCommand(Command):
    @click.command()
    @click.option('-u', '--username', required=True)
    @click.option('-p', '--password', required=True)
    def execute(username, password):
        icecast_connect = IcecastConnect()

        if icecast_connect.has_endpoint():

            response = icecast_connect.status()
            icestats = response.get('icestats')
            source = icestats.get('source')

            source_ = {
                'source': source
            }

            identity = {
                'username': username,
                'password': password
            }

            snapsnare_connect = SnapsnareConnect(identity)
            uuid = snapsnare_connect.create_icecast_status(source_)
            logging.debug(uuid)
