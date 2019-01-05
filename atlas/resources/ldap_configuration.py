from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/ldaps-configuration/
"""


class LdapConfiguration(BaseApi):
    def verify_ldap_config(self, project_id, ldap_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-request-verification/
        TODO: introduce error for failed validation?

        :param project_id:
        :param ldap_doc:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/userSecurity/ldap/verify'.format(project_id),
            ldap_doc,
            params=kwargs
        )

    def get_most_recent_ldap_verification(self, project_id, request_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-verification-status/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/userSecurity/ldap/verify/{}'.format(project_id, request_id),
            {},
            params=kwargs
        )

    def save_ldap_configuration(self, project_id, ldap_doc, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-save/

        :param project_id:
        :param ldap_doc:
        :param kwargs:
        :return:
        """
        return self._patch(
            '/groups/{}/userSecurity'.format(project_id),
            ldap_doc,
            params=kwargs
        )

    def get_ldap_configuration(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-get-current/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/userSecurity'.format(project_id),
            params=kwargs
        )

    def delete_user_to_dn_mapping(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-remove-usertodnmapping/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/userSecurity'.format(project_id),
            params=kwargs
        )
