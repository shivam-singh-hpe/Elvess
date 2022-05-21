import json
import requests
import logging


class Authentication:
    def __init__(self):
        logging.basicConfig(level='DEBUG')
        self.logger = logging.getLogger(name=__name__)

    def authenticate(self, username, password, host_name):
        """
        Function used to create the iiam-cookie using the username and password credentials and host name path

        :param username: Vaulted username used for authentication
        :param password: Vaulted password used for authentication
        :param host_name: Host name used for path
        :return: Authentication Cookie with no tenant id
        """
        url = host_name + "/auth/authenticate"
        body = {'accessKey': username, 'secretKey': password}
        payload = json.dumps(body)
        headers = {
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        self.logger.info("\nAuthentication In Progress\n")
        response.status_code == requests.codes.ok
        return response.cookies['infosight_iam']

    def get_tenant_id(self, auth_iam_cookie, account_id, host_name):
        """
        currentUserTenantSearch graphql api call
        Function used to get the tenant id given the cookie, host name, and account id from a graphql api call
        Search by name across all Tenants for which the current User has access

        :param auth_iam_cookie: Used for authentication
        :param account_id: Used to pull tenant id for this specific account id
        :param host_name: Host name used for path
        :return: Tenant Id
        """
        url = host_name + "/InfoSight/api/iam/graphql"
        iam_cookie = "infosight_iam=" + auth_iam_cookie
        headers = {
            'cookie': iam_cookie,
            'Content-Type': "application/json",
            'Accept': "*/*"
        }
        query = '''
            {
             currentUserTenantSearch(searchTerm:"urn:nimble:%s") { 
                 id
                 name
                    claims {
                      urn
                    } 
                } 
            }''' % account_id
        payload = {
            'query': query
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        resp = json.loads(response.content)
        self.logger.info("\n *****API RESPONSE*** \n %s", response.text)
        self.logger.info("\n Fetching Tenant Id\n")
        response.status_code == requests.codes.ok
        return resp['data']['currentUserTenantSearch'][0]['id']

    def set_tenant_id(self, auth_iam_cookie, tenant_id, host_name):
        """
        Set tenant graphql api call
        Changes the active tenant and refreshes the infosight_iam cookie. If an IAM tenant is not found the infosight_iam
        cookie is still refreshed, but the claim tokens and tenant properties will be null

        :param auth_iam_cookie: Used for authentication
        :param tenant_id: Added into cookie for authentication
        :param host_name: Host name used for path
        :return: tenant_iam_cookie used for any api calls
        """
        url = host_name + "/InfoSight/api/iam/graphql"
        iam_cookie = "infosight_iam=" + auth_iam_cookie
        headers = {
            'cookie': iam_cookie,
            'Content-Type': "application/json",
            'Accept': "*/*"
        }
        query = """
                 mutation  ($tenantId: ID) {
                    setTenant(tenantId: $tenantId) {
                    identityProvider
                    userId
                    userName
                    tenantId
                    tenantName
                    userRole
                    userRealm
                    claimTags
                    oculusRoles
            }
        }
                """
        variable = {'tenantId': tenant_id}
        payload = {
            'query': query,
            'variables': variable
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        self.logger.info("\nAuthentication Complete\n")
        response.status_code == requests.codes.ok
        return response.cookies['infosight_iam']
