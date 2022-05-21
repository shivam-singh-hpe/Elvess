import hvac
import logging


class Vault:

    def __init__(self):
        logging.basicConfig(level='DEBUG')
        self.logger = logging.getLogger(name=__name__)

    def fetch_from_vault(self, vault_token, url, path, username, password):
        """
        Function to fetch credentials from the vault server given the params

        :param vault_token: tvt value used for accessing vaulting server
        :param url: Url to vaulting server
        :param path: Path to where vaulting credentials are stored
        :param username: Username key used to access vaulted value
        :param password: Password key used to access vaulted value
        :return: Vaulted username and Password
        """
        # Connect to vault
        vault_conn = hvac.Client(url, vault_token)
        # Read from the path
        vault_data = vault_conn.read(path)

        # Access your credentials
        if vault_data is not None:
            vault_username = vault_data.get('data').get(username)
            vault_password = vault_data.get('data').get(password)
        else:
            raise ValueError('Path does not exist')

        self.logger.info("Fetch from vault Successful\n")
        return vault_username, vault_password
