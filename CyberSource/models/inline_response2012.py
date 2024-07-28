# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class InlineResponse2012(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'submit_time_utc': 'date',
        'status': 'str',
        'registration_information': 'InlineResponse2012RegistrationInformation',
        'integration_information': 'InlineResponse2012IntegrationInformation',
        'organization_information': 'InlineResponse2012OrganizationInformation',
        'product_information_setups': 'list[InlineResponse2012ProductInformationSetups]',
        'message': 'str',
        'details': 'dict(str, list[object])'
    }

    attribute_map = {
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'registration_information': 'registrationInformation',
        'integration_information': 'integrationInformation',
        'organization_information': 'organizationInformation',
        'product_information_setups': 'productInformationSetups',
        'message': 'message',
        'details': 'details'
    }

    def __init__(self, id=None, submit_time_utc=None, status=None, registration_information=None, integration_information=None, organization_information=None, product_information_setups=None, message=None, details=None):
        """
        InlineResponse2012 - a model defined in Swagger
        """

        self._id = None
        self._submit_time_utc = None
        self._status = None
        self._registration_information = None
        self._integration_information = None
        self._organization_information = None
        self._product_information_setups = None
        self._message = None
        self._details = None

        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if registration_information is not None:
          self.registration_information = registration_information
        if integration_information is not None:
          self.integration_information = integration_information
        if organization_information is not None:
          self.organization_information = organization_information
        if product_information_setups is not None:
          self.product_information_setups = product_information_setups
        if message is not None:
          self.message = message
        if details is not None:
          self.details = details

    @property
    def id(self):
        """
        Gets the id of this InlineResponse2012.

        :return: The id of this InlineResponse2012.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse2012.

        :param id: The id of this InlineResponse2012.
        :type: str
        """

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this InlineResponse2012.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :return: The submit_time_utc of this InlineResponse2012.
        :rtype: date
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this InlineResponse2012.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this InlineResponse2012.
        :type: date
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2012.
        The status of Registration request Possible Values:   - 'INITIALIZED'   - 'RECEIVED'   - 'PROCESSING'   - 'SUCCESS'   - 'FAILURE'   - 'PARTIAL' 

        :return: The status of this InlineResponse2012.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2012.
        The status of Registration request Possible Values:   - 'INITIALIZED'   - 'RECEIVED'   - 'PROCESSING'   - 'SUCCESS'   - 'FAILURE'   - 'PARTIAL' 

        :param status: The status of this InlineResponse2012.
        :type: str
        """
        allowed_values = ["INITIALIZED", "RECEIVED", "PROCESSING", "SUCCESS", "FAILURE", "PARTIAL"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def registration_information(self):
        """
        Gets the registration_information of this InlineResponse2012.

        :return: The registration_information of this InlineResponse2012.
        :rtype: InlineResponse2012RegistrationInformation
        """
        return self._registration_information

    @registration_information.setter
    def registration_information(self, registration_information):
        """
        Sets the registration_information of this InlineResponse2012.

        :param registration_information: The registration_information of this InlineResponse2012.
        :type: InlineResponse2012RegistrationInformation
        """

        self._registration_information = registration_information

    @property
    def integration_information(self):
        """
        Gets the integration_information of this InlineResponse2012.

        :return: The integration_information of this InlineResponse2012.
        :rtype: InlineResponse2012IntegrationInformation
        """
        return self._integration_information

    @integration_information.setter
    def integration_information(self, integration_information):
        """
        Sets the integration_information of this InlineResponse2012.

        :param integration_information: The integration_information of this InlineResponse2012.
        :type: InlineResponse2012IntegrationInformation
        """

        self._integration_information = integration_information

    @property
    def organization_information(self):
        """
        Gets the organization_information of this InlineResponse2012.

        :return: The organization_information of this InlineResponse2012.
        :rtype: InlineResponse2012OrganizationInformation
        """
        return self._organization_information

    @organization_information.setter
    def organization_information(self, organization_information):
        """
        Sets the organization_information of this InlineResponse2012.

        :param organization_information: The organization_information of this InlineResponse2012.
        :type: InlineResponse2012OrganizationInformation
        """

        self._organization_information = organization_information

    @property
    def product_information_setups(self):
        """
        Gets the product_information_setups of this InlineResponse2012.

        :return: The product_information_setups of this InlineResponse2012.
        :rtype: list[InlineResponse2012ProductInformationSetups]
        """
        return self._product_information_setups

    @product_information_setups.setter
    def product_information_setups(self, product_information_setups):
        """
        Sets the product_information_setups of this InlineResponse2012.

        :param product_information_setups: The product_information_setups of this InlineResponse2012.
        :type: list[InlineResponse2012ProductInformationSetups]
        """

        self._product_information_setups = product_information_setups

    @property
    def message(self):
        """
        Gets the message of this InlineResponse2012.

        :return: The message of this InlineResponse2012.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineResponse2012.

        :param message: The message of this InlineResponse2012.
        :type: str
        """

        self._message = message

    @property
    def details(self):
        """
        Gets the details of this InlineResponse2012.

        :return: The details of this InlineResponse2012.
        :rtype: dict(str, list[object])
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this InlineResponse2012.

        :param details: The details of this InlineResponse2012.
        :type: dict(str, list[object])
        """

        self._details = details

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse2012):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
