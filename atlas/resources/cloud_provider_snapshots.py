from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot/
"""


class CloudProviderSnapshots(BaseApi):
    def get_cloud_provider_snapshots(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-get-all/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/backup/snapshots'.format(project_id, cluster_name),
            params=kwargs
        )

    def get_cloud_provider_snapshot(self, project_id, cluster_name, snapshot_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-get-one/

        :param project_id:
        :param cluster_name:
        :param snapshot_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/backup/snapshots/{}'.format(project_id, cluster_name, snapshot_id),
            params=kwargs
        )

    def delete_cloud_provider_snapshot(self, project_id, cluster_name, snapshot_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-delete-one/

        :param project_id:
        :param cluster_name:
        :param snapshot_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/clusters/{}/backup/snapshots/{}'.format(project_id, cluster_name, snapshot_id),
            params=kwargs
        )
