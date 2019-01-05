from atlas import BaseApi

"""
https://docs.atlas.mongodb.com/reference/api/whitelist/

support creating temporary whitelist entries that automatically expire within
a user configurable 7-day period
"""


class ProjectWhiteList(BaseApi):
    def get_whitelists(self, group_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-get-all/

        :param group_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/whitelist'.format(group_id),
            params=kwargs
        )

    def get_whitelist(self, group_id, wl_entry, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-get-one-entry/

        :param group_id:
        :param wl_entry:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/whitelist/{}'.format(group_id, wl_entry),
            params=kwargs
        )

    def update_whitelists(self, group_id, wl_entries, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-add-one/

        :param group_id:
        :param wl_entries:
        :param kwargs:
        :return:
        """
        return self._post(
            '/groups/{}/whitelist'.format(group_id),
            wl_entries,
            params=kwargs
        )

    def delete_whitelist(self, group_id, wl_entry, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-delete-one/

        :param group_id:
        :param wl_entry:
        :param kwargs:
        :return:
        """
        return self._delete(
            '/groups/{}/whitelist/{}'.format(group_id, wl_entry),
            params=kwargs
        )
