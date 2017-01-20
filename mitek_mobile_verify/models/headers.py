# -*- coding: utf-8 -*-

from mitek_mobile_verify.models.base import BasicModel
from mitek_mobile_verify.models import validators

__author__ = 'lundberg'


class DeviceMetaData(BasicModel):
    def __init__(self, browser, device, operating_system, raw_data):
        """
        :param browser: Browser
        :type browser: str
        :param device: Device
        :type device: str
        :param operating_system: Operating system
        :type operating_system: str
        :param raw_data: Raw data
        :type raw_data: str
        """

        self.data = {}
        self.browser = browser
        self.device = device
        self.operating_system = operating_system
        self.raw_data = raw_data

    @property
    def browser(self):
        return self.data.get('Browser')

    @browser.setter
    def browser(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['Browser'] = s

    @property
    def device(self):
        return self.data.get('Device')

    @device.setter
    def device(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['Device'] = s

    @property
    def operating_system(self):
        return self.data.get('OperatingSystem')

    @operating_system.setter
    def operating_system(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['OperatingSystem'] = s

    @property
    def raw_data(self):
        return self.data.get('RawData')

    @raw_data.setter
    def raw_data(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['RawData'] = s


class AgentMetaData(DeviceMetaData):
    # Identical to DeviceMetaData
    pass


class MibiDataHeader(BasicModel):

    def __init__(self, mibi_data):
        self.data = {}
        self.mibi_data = mibi_data

    @property
    def mibi_data(self):
        return self.data.get('MibiData')

    @mibi_data.setter
    def mibi_data(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['MibiData'] = s


class WebRequestMetadataHeader(BasicModel):

    def __init__(self, application_token, session_reference_id, tenant_reference, version):
        """
        :param application_token: Application token
        :type application_token: str
        :param session_reference_id: Session reference ID
        :type session_reference_id: str
        :param tenant_reference: Tenant Reference
        :type tenant_reference: str
        :param version: Version
        :type version: str
        """
        self.data = {}
        self.application_token = application_token
        self.session_reference_id = session_reference_id
        self.tenant_reference = tenant_reference
        self.version = version

    @property
    def application_token(self):
        return self.data.get('ApplicationToken')

    @application_token.setter
    def application_token(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['ApplicationToken'] = s

    @property
    def session_reference_id(self):
        return self.data.get('SessionReferenceId')

    @session_reference_id.setter
    def session_reference_id(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['SessionReferenceId'] = s

    @property
    def tenant_reference(self):
        return self.data.get('TenantReference')

    @tenant_reference.setter
    def tenant_reference(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['TenantReference'] = s

    @property
    def version(self):
        return self.data.get('Version')

    @version.setter
    def version(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['Version'] = s
