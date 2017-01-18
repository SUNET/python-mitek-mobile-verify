# -*- coding: utf-8 -*-

from zeep import Client
from zeep import xsd
from zeep.wsse.username import UsernameToken

__author__ = 'lundberg'


class MitekMobileVerifyService(object):

    def __init__(self, wsdl, username, password, transport=None, service_name=None, port_name=None, plugins=None):
        self.authentication = UsernameToken(username, password, use_digest=False)  # XXX digest true or false?
        self.client = Client(wsdl=wsdl, wsse=self.authentication, transport=transport, service_name=service_name,
                             port_name=port_name, plugins=plugins)


    def create_advanced_request(self):
        # ResponseImageTypes: ArrayOfstring, BackImage: Image, ExpectedName: Name, FrontImage: Image, IssueDate: xsd:dateTime, StateAbbr: xsd:string, EsfDetection: ESFDetection
        request = {
            'ResponseImageTypes': None,
            'BackImage': None,
            'ExpectedName': None,
            'FrontImage': None,
            'IssueDate': None,
            'StateAbbr': None,
            'EsfDetection': None
        }

        pass

    def verify(self, request):
        # Verify(DocumentRequest: DocumentRequest, _soapheaders={DeviceMetaData: DeviceMetaData(), Metadata: Metadata(), MibiDataHeader: MibiDataHeader()})
        pass


