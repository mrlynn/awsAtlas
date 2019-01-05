from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/whitelist-api/
"""


class UserApiWhitelist(BaseApi):
    def get_api_whitelists(self, user_id, **kwargs):
        return self._get('/users/{}/whitelist'.format(user_id), params=kwargs)

    def get_api_whitelist(self, user_id, wl_entry, **kwargs):
        """
        supports both ip address and cidr block as the entry (see documentation)
        :param user_id:
        :param wl_entry:
        :param kwargs:
        :return:
        """
        return self._get('/users/{}/whitelist/{}'.format(user_id, wl_entry), params=kwargs)

    def add_api_whitelist(self, user_id, wl_doc, **kwargs):
        return self._post('/users/{}/whitelist'.format(user_id), wl_doc, params=kwargs)

    def delete_api_whitelist(self, user_id, wl_entry, **kwargs):
        """
        supports both ip address and cidr block as the entry (see documentation)

        :param user_id:
        :param wl_entry:
        :param kwargs:
        :return:
        """
        return self._delete('/users/{}/whitelist/{}'.format(user_id, wl_entry), params=kwargs)
