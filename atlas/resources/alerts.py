from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/alerts/
"""


class Alerts(BaseApi):
    def get_all_alerts(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alerts-get-all-alerts/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/alerts'.format(project_id),
            params=kwargs
        )

    def get_alert(self, project_id, alert_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alerts-get-alert/

        :param project_id:
        :param alert_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/alerts/{}'.format(project_id, alert_id),
            params=kwargs
        )

    def acknowledge_alert(self, project_id, alert_id, ack_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alerts-acknowledge-alert/

        :param project_id:
        :param alert_id:
        :param ack_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/alerts/{}'.format(project_id, alert_id),
            ack_doc,
            params=kwargs
        )
