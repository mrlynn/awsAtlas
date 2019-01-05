from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/encryption-at-rest/
"""

class EncryptionAtRest(BaseApi):
    def enable_encryption_at_rest(self, project_id, enc_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/enable-configure-encryptionatrest/

        :param project_id:
        :param enc_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/encryptionAtRest'.format(project_id),
            enc_doc,
            params=kwargs
        )

    def get_encryption_at_rest_config(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/get-configuration-encryptionatrest/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/encryptionAtRest'.format(project_id),
            params=kwargs
        )
