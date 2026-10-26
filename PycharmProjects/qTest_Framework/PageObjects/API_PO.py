

class API_PO:

    def __init__(self, env_name, url, auth_token):
        self.env_name = env_name
        self.url = url
        self.auth_token = auth_token

    def api_po_get_env_name(self):
        return self.env_name

    def api_po_get_url(self):
        return self.url

    def api_po_get_auth_token(self):
        return self.auth_token