import click
import os
import pprint
from paprika_connector.connectors.connector_factory import ConnectorFactory
from snapsnare_cli.commands.command import Command
from snapsnare_cli.repositories.jammer.jammer_repository import JammerRepository
from snapsnare_cli.system import utils


class JammersCommand(Command):
    @click.command()
    @click.option('-m', '--htmlstatus', required=False, default='htmlstatus.html')
    def execute(htmlstatus):
        ds = utils.load_json('snapsnare-ds.json')
        connector = ConnectorFactory.create_connector(ds)
        jammer_repository = JammerRepository(connector)

        # use the environment variable JAMULUS home to find the location of the html status file.
        # the html status file contains the list of online jammers.
        # if no path is given /opt/jamulus is assumed (for testing purposes)
        jamulus_home = os.environ.get('JAMULUS_HOME', os.path.join(f'{os.sep}opt', 'jamulus'))
        content = utils.load(jamulus_home, htmlstatus)

        jammers = {
            'jammers': content
        }

        jammer_repository.insert(jammers)

        # print(f"{len(markets)} jammers written")
        connector.commit()
        connector.close()
