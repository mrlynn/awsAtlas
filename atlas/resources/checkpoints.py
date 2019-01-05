from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/checkpoints/
"""


class Checkpoints(BaseApi):
    def get_checkpoints(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/checkpoints-get-all/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/backupCheckpoints'.format(project_id, cluster_name),
            params=kwargs
        )

    def get_checkpoint(self, project_id, cluster_name, checkpoint_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/checkpoints-get-one/

        :param project_id:
        :param cluster_name:
        :param checkpoint_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/backupCheckpoints/{}'.format(project_id, cluster_name, checkpoint_id),
            params=kwargs
        )
