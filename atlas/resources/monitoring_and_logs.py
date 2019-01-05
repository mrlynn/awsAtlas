from atlas import BaseApi
"""
https://docs.atlas.mongodb.com/reference/api/monitoring-and-logs/
"""


class Monitoring(BaseApi):
    def get_processes(self, project_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/processes-get-all/

        :param project_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/processes'.format(project_id),
            params=kwargs
        )

    def get_process(self, project_id, host, port, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/processes-get-one/

        :param project_id:
        :param host:
        :param port:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/processes/{}:{}'.format(project_id, host, port),
            params=kwargs
        )

    def get_process_measurement(self, project_id, host, port, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/process-measurements/
        TODO: introduce measurement checks in kwargs

        :param project_id:
        :param host:
        :param port:
        :param kwargs:
        :return:
        """
        if 'granularity' not in kwargs:
            raise Exception('granularity expected in kwargs')
        if 'period' not in kwargs:
            raise Exception('period expected in kwargs')
        if 'start' not in kwargs:
            raise Exception('start expected in kwargs')
        if 'end' not in kwargs:
            raise Exception('end expected in kwargs')
        return self._get(
            '/groups/{}/processes/{}:{}/measurements'.format(project_id, host, port),
            params=kwargs
        )

    def get_process_databases(self, project_id, host, port, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/process-databases/

        :param project_id:
        :param host:
        :param port:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/processes/{}:{}/databases'.format(project_id, host, port),
            params=kwargs
        )

    def get_process_database_measurements(self, project_id, host, port, database_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/process-databases-measurements/

        :param project_id:
        :param host:
        :param port:
        :param database_id:
        :param kwargs:
        :return:
        """
        if 'granularity' not in kwargs:
            raise Exception('granularity expected in kwargs')
        if 'period' not in kwargs:
            raise Exception('period expected in kwargs')
        if 'start' not in kwargs:
            raise Exception('start expected in kwargs')
        if 'end' not in kwargs:
            raise Exception('end expected in kwargs')
        return self._get(
            '/groups/{}/processes/{}:{}/databases/{}/measurements'.format(project_id, host, port, database_id),
            params=kwargs
        )

    def get_process_disks(self, project_id, host, port, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/process-disks/

        :param project_id:
        :param host:
        :param port:
        :param kwargs:
        :return:
        """
        return self._get(
            '/groups/{}/processes/{}:{}/disks'.format(project_id, host, port),
            params=kwargs
        )

    def get_process_disk_measurement(self, project_id, host, port, disk, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/process-disks-measurements/

        :param project_id:
        :param host:
        :param port:
        :param disk:
        :param kwargs:
        :return:
        """
        if 'granularity' not in kwargs:
            raise Exception('granularity expected in kwargs')
        if 'period' not in kwargs:
            raise Exception('period expected in kwargs')
        if 'start' not in kwargs:
            raise Exception('start expected in kwargs')
        if 'end' not in kwargs:
            raise Exception('end expected in kwargs')
        return self._get(
            '/groups/{}/processes/{}:{}/disks/{}/measurements'.format(project_id, host, port, disk),
            params=kwargs
        )


class Logs(BaseApi):
    """
    https://docs.atlas.mongodb.com/reference/api/logs/

    TODO: this returns a gzip file (NEED TO HANDLE THIS)
    """
    def get_log(self, project_id, hostname, log_name, **kwargs):
        return self._get(
            '/groups/{}/clusters/{}/logs/{}'.format(project_id, hostname, log_name),
            params=kwargs
        )
