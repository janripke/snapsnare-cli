from snapsnare_cli.system import utils
from snapsnare_cli.system.requestors import RestRequest, BearerRequest


class IcecastConnect:
    def __init__(self):

        settings = utils.load_json('snapsnare.json')
        api = settings.get('icecast-api')
        self.__proxies = api.get('proxies')
        self.__endpoint = None
        if api:
            self.__endpoint = api.get('endpoint')

    def get_endpoint(self):
        return self.__endpoint

    def has_endpoint(self):
        endpoint = self.get_endpoint()
        if endpoint:
            return True
        return False

    def get_proxies(self):
        return self.__proxies

    def status(self):
        endpoint = self.get_endpoint()
        url = f"{endpoint}/status-json.xsl"

        proxies = self.get_proxies()
        request = RestRequest(proxies=proxies)
        response = request.get(url)
        content = response.json()
        return content
