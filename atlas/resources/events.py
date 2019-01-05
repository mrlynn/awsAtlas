from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/events/
"""


class Events(BaseApi):
    def get_organization_events(self, org_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/events-orgs-get-all/

        :param org_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/events'.format(org_id),
            params=kwargs
        )

    def get_organization_event(self, org_id, event_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/events-orgs-get-one/

        :param org_id:
        :param event_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/events/{}'.format(org_id, event_id),
            params=kwargs
        )

    def get_project_events(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/events-projects-get-all/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/events'.format(project_id),
            params=kwargs
        )

    def get_project_event(self, project_id, event_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/events-projects-get-one/

        :param project_id:
        :param event_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/events/{}'.format(project_id, event_id),
            params=kwargs
        )
