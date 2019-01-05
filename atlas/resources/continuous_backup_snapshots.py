from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/snapshots/
"""


class ContinuousBackupSnapshots(BaseApi):
    def get_continuous_backup_snapshots(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshots-get-all/

        :param project_id:
        :param cluster_name:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/snapshots'.format(project_id, cluster_name),
            params=kwargs
        )

    def get_continuous_backup_snapshot(self, project_id, cluster_name, snapshot_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshots-get-one/

        :param project_id:
        :param cluster_name:
        :param snapshot_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/snapshots/{}'.format(project_id, cluster_name, snapshot_id),
            params=kwargs
        )

    def change_continuous_backup_snapshot_expiration(
            self,
            project_id,
            cluster_name,
            snapshot_id,
            expiry_doc,
            **kwargs
    ):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshots-change-expiration/

        TODO: check expiry doc for validity?

        :param project_id:
        :param cluster_name:
        :param snapshot_id:
        :param expiry_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/clusters/{}/snapshots/{}'.format(project_id, cluster_name, snapshot_id),
            expiry_doc,
            params=kwargs
        )

    def delete_continuous_backup_snapshot(self, project_id, cluster_name, snapshot_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshots-delete-one/

        :param project_id:
        :param cluster_name:
        :param snapshot_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/clusters/{}/snapshots/{}'.format(project_id, cluster_name, snapshot_id),
            params=kwargs
        )
