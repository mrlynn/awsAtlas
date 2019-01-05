from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/database-users/
The databaseUsers resource lets you modify the mongodb users in 
the cluster
"""


class DatabaseUsers(BaseApi):
    def get_all_db_users(self, group_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-get-all-users/

        :param group_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/databaseUsers'.format(group_id),
            params=kwargs
        )

    def get_db_user(self, group_id, username, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-get-single-user/

        :param group_id:
        :param username:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/databaseUsers/admin/{}'.format(group_id, username),
            params=kwargs
        )

    def create_db_user(self, group_id, user_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-create-a-user/

        :param group_id:
        :param user_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/databaseUsers'.format(group_id),
            user_doc,
            params=kwargs
        )

    def update_db_user(self, group_id, username, user_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-update-a-user/

        :param group_id:
        :param username:
        :param user_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/databaseUsers/admin/{}'.format(group_id, username),
            user_doc,
            params=kwargs
        )

    def delete_db_user(self, group_id, username, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-delete-a-user/

        :param group_id:
        :param username:
        :param kwargs:
        :return:
        """
        return self._delete('/groups/{}/databaseUsers/admin/{}'.format(group_id, username), params=kwargs)
