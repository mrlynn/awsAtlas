from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/user/
"""


class AtlasUsers(BaseApi):
    def get_atlas_user(self, user_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/user-get-by-id/

        :param user_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/users/{}'.format(user_id),
            params=kwargs
        )

    def get_atlas_user_by_name(self, username, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/user-get-one-by-name/

        :param username:
        :param kwargs:
        :return:
        """
        return self._get(
            '/users/byName/{}'.format(username),
            params=kwargs
        )

    def create_atlas_user(self, user_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/user-create/

        :param user_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/users',
            user_doc,
            **kwargs
        )

    def update_atlas_user(self, user_id, user_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/user-update/

        :param user_id:
        :param user_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/users/{}'.format(user_id),
            user_doc,
            params=kwargs
        )
