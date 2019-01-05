from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-schedule/
"""


class CloudProviderSnapshotSchedule(BaseApi):
    def get_cloud_provider_snapshot_schedule(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-schedule-get-all/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/backup/schedule'.format(project_id, cluster_name),
            params=kwargs
        )

    def modify_cloud_provider_snapshot_schedule(self, project_id, cluster_name, schedule_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-schedule-modify-one/

        :param project_id:
        :param cluster_name:
        :param schedule_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/clusters/{}/backup/schedule'.format(project_id, cluster_name),
            schedule_doc,
            params=kwargs
        )
