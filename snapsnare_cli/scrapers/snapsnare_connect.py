from snapsnare_cli.system import utils
from snapsnare_cli.system.requestors import RestRequest, BearerRequest


class SnapsnareConnect:
    def __init__(self, identity):
        self.__identity = identity

        settings = utils.load_json('snapsnare.json')
        snapsnare_api = settings['snapsnare-api']
        self.__endpoint = snapsnare_api['endpoint']
        self.__proxies = snapsnare_api.get('proxies')

    def get_identity(self):
        return self.__identity

    def get_endpoint(self):
        return self.__endpoint

    def get_proxies(self):
        return self.__proxies

    def _auth(self):
        endpoint = self.get_endpoint()
        url = f"{endpoint}/auth"
        identity = self.get_identity()

        proxies = self.get_proxies()
        request = RestRequest(proxies=proxies)
        response = request.post(url, identity)
        content = response.json()
        return content.get('access_token')

    def create_jammers(self, jammers):
        access_token = self._auth()
        endpoint = self.get_endpoint()
        url = f"{endpoint}/jamulus/jammers/create"

        proxies = self.get_proxies()
        request = BearerRequest(access_token, proxies=proxies)
        response = request.post(url, jammers)
        content = response.json()
        return content.get('uuid')

    def create_icecast_status(self, source):
        access_token = self._auth()
        endpoint = self.get_endpoint()
        url = f"{endpoint}/icecast/statuses/create"

        proxies = self.get_proxies()
        request = BearerRequest(access_token, proxies=proxies)
        response = request.post(url, source)
        content = response.json()
        return content.get('uuid')
