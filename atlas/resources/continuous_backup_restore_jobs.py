from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/restore-jobs/
"""


class ContinuousBackupRestoreJobs(BaseApi):
    def get_continuous_backup_restore_jobs(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/restore-jobs-get-all/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/restoreJobs'.format(project_id, cluster_name),
            params=kwargs
        )

    def get_continuous_backup_restore_job(self, project_id, cluster_name, job_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/restore-jobs-get-one/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/restoreJobs/{}'.format(project_id, cluster_name, job_id),
            params=kwargs
        )

    def create_continuous_backup_restore_job(self, project_id, cluster_name, restore_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/restore-jobs-create-one/

        :param project_id:
        :param cluster_name:
        :param restore_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/clusters/{}/restoreJobs'.format(project_id, cluster_name),
            restore_doc,
            params=kwargs
        )
