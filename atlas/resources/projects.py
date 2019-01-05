from atlas import BaseApi

"""
https://docs.atlas.mongodb.com/reference/api/projects/
"""


class Projects(BaseApi):
    def get_projects(self, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/project-get-all/

        :param kwargs:
        :return:
        """
        return self._get(
            '/groups',
            params=kwargs
        )

    def get_project(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/project-get-one/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}'.format(project_id),
            params=kwargs
        )

    def get_project_by_name(self, project_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/project-get-one-by-name/

        :param project_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/byName/{}'.format(project_name),
            params=kwargs
        )

    def create_project(self, project_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/project-create-one/

        :param project_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups',
            project_doc,
            params=kwargs
        )

    def delete_project(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/project-delete-one/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}'.format(project_id),
            params=kwargs
        )

    def get_project_teams(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/project-get-teams/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/teams'.format(project_id),
            params=kwargs
        )

    def add_team_to_project(self, project_id, team_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/project-add-team/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/teams'.format(project_id),
            team_doc,
            params=kwargs
        )
