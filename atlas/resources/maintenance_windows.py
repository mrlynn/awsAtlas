from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/maintenance-windows/
"""


class MaintenanceWindows(BaseApi):
    def get_maintenance_window(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/maintenance-windows-view-in-one-project/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/maintenanceWindow'.format(project_id),
            params=kwargs
        )

    def update_maintenance_window(self, project_id, window_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/maintenance-window-update/

        :param project_id:
        :param window_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/maintenanceWindow'.format(project_id),
            window_doc,
            params=kwargs
        )

    def defer_maintenance_window(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/maintenance-window-defer/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/maintenanceWindow/defer'.format(project_id),
            {},
            params=kwargs
        )

    def reset_maintenance_window(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/maintenance-window-clear/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/maintenanceWindow'.format(project_id),
            params=kwargs
        )
