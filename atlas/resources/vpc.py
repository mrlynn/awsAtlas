from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/vpc/
"""


class Vpc(BaseApi):
    def get_cloud_containers(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-get-containers-list/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/containers'.format(project_id),
            params=kwargs
        )

    def create_cloud_container(self, project_id, container_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-create-container/

        :param project_id:
        :param container_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/containers'.format(project_id),
            container_doc,
            params=kwargs
        )

    def get_cloud_container(self, project_id, container_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-get-container/

        :param project_id:
        :param container_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/containers/{}'.format(project_id, container_id),
            params=kwargs
        )

    def update_cloud_container(self, project_id, container_id, container_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-update-container/

        :param project_id:
        :param container_id:
        :param container_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/containers/{}'.format(project_id, container_id),
            container_doc,
            params=kwargs
        )

    def get_vpc_peering_connections(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-get-connections-list/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/peers'.format(project_id),
            params=kwargs
        )

    def create_vpc_peering_connection(self, project_id, peer_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-create-peering-connection/

        :param project_id:
        :param peer_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/peers'.format(project_id),
            peer_doc,
            params=kwargs
        )

    def get_vpc_peering_connection(self, project_id, peer_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-get-connection/

        :param project_id:
        :param peer_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/peers/{}'.format(project_id, peer_id),
            params=kwargs
        )

    def modify_vpc_peering_connection(self, project_id, peer_id, peer_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-update-peering-connection/

        :param project_id:
        :param peer_id:
        :param peer_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/peers/{}'.format(project_id, peer_id),
            peer_doc,
            params=kwargs
        )

    def delete_vpc_peering_connection(self, project_id, peer_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-delete-peering-connection/

        :param project_id:
        :param peer_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/peers/{}'.format(project_id, peer_id),
            params=kwargs
        )
