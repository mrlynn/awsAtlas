from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/api-key/
"""


class UserApiKeys(BaseApi):
    def get_api_keys(self, user_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/api-key-get-all/
        TODO: bug in documentation (POST should be a GET)

        :param user_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/users/{}/keys'.format(user_id),
            params=kwargs
        )

    def create_api_key(self, user_id, key_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/create-api-key/

        :param user_id:
        :param key_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/users/{}/keys'.format(user_id),
            key_doc,
            params=kwargs
        )

    def update_api_key_state(self, user_id, key_id, state_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/enable-disable-api-key/

        :param user_id:
        :param key_id:
        :param state_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/users/{}/keys/{}'.format(user_id, key_id),
            state_doc,
            params=kwargs
        )

    def disable_api_key(self, user_id, key_id):
        return self.update_api_key_state(user_id, key_id, {'enabled': False})

    def enable_api_key(self, user_id, key_id):
        return self.update_api_key_state(user_id, key_id, {'enabled': True})

    def delete_api_key(self, user_id, key_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/delete-api-key/

        :param user_id:
        :param key_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/users/{}/keys/{}'.format(user_id, key_id),
            params=kwargs
        )
