# -*- coding: utf-8 -*-

from zeep import Client
from zeep.wsse.username import UsernameToken

__author__ = 'lundberg'


class MitekMobileVerifyService(object):

    def __init__(self, wsdl, username, password, transport=None, service_name=None, port_name=None, plugins=None):
        self.authentication = UsernameToken(username, password, use_digest=False)  # XXX digest true or false?
        self.client = Client(wsdl=wsdl, wsse=self.authentication, transport=transport, service_name=service_name,
                             port_name=port_name, plugins=plugins)

    def verify(self, request, device_metadata, metadata, mibi_data_header):
        """
        :param request: Photo verification request
        :type request: mitek_mobile_verify.models.requests.PhotoVerifyBaseRequest
        :param device_metadata: Agent metadata
        :type device_metadata: mitek_mobile_verify.models.headers.DeviceMetadata
        :param metadata: Web request metadata
        :type metadata: mitek_mobile_verify.models.headers.WebRequestMetadataHeader
        :param mibi_data_header: Mibi data header
        :type mibi_data_header: mitek_mobile_verify.models.headers.MibiDataHeader
        :return:
        :rtype:
        """
        headers = {
            'DeviceMetaData': device_metadata.to_dict(),
            'Metadata': metadata.to_dict(),
            'MibiDataHeader': mibi_data_header.to_dict()
        }
        # Verify(DocumentRequest: DocumentRequest, _soapheaders={DeviceMetaData: DeviceMetaData(), Metadata: Metadata(), MibiDataHeader: MibiDataHeader()})
        self.client.service.Verify(request.create_request_dict(), _soapheaders=headers)

