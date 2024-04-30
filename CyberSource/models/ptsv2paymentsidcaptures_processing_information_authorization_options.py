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


class Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions(object):
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
        'auth_type': 'str',
        'verbal_auth_code': 'str',
        'verbal_auth_transaction_id': 'str'
    }

    attribute_map = {
        'auth_type': 'authType',
        'verbal_auth_code': 'verbalAuthCode',
        'verbal_auth_transaction_id': 'verbalAuthTransactionId'
    }

    def __init__(self, auth_type=None, verbal_auth_code=None, verbal_auth_transaction_id=None):
        """
        Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions - a model defined in Swagger
        """

        self._auth_type = None
        self._verbal_auth_code = None
        self._verbal_auth_transaction_id = None

        if auth_type is not None:
          self.auth_type = auth_type
        if verbal_auth_code is not None:
          self.verbal_auth_code = verbal_auth_code
        if verbal_auth_transaction_id is not None:
          self.verbal_auth_transaction_id = verbal_auth_transaction_id

    @property
    def auth_type(self):
        """
        Gets the auth_type of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Authorization type. Possible values:   - `AUTOCAPTURE`: automatic capture.  - `STANDARDCAPTURE`: standard capture.  - `VERBAL`: forced capture. Include it in the payment request for a forced capture. Include it in the capture request for a verbal payment.  #### Asia, Middle East, and Africa Gateway; Cielo; Comercio Latino; and CyberSource Latin American Processing Set this field to `AUTOCAPTURE` and include it in a bundled request to indicate that you are requesting an automatic capture. If your account is configured to enable automatic captures, set this field to `STANDARDCAPTURE` and include it in a standard authorization or bundled request to indicate that you are overriding an automatic capture. For more information, see the `auth_type` field description in [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Forced Capture Set this field to `VERBAL` and include it in the authorization request to indicate that you are performing a forced capture; therefore, you receive the authorization code outside the CyberSource system.  #### Verbal Authorization Set this field to `VERBAL` and include it in the capture request to indicate that the request is for a verbal authorization. For more information, see \"Verbal Authorizations\" in [Credit Card Services Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html). 

        :return: The auth_type of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """
        Sets the auth_type of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Authorization type. Possible values:   - `AUTOCAPTURE`: automatic capture.  - `STANDARDCAPTURE`: standard capture.  - `VERBAL`: forced capture. Include it in the payment request for a forced capture. Include it in the capture request for a verbal payment.  #### Asia, Middle East, and Africa Gateway; Cielo; Comercio Latino; and CyberSource Latin American Processing Set this field to `AUTOCAPTURE` and include it in a bundled request to indicate that you are requesting an automatic capture. If your account is configured to enable automatic captures, set this field to `STANDARDCAPTURE` and include it in a standard authorization or bundled request to indicate that you are overriding an automatic capture. For more information, see the `auth_type` field description in [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Forced Capture Set this field to `VERBAL` and include it in the authorization request to indicate that you are performing a forced capture; therefore, you receive the authorization code outside the CyberSource system.  #### Verbal Authorization Set this field to `VERBAL` and include it in the capture request to indicate that the request is for a verbal authorization. For more information, see \"Verbal Authorizations\" in [Credit Card Services Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html). 

        :param auth_type: The auth_type of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :type: str
        """

        self._auth_type = auth_type

    @property
    def verbal_auth_code(self):
        """
        Gets the verbal_auth_code of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Authorization code.  #### Forced Capture Use this field to send the authorization code you received from a payment that you authorized outside the CyberSource system.  #### PIN debit Authorization code that is returned by the processor.  Returned by PIN debit purchase.  #### Verbal Authorization Use this field in CAPTURE API to send the verbally received authorization code.  For processor-specific information, see the `auth_code` field description in [Credit Card Services Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html). 

        :return: The verbal_auth_code of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :rtype: str
        """
        return self._verbal_auth_code

    @verbal_auth_code.setter
    def verbal_auth_code(self, verbal_auth_code):
        """
        Sets the verbal_auth_code of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Authorization code.  #### Forced Capture Use this field to send the authorization code you received from a payment that you authorized outside the CyberSource system.  #### PIN debit Authorization code that is returned by the processor.  Returned by PIN debit purchase.  #### Verbal Authorization Use this field in CAPTURE API to send the verbally received authorization code.  For processor-specific information, see the `auth_code` field description in [Credit Card Services Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html). 

        :param verbal_auth_code: The verbal_auth_code of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :type: str
        """

        self._verbal_auth_code = verbal_auth_code

    @property
    def verbal_auth_transaction_id(self):
        """
        Gets the verbal_auth_transaction_id of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Transaction ID (TID).  #### FDMS South This field is required for verbal authorizations and forced captures with the American Express card type to comply with the CAPN requirements: - Forced capture: Obtain the value for this field from the authorization response. - Verbal authorization: You cannot obtain a value for this field so CyberSource uses the default value of `000000000000000` (15 zeros). 

        :return: The verbal_auth_transaction_id of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :rtype: str
        """
        return self._verbal_auth_transaction_id

    @verbal_auth_transaction_id.setter
    def verbal_auth_transaction_id(self, verbal_auth_transaction_id):
        """
        Sets the verbal_auth_transaction_id of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Transaction ID (TID).  #### FDMS South This field is required for verbal authorizations and forced captures with the American Express card type to comply with the CAPN requirements: - Forced capture: Obtain the value for this field from the authorization response. - Verbal authorization: You cannot obtain a value for this field so CyberSource uses the default value of `000000000000000` (15 zeros). 

        :param verbal_auth_transaction_id: The verbal_auth_transaction_id of this Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :type: str
        """

        self._verbal_auth_transaction_id = verbal_auth_transaction_id

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
        if not isinstance(other, Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
