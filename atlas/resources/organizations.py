from atlas import BaseApi


class Organizations(BaseApi):
    def get_organizations(self, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-all/

        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs',
            params=kwargs
        )

    def get_organization(self, org_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-one/

        :param org_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}'.format(org_id),
            params=kwargs
        )

    def get_organization_users(self, org_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-users-get-all-users/

        :param org_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/users'.format(org_id),
            params=kwargs
        )

    def create_organization(self, org_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-create-one/

        :param org_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/orgs',
            org_doc,
            params=kwargs
        )

    def rename_organization(self, org_id, org_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-create-one/

        :param org_id:
        :param org_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/orgs/{}'.format(org_id),
            org_doc,
            params=kwargs
        )

    def delete_organization(self, org_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-delete-one/

        :param org_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/orgs/{}'.format(org_id),
            params=kwargs
        )

    def get_projects_in_organization(self, group_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-all-projects/

        :param group_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/groups'.format(group_id),
            params=kwargs
        )
