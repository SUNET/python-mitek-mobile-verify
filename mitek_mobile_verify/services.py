# -*- coding: utf-8 -*-

from zeep import Client
from zeep.wsse.username import UsernameToken

from mitek_mobile_verify.models.requests import PhotoVerifyAdvancedRequest

__author__ = 'lundberg'


class MitekMobileVerifyService(object):

    def __init__(self, wsdl, username, password, transport=None, service_name=None, port_name=None, plugins=None):
        self.authentication = UsernameToken(username, password, use_digest=False)  # XXX digest true or false?
        self.client = Client(wsdl=wsdl, wsse=self.authentication, transport=transport, service_name=service_name,
                             port_name=port_name, plugins=plugins)

    def _prepare_request(self, request):
        """
        :param request: Request object
        :type request: mitek_mobile_verify.models.requests.PhotoVerifyBaseRequest
        :return: Schema object
        :rtype: zeep.objects.PhotoVerifyAdvancedRequest
        """
        if isinstance(request, PhotoVerifyAdvancedRequest):
            req = self.client.get_type('ns2:PhotoVerifyAdvancedRequest')
            return req(**request.to_dict())

        raise NotImplementedError('Request of type {} not implemented'.format(type(request)))

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
        prepered_request = self._prepare_request(request)
        self.client.service.Verify(prepered_request, _soapheaders=headers)

