# -*- coding: utf-8 -*-

from mitek_mobile_verify.models import validators

__author__ = 'lundberg'


class BasicModel(object):

    data = None

    def to_dict(self):
        return self.data


class Image(BasicModel):

    def __init__(self, image_data=None, hints=None):
        """
        :param image_data: Image data as a byte array
        :type image_data: bytes
        :param hints: Hints
        :type hints: list|None
        """
        self.data = {}
        self.image_data = image_data
        self.hints = hints

    @property
    def hints(self):
        return self.data.get('Hints')

    @hints.setter
    def hints(self, l):
        if l is None:
            self.data['Hints'] = None
            return

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
        if s is None:
            self.data['ImageData'] = None
            return
        # Zeep will base64 encode the bytes when creating xml request
        if not validators.is_string(s):
            raise TypeError('Value needs to be a string')
        self.data['ImageData'] = s


class Name(BasicModel):

    def __init__(self, first_name=None, last_name=None, middle_name=None, suffix=None):
        """
        :param first_name: First name
        :type first_name: str|None
        :param last_name: Last name
        :type last_name: str|None
        :param middle_name: Middle name
        :type middle_name: str|None
        :param suffix: Suffix
        :type suffix: str|None
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

    def __init__(self, extracted_data=None, performed_evaluation=False):
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
        if l is None:
            self.data['ExtractedData'] = None
            return
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
