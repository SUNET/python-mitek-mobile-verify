# -*- coding: utf-8 -*-

from mitek_mobile_verify import validators

__author__ = 'lundberg'


class PhotoVerifyAdvancedRequest(object):

    def __init__(self):
        self.data = {}

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
        self.response_image_types = response_image_types  # ArrayOfstring
        self.back_image = back_image  # Image
        self.expected_name = expected_name  # Name
        self.front_image = front_image  # Image
        self.issue_date = issue_date  # DateTime
        self.state_abbr = state_abbr  # String
        self.esf_detection = esf_detection

    @property
    def response_image_types(self):
        return self.data['ResponseImageTypes']

    @response_image_types.setter
    def response_image_types(self, l):
        if not validators.is_string_value_list(l):
            raise TypeError('All list items needs to be of type str')
        self.data['ResponseImageTypes'] = l

    @property
    def back_image(self):
        return self.data['BackImage']

    @back_image.setter
    def back_image(self, image):
        if not isinstance(image, Image):
            raise ValueError('Value needs to by of type mitek_mobile_verify.models.Image')
        self.data['BackImage'] = image

    @back_image.setter
    def back_image(self, hints, image_data):
        self.data['BackImage'] = Image(hints=hints, image_data=image_data)

    @property
    def expected_name(self):
        return self.data['ExpectedName']

    @expected_name.setter
    def expected_name(self, name):
        if not isinstance(name, Name):
            raise ValueError('Value needs to by of type mitek_mobile_verify.models.Name')
        self.data['ExpectedName'] = name

    @expected_name.setter
    def expected_name(self, first_name, last_name, middle_name='', suffix=''):
        self.data['ExpectedName'] = Name(first_name=first_name, last_name=last_name, middle_name=middle_name,
                                         suffix=suffix)

    @property
    def front_image(self):
        return self.data['FrontImage']

    @front_image.setter
    def front_image(self, image):
        if not isinstance(image, Image):
            raise ValueError('Value needs to by of type mitek_mobile_verify.models.Image')
        self.data['FrontImage'] = image

    @front_image.setter
    def front_image(self, hints, image_data):
        self.data['FrontImage'] = Image(hints=hints, image_data=image_data)

    @property
    def issue_date(self):
        return self.data['IssueDate']

    @issue_date.setter
    def issue_date(self, dt):
        if not validators.is_datetime(dt):
            raise ValueError('Value needs to be of type datetime.datetime')
        self.data['IssueDate'] = dt

    @property
    def state_abbr(self):
        return self.data['StateAbbr']

    @state_abbr.setter
    def state_abbr(self, s):
        if not validators.is_string(s):
            raise ValueError('Value needs to be of type str')
        self.data['StateAbbr'] = s

    @property
    def esf_detection(self):
        return self.data['ESFDetection']

    @esf_detection.setter
    def esf_detection(self, esf_detection):
        if not isinstance(esf_detection, ESFDetection):
            raise ValueError('Value needs to by of type mitek_mobile_verify.models.ESFDetection')
        self.data['ESFDetection'] = esf_detection

    @esf_detection.setter
    def esf_detection(self, extracted_data, performed_evaluation):
        self.data['ESFDetection'] = ESFDetection(extracted_data=extracted_data,
                                                 performed_evaluation=performed_evaluation)

    def to_dict(self):
        d = {}
        for key, value in self.data:
            if isinstance(value, PrimitiveModel):
                value = value.to_dict()
            d[key] = value
        return d


class PrimitiveModel(object):

    data = None

    def to_dict(self):
        return self.data


class Image(PrimitiveModel):

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
        return self.data['Hints']

    @hints.setter
    def hints(self, l):
        # ArrayOfKeyValueOfstringstring
        if not all([validators.is_string_value_dict(item) for item in l]):
            raise TypeError('All dict value needs to be of type str')
        self.data['Hints'] = l

    @property
    def image_data(self):
        return self.data['ImageData']

    @image_data.setter
    def image_data(self, s):
        # Do our best to check if s is a base64 encoded string
        if not validators.is_base64(s):
            raise TypeError('Value needs to be a base64 encoded string')
        self.data['ImageData'] = s


class Name(PrimitiveModel):

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
        return self.data['FirstName']

    @first_name.setter
    def first_name(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['FirstName'] = s

    @property
    def last_name(self):
        return self.data['LastName']

    @last_name.setter
    def last_name(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['LastName'] = s

    @property
    def middle_name(self):
        return self.data['MiddleName']

    @middle_name.setter
    def middle_name(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['MiddleName'] = s

    @property
    def suffix(self):
        return self.data['Suffix']

    @suffix.setter
    def suffix(self, s):
        if not validators.is_string(s):
            raise TypeError('Value needs to be of type str')
        self.data['Suffix'] = s


class ESFDetection(PrimitiveModel):

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
        return self.data['ExtractedData']

    @extracted_data.setter
    def extracted_data(self, l):
        # ArrayOfKeyValueOfstringstring
        if not all([validators.is_string_value_dict(item) for item in l]):
            raise TypeError('All dict value needs to be of type str')
        self.data['ExtractedData'] = l

    @property
    def performed_evaluation(self):
        return self.data['PerformedEvaluation']

    @performed_evaluation.setter
    def performed_evaluation(self, b):
        if not validators.is_bool(b):
            raise TypeError('Value needs to be of type bool')
        self.data['PerformedEvaluation'] = b
