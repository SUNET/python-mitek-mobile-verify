# -*- coding: utf-8 -*-

from zeep import Client
from zeep.wsse.username import UsernameToken

__author__ = 'lundberg'


class MitekMobileVerifyService(object):

    def __init__(self, wsdl, username, password, transport=None, service_name=None, port_name=None, plugins=None):
        self.authentication = UsernameToken(username, password, use_digest=False)  # XXX digest true or false?
        self.client = Client(wsdl=wsdl, wsse=self.authentication, transport=transport, service_name=service_name,
                             port_name=port_name, plugins=plugins)

    def verify(self, request, device_metadata=dict, metadata=dict, mibi_data_header=dict):
        headers = {
            'DeviceMetaData': device_metadata,
            'Metadata': metadata,
            'MibiDataHeader': mibi_data_header
        }
        # Verify(DocumentRequest: DocumentRequest, _soapheaders={DeviceMetaData: DeviceMetaData(), Metadata: Metadata(), MibiDataHeader: MibiDataHeader()})
        self.client.service.Verify(request.create_request_dict(), _soapheaders=[headers])

