from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/snapshot-schedule/
"""


class ContinuousBackupSnapshotSchedule(BaseApi):
    def get_continuous_backup_snapshot_schedule(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshot-schedule-get/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/snapshotSchedule'.format(project_id, cluster_name),
            params=kwargs
        )

    def update_continuous_backup_snapshot_schedule(self, project_id, cluster_name, schedule_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshot-schedule-patch/

        :param project_id:
        :param cluster_name:
        :param schedule_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/clusters/{}/snapshotSchedule'.format(project_id, cluster_name),
            schedule_doc,
            params=kwargs
        )
