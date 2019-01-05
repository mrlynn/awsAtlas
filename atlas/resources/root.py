from atlas import BaseApi
"""
    https://docs.atlas.mongodb.com/reference/api/root/
    The root resource is the starting point for the atlas API
"""


class Root(BaseApi):
    def get_root(self, **kwargs):
        """
        GET https://cloud.mongodb.com/api/atlas/v1.0/

        :param kwargs: supports
        1. pretty - boolean (false) - displays response in pretty print format
        2. envelope = boolean (false) - should we wrap the response in an envelope
        :return:
        """
        return self._get('/', params=kwargs)