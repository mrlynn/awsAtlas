from atlas import BaseApi

"""
https://docs.atlas.mongodb.com/reference/api/clusters/
"""


class Clusters(BaseApi):
    def get_clusters(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-get-all/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters'.format(project_id),
            params=kwargs
        )

    def get_cluster(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-get-one/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}'.format(project_id, cluster_name),
            params=kwargs
        )

    def get_cluster_advanced_configs(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-get-advanced-configuration-options/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/processArgs'.format(project_id, cluster_name),
            params=kwargs
        )

    def create_cluster(self, project_id, cluster_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-create-one/

        :param proejct_id:
        :param cluster_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/clusters'.format(project_id),
            cluster_doc,
            params=kwargs
        )

    def modify_cluster(self, project_id, cluster_name, cluster_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-modify-one/

        :param project_id:
        :param cluster_name:
        :param cluster_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/clusters/{}'.format(project_id, cluster_name),
            cluster_doc,
            params=kwargs
        )

    def modify_cluster_advanced_config(self, project_id, cluster_name, config_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-modify-advanced-configuration-options/

        :param project_id:
        :param cluster_name:
        :param config_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/clusters/{}/processArgs'.format(project_id, cluster_name),
            config_doc,
            params=kwargs
        )

    def delete_cluster(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-delete-one/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/clusters/{}'.format(project_id, cluster_name),
            params=kwargs
        )
