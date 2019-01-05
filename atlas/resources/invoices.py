from atlas import BaseApi

"""
https://docs.atlas.mongodb.com/reference/api/invoices/
"""

class Invoices(BaseApi):
    def get_all_invoices(self, org_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-all-invoices/

        :param org_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/invoices'.format(org_id),
            params=kwargs
        )

    def get_invoice(self, org_id, invoice_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-one-invoice/

        :param org_id:
        :param invoice_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/invoices/{}'.format(org_id, invoice_id),
            params=kwargs
        )

    def get_pending_invoices(self, org_id, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-pending-invoices/

        :param org_id:
        :param kwargs:
        :return:
        """
        return self._get(
            '/orgs/{}/invoices/pending'.format(org_id),
            params=kwargs
        )
