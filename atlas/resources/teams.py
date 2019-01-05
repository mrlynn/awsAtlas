from atlas import BaseApi

"""
https://docs.atlas.mongodb.com/reference/api/teams/
"""


class Teams(BaseApi):
    def get_teams(self, org_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-get-all/

        :param org_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/teams'.format(org_id),
            params=kwargs
        )

    def get_team(self, org_id, team_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-get-one-by-id/

        :param org_id:
        :param team_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/teams/{}'.format(org_id, team_id),
            params=kwargs
        )

    def get_team_by_name(self, org_id, team_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-get-one-by-name/

        :param org_id:
        :param team_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/teams/byName/{}'.format(org_id, team_name),
            params=kwargs
        )

    def get_users_in_team(self, org_id, team_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-get-all-users/

        :param org_id:
        :param team_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/teams/{}/users'.format(org_id, team_id),
            params=kwargs
        )

    def create_team(self, org_id, team_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-create-one/

        :param org_id:
        :param team_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/orgs/{}/teams'.format(org_id),
            team_doc,
            params=kwargs
        )

    def rename_team(self, org_id, team_id, team_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-rename-one/

        :param org_id:
        :param team_id:
        :param team_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/orgs/{}/teams/{}'.format(org_id, team_id),
            team_doc,
            params=kwargs
        )

    def add_user_to_team(self, org_id, team_id, user_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-add-user/

        :param org_id:
        :param team_id:
        :param user_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/orgs/{}/teams/{}/users'.format(org_id, team_id),
            user_doc,
            params=kwargs
        )

    def delete_team(self, org_id, team_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-delete-one/

        :param org_id:
        :param team_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/orgs/{}/teams/{}'.format(org_id, team_id),
            params=kwargs
        )

    def remove_team_from_project(self, project_id, team_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-remove-from-project/

        :param project_id:
        :param team_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/teams/{}'.format(project_id, team_id),
            params=kwargs
        )

    def remove_user_from_team(self, org_id, team_id, user_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-remove-user/

        :param org_id:
        :param team_id:
        :param user_id:
        :return:
        """
        return self._delete(
            '/orgs/{}/teams/{}/users/{}'.format(org_id, team_id, user_id),
            params=kwargs
        )
