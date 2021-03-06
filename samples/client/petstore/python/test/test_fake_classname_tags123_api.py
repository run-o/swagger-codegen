# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import petstore_api
from petstore_api.rest import ApiException
from petstore_api.apis.fake_classname_tags123_api import FakeClassnameTags123Api


class TestFakeClassnameTags123Api(unittest.TestCase):
    """ FakeClassnameTags123Api unit test stubs """

    def setUp(self):
        self.api = petstore_api.apis.fake_classname_tags123_api.FakeClassnameTags123Api()

    def tearDown(self):
        pass

    def test_test_classname(self):
        """
        Test case for test_classname

        To test class name in snake case
        """
        pass


if __name__ == '__main__':
    unittest.main()
