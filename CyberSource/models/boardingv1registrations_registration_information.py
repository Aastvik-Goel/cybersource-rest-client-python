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


class Boardingv1registrationsRegistrationInformation(object):
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
        'boarding_registration_id': 'str',
        'submit_time_utc': 'date',
        'status': 'str',
        'boarding_package_id': 'str',
        'boarding_flow': 'str',
        'mode': 'str',
        'sales_rep_id': 'str'
    }

    attribute_map = {
        'boarding_registration_id': 'boardingRegistrationId',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'boarding_package_id': 'boardingPackageId',
        'boarding_flow': 'boardingFlow',
        'mode': 'mode',
        'sales_rep_id': 'salesRepId'
    }

    def __init__(self, boarding_registration_id=None, submit_time_utc=None, status=None, boarding_package_id=None, boarding_flow=None, mode=None, sales_rep_id=None):
        """
        Boardingv1registrationsRegistrationInformation - a model defined in Swagger
        """

        self._boarding_registration_id = None
        self._submit_time_utc = None
        self._status = None
        self._boarding_package_id = None
        self._boarding_flow = None
        self._mode = None
        self._sales_rep_id = None

        if boarding_registration_id is not None:
          self.boarding_registration_id = boarding_registration_id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if boarding_package_id is not None:
          self.boarding_package_id = boarding_package_id
        if boarding_flow is not None:
          self.boarding_flow = boarding_flow
        if mode is not None:
          self.mode = mode
        if sales_rep_id is not None:
          self.sales_rep_id = sales_rep_id

    @property
    def boarding_registration_id(self):
        """
        Gets the boarding_registration_id of this Boardingv1registrationsRegistrationInformation.

        :return: The boarding_registration_id of this Boardingv1registrationsRegistrationInformation.
        :rtype: str
        """
        return self._boarding_registration_id

    @boarding_registration_id.setter
    def boarding_registration_id(self, boarding_registration_id):
        """
        Sets the boarding_registration_id of this Boardingv1registrationsRegistrationInformation.

        :param boarding_registration_id: The boarding_registration_id of this Boardingv1registrationsRegistrationInformation.
        :type: str
        """

        self._boarding_registration_id = boarding_registration_id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this Boardingv1registrationsRegistrationInformation.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :return: The submit_time_utc of this Boardingv1registrationsRegistrationInformation.
        :rtype: date
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this Boardingv1registrationsRegistrationInformation.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this Boardingv1registrationsRegistrationInformation.
        :type: date
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this Boardingv1registrationsRegistrationInformation.
        The status of Registration request Possible Values:   - 'PROCESSING': This status is for Registrations that are still in Progress, you can get the latest status by calling the GET endpoint using the Registration Id   - 'SUCCESS': This status is for Registrations that were successfull on every step of the on boarding process.   - 'FAILURE': This status is for Registrations that fail before the Organization was created; please refer to the details section in the reponse for more information.   - 'PARTIAL': This status is for Registrations that created the Organization successfully but fail in at least on step while configuring it; please refer to the details section in the response for more information. 

        :return: The status of this Boardingv1registrationsRegistrationInformation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Boardingv1registrationsRegistrationInformation.
        The status of Registration request Possible Values:   - 'PROCESSING': This status is for Registrations that are still in Progress, you can get the latest status by calling the GET endpoint using the Registration Id   - 'SUCCESS': This status is for Registrations that were successfull on every step of the on boarding process.   - 'FAILURE': This status is for Registrations that fail before the Organization was created; please refer to the details section in the reponse for more information.   - 'PARTIAL': This status is for Registrations that created the Organization successfully but fail in at least on step while configuring it; please refer to the details section in the response for more information. 

        :param status: The status of this Boardingv1registrationsRegistrationInformation.
        :type: str
        """
        allowed_values = ["PROCESSING", "SUCCESS", "FAILURE", "PARTIAL"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def boarding_package_id(self):
        """
        Gets the boarding_package_id of this Boardingv1registrationsRegistrationInformation.

        :return: The boarding_package_id of this Boardingv1registrationsRegistrationInformation.
        :rtype: str
        """
        return self._boarding_package_id

    @boarding_package_id.setter
    def boarding_package_id(self, boarding_package_id):
        """
        Sets the boarding_package_id of this Boardingv1registrationsRegistrationInformation.

        :param boarding_package_id: The boarding_package_id of this Boardingv1registrationsRegistrationInformation.
        :type: str
        """

        self._boarding_package_id = boarding_package_id

    @property
    def boarding_flow(self):
        """
        Gets the boarding_flow of this Boardingv1registrationsRegistrationInformation.
        Determines the boarding flow for this registration. Possible Values:   - 'ENTERPRISE'   - 'SMB'   - 'ADDPRODUCT' 

        :return: The boarding_flow of this Boardingv1registrationsRegistrationInformation.
        :rtype: str
        """
        return self._boarding_flow

    @boarding_flow.setter
    def boarding_flow(self, boarding_flow):
        """
        Sets the boarding_flow of this Boardingv1registrationsRegistrationInformation.
        Determines the boarding flow for this registration. Possible Values:   - 'ENTERPRISE'   - 'SMB'   - 'ADDPRODUCT' 

        :param boarding_flow: The boarding_flow of this Boardingv1registrationsRegistrationInformation.
        :type: str
        """
        allowed_values = ["ENTERPRISE", "SMB", "ADDPRODUCT"]
        if boarding_flow not in allowed_values:
            raise ValueError(
                "Invalid value for `boarding_flow` ({0}), must be one of {1}"
                .format(boarding_flow, allowed_values)
            )

        self._boarding_flow = boarding_flow

    @property
    def mode(self):
        """
        Gets the mode of this Boardingv1registrationsRegistrationInformation.
        In case mode is not provided the API will use COMPLETE as default Possible Values:   - 'COMPLETE'   - 'PARTIAL' 

        :return: The mode of this Boardingv1registrationsRegistrationInformation.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this Boardingv1registrationsRegistrationInformation.
        In case mode is not provided the API will use COMPLETE as default Possible Values:   - 'COMPLETE'   - 'PARTIAL' 

        :param mode: The mode of this Boardingv1registrationsRegistrationInformation.
        :type: str
        """
        allowed_values = ["COMPLETE", "PARTIAL"]
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def sales_rep_id(self):
        """
        Gets the sales_rep_id of this Boardingv1registrationsRegistrationInformation.

        :return: The sales_rep_id of this Boardingv1registrationsRegistrationInformation.
        :rtype: str
        """
        return self._sales_rep_id

    @sales_rep_id.setter
    def sales_rep_id(self, sales_rep_id):
        """
        Sets the sales_rep_id of this Boardingv1registrationsRegistrationInformation.

        :param sales_rep_id: The sales_rep_id of this Boardingv1registrationsRegistrationInformation.
        :type: str
        """

        self._sales_rep_id = sales_rep_id

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
        if not isinstance(other, Boardingv1registrationsRegistrationInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
