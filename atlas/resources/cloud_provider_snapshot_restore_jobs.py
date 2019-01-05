from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs/
"""


class CloudProviderSnapshotRestoreJobs(BaseApi):
    def get_cloud_provider_snapshot_restore_jobs(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs-get-all/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/backup/restoreJobs'.format(project_id, cluster_name),
            params=kwargs
        )

    def get_cloud_provider_snapshot_restore_job(self, project_id, cluster_name, job_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs-get-one/

        :param project_id:
        :param cluster_name:
        :param job_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/backup/restoreJobs/{}'.format(project_id, cluster_name, job_id),
            params=kwargs
        )

    def create_cloud_provider_snapshot_restore_job(self, project_id, cluster_name, job_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs-create-one/

        :param project_id:
        :param cluster_name:
        :param job_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/clusters/{}/backup/restoreJobs/'.format(project_id, cluster_name),
            job_doc,
            params=kwargs
        )

    def cancel_cloud_provider_snapshot_restore_job(self, project_id, cluster_name, job_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs-delete-one/
        TODO: bug in documentation (GET is documented instead of DELETE)

        :param project_id:
        :param cluster_name:
        :param job_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/clusters/{}/backup/restoreJobs/{}'.format(project_id, cluster_name, job_id),
            params=kwargs
        )
