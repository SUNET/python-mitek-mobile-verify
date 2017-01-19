# -*- coding: utf-8 -*-

import unittest
import base64
from datetime import datetime
from mitek_mobile_verify import models
from mitek_mobile_verify.requests import PhotoVerifyAdvancedRequest

__author__ = 'lundberg'



class TestPhotoVerifyAdvancedRequest(unittest.TestCase):

    def setUp(self):
        self.request = PhotoVerifyAdvancedRequest()
        self.ref_dict = {
            'PhotoVerifyBaseRequest': {
                'DocumentRequest': {
                    'BackImage': {
                        'Hints': [{'hint1': 'a hint'}],
                        'ImageData': b'YmFzZTY0c3Ry'
                    },
                    'ESFDetection': {
                        'ExtractedData': [{'some': 'data'}],
                        'PerformedEvaluation': True
                    },
                    'ExpectedName': {
                        'FirstName': 'Test',
                        'LastName': 'Testsson',
                        'MiddleName': 'Testaren',
                        'Suffix': 'III'
                    },
                    'FrontImage': {
                        'Hints': [{'hint1': 'a hint'}], 'ImageData': b'YmFzZTY0c3Ry'
                    },
                    'IssueDate': datetime(2017, 1, 19, 16, 41, 47, 188358),
                    'ResponseImageTypes': ['image_type1', 'image_type2'],
                    'StateAbbr': 'AL',
                    'type': 'PhotoVerifyAdvancedRequest'
                },
            }
        }


    def test_response_image_types(self):
        self.request.response_image_types = ['image_type1']
        self.assertEqual(['image_type1'], self.request.response_image_types)

        self.request.response_image_types = ['image_type2']
        self.assertEqual(['image_type2'], self.request.response_image_types)

        self.request.response_image_types = ['image_type1', 'image_type2']
        self.assertEqual(['image_type1', 'image_type2'], self.request.response_image_types)

        self.assertRaises(TypeError, self.request.response_image_types, 'test')
        self.assertRaises(TypeError, self.request.response_image_types, {})
        self.assertRaises(TypeError, self.request.response_image_types, ['test', 123])
        self.assertRaises(TypeError, self.request.response_image_types, True)

    def test_back_image(self):

        image = models.Image(hints=[{'hint1': 'a hint'}], image_data=base64.b64encode(b'base64str'))
        self.request.back_image = image
        self.assertEqual(self.request.back_image, image)

        image = self.request.create_image(hints=[{'hint1': 'a hint'}], image_data=base64.b64encode(b'base64str'))
        self.request.back_image = image
        self.assertEqual(self.request.back_image, image)

        self.assertRaises(TypeError, self.request.back_image, 'test')

    def test_expected_name(self):

        name = models.Name(first_name='Test', last_name='Testsson', middle_name='Testaren', suffix='III')
        self.request.expected_name = name
        self.assertEqual(self.request.expected_name, name)

        name = self.request.create_name(first_name='Test', last_name='Testsson', middle_name='Testaren', suffix='III')
        self.request.expected_name = name
        self.assertEqual(self.request.expected_name, name)

        self.assertRaises(TypeError, self.request.expected_name, 'test')

    def test_front_image(self):
        image = models.Image(hints=[{'hint1': 'a hint'}], image_data=base64.b64encode(b'base64str'))
        self.request.front_image = image
        self.assertEqual(self.request.front_image, image)

        image = self.request.create_image(hints=[{'hint1': 'a hint'}], image_data=base64.b64encode(b'base64str'))
        self.request.front_image = image
        self.assertEqual(self.request.front_image, image)

        self.assertRaises(TypeError, self.request.front_image, 'test')

    def test_issue_date(self):
        dt = datetime.now()
        self.request.issue_date = dt
        self.assertEqual(self.request.issue_date, dt)

        self.assertRaises(TypeError, self.request.issue_date, 'test')

    def test_state_abbr(self):
        state = 'AL'
        self.request.state_abbr = state
        self.assertEqual(self.request.state_abbr, state)

        self.assertRaises(TypeError, self.request.issue_date, 123)

    def test_esf_detection(self):
        esf_detection = models.ESFDetection(extracted_data=[{'some': 'data'}], performed_evaluation=True)
        self.request.esf_detection = esf_detection
        self.assertEqual(self.request.esf_detection, esf_detection)

        esf_detection = self.request.create_esf_detection(extracted_data=[{'some': 'data'}], performed_evaluation=True)
        self.request.esf_detection = esf_detection
        self.assertEqual(self.request.esf_detection, esf_detection)

        self.assertRaises(TypeError, self.request.esf_detection, 'test')
        self.assertRaises(TypeError, self.request.create_esf_detection, extracted_data=[{'expect_error': True}],
                          performed_evaluation=True)

    def test_load(self):
        response_image_types = ['image_type1', 'image_type2']
        back_image = self.request.create_image(hints=[{'hint1': 'a hint'}], image_data=base64.b64encode(b'base64str'))
        expected_name = self.request.create_name(first_name='Test', last_name='Testsson', middle_name='Testaren',
                                                 suffix='III')
        front_image = self.request.create_image(hints=[{'hint1': 'a hint'}], image_data=base64.b64encode(b'base64str'))
        issue_date = datetime.now()
        state_abbr = 'AL'
        esf_detection = self.request.create_esf_detection(extracted_data=[{'some': 'data'}], performed_evaluation=True)

        self.request.load(response_image_types, back_image, expected_name, front_image, issue_date, state_abbr,
                          esf_detection)

        self.assertEqual(self.request.response_image_types, response_image_types)
        self.assertEqual(self.request.back_image, back_image)
        self.assertEqual(self.request.expected_name, expected_name)
        self.assertEqual(self.request.front_image, front_image)
        self.assertEqual(self.request.issue_date, issue_date)
        self.assertEqual(self.request.state_abbr, state_abbr)
        self.assertEqual(self.request.esf_detection, esf_detection)

    def test_to_dict(self):
        response_image_types = ['image_type1', 'image_type2']
        back_image = self.request.create_image(hints=[{'hint1': 'a hint'}], image_data=base64.b64encode(b'base64str'))
        expected_name = self.request.create_name(first_name='Test', last_name='Testsson', middle_name='Testaren',
                                                 suffix='III')
        front_image = self.request.create_image(hints=[{'hint1': 'a hint'}], image_data=base64.b64encode(b'base64str'))
        issue_date = datetime(2017, 1, 19, 16, 41, 47, 188358)
        state_abbr = 'AL'
        esf_detection = self.request.create_esf_detection(extracted_data=[{'some': 'data'}], performed_evaluation=True)

        self.request.load(response_image_types, back_image, expected_name, front_image, issue_date, state_abbr,
                          esf_detection)

        self.assertEqual(self.request.create_request_dict(), self.ref_dict)


