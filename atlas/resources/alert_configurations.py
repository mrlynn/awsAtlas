from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/alert-configurations/
"""


class AlertConfigurations(BaseApi):
    def get_alert_configurations(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-get-all-configs/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/alertConfigs'.format(project_id),
            params=kwargs
        )

    def create_alert_configuration(self, project_id, alert_config_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-create-config/

        :param project_id:
        :param alert_config_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/alertConfigs'.format(project_id),
            alert_config_doc,
            params=kwargs
        )

    def get_alert_configuration(self, project_id, alert_config_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-get-config/

        :param project_id:
        :param alert_config_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/alertConfigs/{}'.format(project_id, alert_config_id),
            params=kwargs
        )

    def update_alert_configuration(self, project_id, alert_config_id, alert_config_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-update-config/

        :param project_id:
        :param alert_config_id:
        :param alert_config_doc:
        :param kwargs:
        :return:
        """
        return self._put(
            '/groups/{}/alertConfigs/{}'.format(project_id, alert_config_id),
            alert_config_doc,
            params=kwargs
        )

    def update_alert_config_state(self, project_id, alert_config_id, state_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-enable-disable-config/

        :param project_id:
        :param alert_config_id:
        :param state_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/alertConfigs/{}'.format(project_id, alert_config_id),
            state_doc,
            params=kwargs
        )

    def enable_alert_config(self, project_id, config_id):
        return self.update_alert_config_state(project_id, config_id, {'enabled': True})

    def disable_alert_config(self, project_id, config_id):
        return self.update_alert_config_state(project_id, config_id, {'enabled': False})

    def delete_alert_configuration(self, project_id, config_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-delete-config/

        :param project_id:
        :param config_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/alertConfigs/{}'.format(project_id, config_id),
            params=kwargs
        )

    def get_open_alerts(self, project_id, config_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-get-open-alerts/

        :param project_id:
        :param config_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/alertConfigs/{}/alerts'.format(project_id, config_id),
            params=kwargs
        )
