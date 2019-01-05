from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/auditing/
"""


class Auditing(BaseApi):
    def get_audit_configuration(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/auditing-get-auditLog/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/auditLog'.format(project_id),
            params=kwargs
        )

    def configure_auditing(self, project_id, audit_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/auditing-set-auditLog/

        :param project_id:
        :param audit_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/auditLog'.format(project_id),
            audit_doc,
            params=kwargs
        )
