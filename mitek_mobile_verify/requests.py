# -*- coding: utf-8 -*-

from mitek_mobile_verify import models, validators

__author__ = 'lundberg'


class PhotoVerifyBaseRequest(object):

    def __init__(self):
        self.data = {}

    def to_dict(self):
        raise NotImplemented()

    def create_request_dict(self):
        return {'PhotoVerifyBaseRequest': self.to_dict()}

    @staticmethod
    def create_name(first_name, last_name, middle_name, suffix):
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
        :rtype: mitek_mobile_verify.models.Name
        """
        return models.Name(first_name=first_name, last_name=last_name, middle_name=middle_name, suffix=suffix)

    @staticmethod
    def create_image(hints, image_data):
        """
        :param hints: Image hints
        :type hints: list
        :param image_data: Image as base64 encoded string
        :type image_data: str
        :return: Image object
        :rtype: mitek_mobile_verify.models.Image
        """
        return models.Image(hints=hints, image_data=image_data)


class PhotoVerifyAdvancedRequest(PhotoVerifyBaseRequest):

    def load(self, response_image_types, back_image, expected_name, front_image, issue_date, state_abbr,
             esf_detection):
        """
        :param response_image_types: Image types
        :type response_image_types: list
        :param back_image: Back image
        :type back_image: mitek_mobile_verify.models.Image
        :param expected_name: Expected name
        :type expected_name: mitek_mobile_verify.models.Name
        :param front_image: Front image
        :type front_image: mitek_mobile_verify.models.Image
        :param issue_date: Issue date
        :type issue_date: datetime.Datetime
        :param state_abbr: State abbreviation
        :type state_abbr: str
        :param esf_detection: ESF data
        :type esf_detection: mitek_mobile_verify.models.ESFDetection
        """
        self.response_image_types = response_image_types
        self.back_image = back_image
        self.expected_name = expected_name
        self.front_image = front_image
        self.issue_date = issue_date
        self.state_abbr = state_abbr
        self.esf_detection = esf_detection

    @property
    def response_image_types(self):
        return self.data.get('ResponseImageTypes')

    @response_image_types.setter
    def response_image_types(self, l):
        """
        :param l: List of strings
        :type l: list
        """
        if not validators.is_string_value_list(l):
            raise TypeError('All list items needs to be of type str')
        self.data['ResponseImageTypes'] = l

    @property
    def back_image(self):
        return self.data.get('BackImage')

    @back_image.setter
    def back_image(self, image):
        """
        :param image: Image object
        :type image: mitek_mobile_verify.models.Image
        """
        if not isinstance(image, models.Image):
            raise ValueError('Value needs to by of type mitek_mobile_verify.models.Image')
        self.data['BackImage'] = image

    @property
    def expected_name(self):
        return self.data.get('ExpectedName')

    @expected_name.setter
    def expected_name(self, name):
        """
        :param name: Name object
        :type name: mitek_mobile_verify.models.Name
        """
        if not isinstance(name, models.Name):
            raise ValueError('Value needs to by of type mitek_mobile_verify.models.Name')
        self.data['ExpectedName'] = name

    @property
    def front_image(self):
        return self.data.get('FrontImage')

    @front_image.setter
    def front_image(self, image):
        """
        :param image: Image object
        :type image: mitek_mobile_verify.models.Image
        """
        if not isinstance(image, models.Image):
            raise ValueError('Value needs to by of type mitek_mobile_verify.models.Image')
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

    @property
    def esf_detection(self):
        return self.data.get('ESFDetection')

    @esf_detection.setter
    def esf_detection(self, esf_detection):
        """
        :param esf_detection: ESFDetection object
        :type esf_detection: mitek_mobile_verify.models.ESFDetection
        """
        if not isinstance(esf_detection, models.ESFDetection):
            raise ValueError('Value needs to by of type mitek_mobile_verify.models.ESFDetection')
        self.data['ESFDetection'] = esf_detection

    @staticmethod
    def create_esf_detection(extracted_data, performed_evaluation):
        """
        :param extracted_data: Extracted data
        :type extracted_data: list
        :param performed_evaluation: Performed evaluation
        :type performed_evaluation: bool
        :return: ESFDetection object
        :rtype: mitek_mobile_verify.models.ESFDetection
        """
        return models.ESFDetection(extracted_data=extracted_data, performed_evaluation=performed_evaluation)

    def to_dict(self):
        d = {
            'DocumentRequest': {
                'type': 'PhotoVerifyAdvancedRequest'
            }
        }

        for key, value in self.data.items():
            if isinstance(value, models.BasicModel):
                value = value.to_dict()
            d['DocumentRequest'][key] = value
        return d
