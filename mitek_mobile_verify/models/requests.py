# -*- coding: utf-8 -*-

from mitek_mobile_verify.models import base
from mitek_mobile_verify.models import validators

__author__ = 'lundberg'


class PhotoVerifyBaseRequest(object):

    def __init__(self):
        self.data = {}

    @staticmethod
    def create_name(first_name=None, last_name=None, middle_name=None, suffix=None):
        """
        :param first_name: First name
        :type first_name: str
        :param last_name: Last name
        :type last_name: str
        :param middle_name: Middle name
        :type middle_name: str
        :param suffix: Suffix
        :type suffix: str
        :return: Name object
        :rtype: mitek_mobile_verify.base.Name
        """
        return base.Name(first_name=first_name, last_name=last_name, middle_name=middle_name, suffix=suffix)

    @staticmethod
    def create_image(image_data, hints=None):
        """
        :param image_data: Image as base64 encoded string
        :type image_data: str
        :param hints: Image hints
        :type hints: list
        :return: Image object
        :rtype: mitek_mobile_verify.base.Image
        """
        return base.Image(image_data=image_data, hints=hints)

    def to_dict(self):
        d = {}
        for key, value in self.data.items():
            if isinstance(value, base.BasicModel):
                value = value.to_dict()
            d[key] = value
        return d


class PhotoVerifyRequest(PhotoVerifyBaseRequest):

    def load(self, response_image_types, back_image, expected_name, front_image, issue_date, state_abbr):
        """
        :param response_image_types: Image types
        :type response_image_types: list
        :param back_image: Back image
        :type back_image: mitek_mobile_verify.base.Image
        :param expected_name: Expected name
        :type expected_name: mitek_mobile_verify.base.Name
        :param front_image: Front image
        :type front_image: mitek_mobile_verify.base.Image
        :param issue_date: Issue date
        :type issue_date: datetime.Datetime
        :param state_abbr: State abbreviation
        :type state_abbr: str
        """
        self.response_image_types = response_image_types
        self.back_image = back_image
        self.expected_name = expected_name
        self.front_image = front_image
        self.issue_date = issue_date
        self.state_abbr = state_abbr

    @property
    def response_image_types(self):
        return self.data.get('ResponseImageTypes')

    @response_image_types.setter
    def response_image_types(self, l):
        """
        :param l: List of strings
        :type l: list
        """
        if l is None:
            self.data['ResponseImageTypes'] = None
            return

        if not validators.is_string_value_list(l):
            raise TypeError('All list items needs to be of type str')

        d = {
            'string': []
        }
        for item in l:
            d['string'].append(item)
        self.data['ResponseImageTypes'] = d

    @property
    def back_image(self):
        return self.data.get('BackImage')

    @back_image.setter
    def back_image(self, image):
        """
        :param image: Image object
        :type image: mitek_mobile_verify.base.Image
        """
        if not isinstance(image, base.Image):
            raise ValueError('Value needs to by of type mitek_mobile_verify.base.Image')
        self.data['BackImage'] = image

    @property
    def expected_name(self):
        return self.data.get('ExpectedName')

    @expected_name.setter
    def expected_name(self, name):
        """
        :param name: Name object
        :type name: mitek_mobile_verify.base.Name
        """
        if not isinstance(name, base.Name):
            raise ValueError('Value needs to by of type mitek_mobile_verify.base.Name')
        self.data['ExpectedName'] = name

    @property
    def front_image(self):
        return self.data.get('FrontImage')

    @front_image.setter
    def front_image(self, image):
        """
        :param image: Image object
        :type image: mitek_mobile_verify.base.Image
        """
        if not isinstance(image, base.Image):
            raise ValueError('Value needs to by of type mitek_mobile_verify.base.Image')
        self.data['FrontImage'] = image

    @property
    def issue_date(self):
        return self.data.get('IssueDate')

    @issue_date.setter
    def issue_date(self, dt):
        """
        :param dt: Issue date
        :type dt: datetime.datetime
        """
        if not validators.is_datetime(dt):
            raise ValueError('Value needs to be of type datetime.datetime')
        self.data['IssueDate'] = dt

    @property
    def state_abbr(self):
        return self.data.get('StateAbbr')

    @state_abbr.setter
    def state_abbr(self, s):
        """
        :param s: State abbreviation
        :type s: str
        """
        if not validators.is_string(s):
            raise ValueError('Value needs to be of type str')
        self.data['StateAbbr'] = s


class PhotoVerifyAdvancedRequest(PhotoVerifyRequest):

    def load(self, response_image_types, back_image, expected_name, front_image, issue_date, state_abbr, esf_detection):
        """
        :param response_image_types: Image types
        :type response_image_types: list
        :param back_image: Back image
        :type back_image: mitek_mobile_verify.base.Image
        :param expected_name: Expected name
        :type expected_name: mitek_mobile_verify.base.Name
        :param front_image: Front image
        :type front_image: mitek_mobile_verify.base.Image
        :param issue_date: Issue date
        :type issue_date: datetime.Datetime
        :param state_abbr: State abbreviation
        :type state_abbr: str
        :param esf_detection: ESF data
        :type esf_detection: mitek_mobile_verify.base.ESFDetection
        """
        super(PhotoVerifyAdvancedRequest, self).load(response_image_types, back_image, expected_name, front_image,
                                                     issue_date, state_abbr)
        self.esf_detection = esf_detection

    @property
    def esf_detection(self):
        return self.data.get('EsfDetection')

    @esf_detection.setter
    def esf_detection(self, esf_detection):
        """
        :param esf_detection: ESFDetection object
        :type esf_detection: mitek_mobile_verify.base.ESFDetection
        """
        if not isinstance(esf_detection, base.ESFDetection):
            raise ValueError('Value needs to by of type mitek_mobile_verify.base.ESFDetection')
        self.data['EsfDetection'] = esf_detection

    @staticmethod
    def create_esf_detection(extracted_data=None, performed_evaluation=False):
        """
        :param extracted_data: Extracted data
        :type extracted_data: list
        :param performed_evaluation: Performed evaluation
        :type performed_evaluation: bool
        :return: ESFDetection object
        :rtype: mitek_mobile_verify.base.ESFDetection
        """
        return base.ESFDetection(extracted_data=extracted_data, performed_evaluation=performed_evaluation)
