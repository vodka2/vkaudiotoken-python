class VkClient(object):
    def __init__(self, user_agent, client_secret, client_id):
        self._user_agent = user_agent
        self._client_secret = client_secret
        self._client_id = client_id

    @property
    def user_agent(self):
        return self._user_agent

    @property
    def client_secret(self):
        return self._client_secret

    @property
    def client_id(self):
        return self._client_id
