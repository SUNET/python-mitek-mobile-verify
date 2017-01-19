# -*- coding: utf-8 -*-

from mitek_mobile_verify import validators

__author__ = 'lundberg'


class BasicModel(object):

    data = None

    def to_dict(self):
        return self.data


class Image(BasicModel):

    def __init__(self, hints, image_data):
        """
        :param hints: Hints
        :type hints: list
        :param image_data: Image as base64 encoded string
        :type image_data: str
        """
        self.data = {}
        self.hints = hints
        self.image_data = image_data

    @property
    def hints(self):
        return self.data.get('Hints')

    @hints.setter
    def hints(self, l):
        if not all([validators.is_string_value_dict(item) for item in l]):
            raise TypeError('All dict value needs to be of type str')
        self.data['Hints'] = l

    @property
    def image_data(self):
        return self.data.get('ImageData')

    @image_data.setter
    def image_data(self, s):
        # Do our best to check if s is a base64 encoded string
        if not validators.is_base64(s):
            raise TypeError('Value needs to be a base64 encoded string')
        self.data['ImageData'] = s


class Name(BasicModel):

    def __init__(self, first_name, last_name, middle_name='', suffix=''):
        """
        :param first_name: First name
        :type first_name: str
        :param last_name: Last name
        :type last_name: str
        :param middle_name: Middle name
        :type middle_name: str
        :param suffix: Suffix
        :type suffix: str
        """

        self.data = {}
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.suffix = suffix

    @property
    def first_name(self):
        return self.data.get('FirstName')

    @first_name.setter
    def first_name(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['FirstName'] = s

    @property
    def last_name(self):
        return self.data.get('LastName')

    @last_name.setter
    def last_name(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['LastName'] = s

    @property
    def middle_name(self):
        return self.data.get('MiddleName')

    @middle_name.setter
    def middle_name(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['MiddleName'] = s

    @property
    def suffix(self):
        return self.data.get('Suffix')

    @suffix.setter
    def suffix(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['Suffix'] = s


class ESFDetection(BasicModel):

    def __init__(self, extracted_data, performed_evaluation):
        """
        :param extracted_data: Extracted data
        :type extracted_data: list
        :param performed_evaluation: Performed evaluation
        :type performed_evaluation: bool
        """

        self.data = {}
        self.extracted_data = extracted_data
        self.performed_evaluation = performed_evaluation

    @property
    def extracted_data(self):
        return self.data.get('ExtractedData')

    @extracted_data.setter
    def extracted_data(self, l):
        if not all([validators.is_string_value_dict(item) for item in l]):
            raise TypeError('All dict values needs to be of type str')
        self.data['ExtractedData'] = l

    @property
    def performed_evaluation(self):
        return self.data.get('PerformedEvaluation')

    @performed_evaluation.setter
    def performed_evaluation(self, b):
        if not validators.is_bool(b):
            raise TypeError('Value needs to be of type bool')
        self.data['PerformedEvaluation'] = b


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
