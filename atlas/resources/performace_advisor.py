from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/performance-advisor/
"""


class PerformanceAdvisor(BaseApi):
    def get_process_namespaces(self, project_id, host, port, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/pa-namespaces-get-all/

        :param project_id:
        :param host:
        :param port:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/processes/{}:{}/performanceAdvisor/namespaces'.format(project_id, host, port),
            params=kwargs
        )

    def get_process_indexes(self, project_id, host, port, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/pa-existing-indexes-get-all/

        :param project_id:
        :param host:
        :param port:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/processes/{}:{}/performanceAdvisor/existingIndexes'.format(project_id, host, port),
            params=kwargs
        )

    def get_process_slow_queries(self, project_id, host, port, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/pa-get-slow-query-logs/

        :param project_id:
        :param host:
        :param port:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/processes/{}:{}/performanceAdvisor/slowQueryLogs'.format(project_id, host, port),
            params=kwargs
        )

    def get_process_suggested_indexes(self, project_id, host, port, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/pa-suggested-indexes-get-all/

        :param project_id:
        :param host:
        :param port:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/processes/{}:{}/performanceAdvisor/suggestedIndexes'.format(project_id, host, port),
            params=kwargs
        )


