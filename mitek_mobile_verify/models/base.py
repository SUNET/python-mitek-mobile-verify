# -*- coding: utf-8 -*-

from mitek_mobile_verify.models import validators

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
        d = {
            'KeyValueOfstringstring': []
        }
        for item in l:
            for key, value in item.items():
                d['KeyValueOfstringstring'].append({'Key': key, 'Value': value})
        self.data['Hints'] = d

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
            raise TypeError('All dict value needs to be of type str')
        d = {
            'KeyValueOfstringstring': []
        }
        for item in l:
            for key, value in item.items():
                d['KeyValueOfstringstring'].append({'Key': key, 'Value': value})
        self.data['ExtractedData'] = d

    @property
    def performed_evaluation(self):
        return self.data.get('PerformedEvaluation')

    @performed_evaluation.setter
    def performed_evaluation(self, b):
        if not validators.is_bool(b):
            raise TypeError('Value needs to be of type bool')
        self.data['PerformedEvaluation'] = b
