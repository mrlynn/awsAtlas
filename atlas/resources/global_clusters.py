from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/global-clusters/
"""


class GlobalClusters(BaseApi):
    def get_global_clusters(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-retrieve-namespaces/

        :param group_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/clusters/{}/globalWrites'.format(project_id, cluster_name),
            params=kwargs
        )

    def add_managed_namespace_to_global_cluster(self, project_id, cluster_name, namespace_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-add-namespace/

        :param project_id:
        :param cluster_name:
        :param namespace_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/clusters/{}/globalWrites/managedNamespaces'.format(project_id, cluster_name),
            namespace_doc,
            params=kwargs
        )

    def delete_managed_namespace_from_global_cluster(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-delete-namespace/
        TODO: error management

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        if 'collection' not in kwargs:
            raise Exception('collection required in kwargs')
        if 'db' not in kwargs:
            raise Exception('db required in kwargs')

        return self._delete(
            '/groups/{}/clusters/{}/globalWrites/managedNamespaces'.format(project_id, cluster_name),
            params=kwargs
        )

    def add_custom_zone_mapping(self, project_id, cluster_name, zone_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-add-customzonemapping/

        :param project_id:
        :param cluster_name:
        :param zone_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/clusters/{}/globalWrites/customZoneMapping'.format(project_id, cluster_name),
            zone_doc,
            params=kwargs
        )

    def delete_custom_zone_mapping(self, project_id, cluster_name, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-delete-customzonemappings/

        :param project_id:
        :param cluster_name:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/clusters/{}/globalWrites/customZoneMapping'.format(project_id, cluster_name),
            params=kwargs
        )
