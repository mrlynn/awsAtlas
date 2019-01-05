from atlas import BaseApi

"""
https://docs.atlas.mongodb.com/reference/api/custom-roles/
retrieve, create, modify, delete custom roles
"""


class CustomRoles(BaseApi):
    def get_custom_roles(self, group_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/custom-roles-get-all-roles/

        :param group_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/customDBRoles/roles'.format(group_id),
            params=kwargs
        )

    def get_custom_role(self, group_id, role_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/custom-roles-get-single-role/

        :param group_id:
        :param role_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/customDBRoles/roles/{}'.format(group_id, role_id),
            params=kwargs
        )

    def create_custom_role(self, group_id, role_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/custom-roles-create-a-role/

        :param group_id:
        :param role_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/customDBRoles/roles'.format(group_id),
            role_doc,
            params=kwargs
        )

    def update_custom_role(self, group_id, role_id, role_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/custom-roles-update-a-role/

        :param group_id:
        :param role_id:
        :param role_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/customDBRoles/roles/{}'.format(group_id, role_id),
            role_doc,
            params=kwargs
        )

    def delete_custom_role(self, group_id, role_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/custom-roles-delete-a-role/

        :param group_id:
        :param role_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/customDBRoles/roles/{}'.format(group_id, role_id),
            params=kwargs
        )
