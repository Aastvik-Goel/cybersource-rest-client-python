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


class Riskv1authenticationresultsConsumerAuthenticationInformation(object):
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
        'authentication_transaction_id': 'str',
        'authentication_transaction_context': 'str',
        'otp_token': 'str',
        'authentication_type': 'str',
        'effective_authentication_type': 'str',
        'response_access_token': 'str',
        'signed_pares_status_reason': 'str',
        'signed_pares': 'str',
        'white_list_status': 'str',
        'credential_encrypted': 'str'
    }

    attribute_map = {
        'authentication_transaction_id': 'authenticationTransactionId',
        'authentication_transaction_context': 'authenticationTransactionContext',
        'otp_token': 'otpToken',
        'authentication_type': 'authenticationType',
        'effective_authentication_type': 'effectiveAuthenticationType',
        'response_access_token': 'responseAccessToken',
        'signed_pares_status_reason': 'signedParesStatusReason',
        'signed_pares': 'signedPares',
        'white_list_status': 'whiteListStatus',
        'credential_encrypted': 'credentialEncrypted'
    }

    def __init__(self, authentication_transaction_id=None, authentication_transaction_context=None, otp_token=None, authentication_type=None, effective_authentication_type=None, response_access_token=None, signed_pares_status_reason=None, signed_pares=None, white_list_status=None, credential_encrypted=None):
        """
        Riskv1authenticationresultsConsumerAuthenticationInformation - a model defined in Swagger
        """

        self._authentication_transaction_id = None
        self._authentication_transaction_context = None
        self._otp_token = None
        self._authentication_type = None
        self._effective_authentication_type = None
        self._response_access_token = None
        self._signed_pares_status_reason = None
        self._signed_pares = None
        self._white_list_status = None
        self._credential_encrypted = None

        if authentication_transaction_id is not None:
          self.authentication_transaction_id = authentication_transaction_id
        if authentication_transaction_context is not None:
          self.authentication_transaction_context = authentication_transaction_context
        if otp_token is not None:
          self.otp_token = otp_token
        if authentication_type is not None:
          self.authentication_type = authentication_type
        if effective_authentication_type is not None:
          self.effective_authentication_type = effective_authentication_type
        if response_access_token is not None:
          self.response_access_token = response_access_token
        if signed_pares_status_reason is not None:
          self.signed_pares_status_reason = signed_pares_status_reason
        if signed_pares is not None:
          self.signed_pares = signed_pares
        if white_list_status is not None:
          self.white_list_status = white_list_status
        if credential_encrypted is not None:
          self.credential_encrypted = credential_encrypted

    @property
    def authentication_transaction_id(self):
        """
        Gets the authentication_transaction_id of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Payer authentication transaction identifier passed to link the check enrollment and validate authentication messages.For Rupay,this is passed only in Re-Send OTP usecase. **Note**: Required for Standard integration, Rupay Seamless server to server integration for enroll service. Required for Hybrid integration for validate service. 

        :return: The authentication_transaction_id of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._authentication_transaction_id

    @authentication_transaction_id.setter
    def authentication_transaction_id(self, authentication_transaction_id):
        """
        Sets the authentication_transaction_id of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Payer authentication transaction identifier passed to link the check enrollment and validate authentication messages.For Rupay,this is passed only in Re-Send OTP usecase. **Note**: Required for Standard integration, Rupay Seamless server to server integration for enroll service. Required for Hybrid integration for validate service. 

        :param authentication_transaction_id: The authentication_transaction_id of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._authentication_transaction_id = authentication_transaction_id

    @property
    def authentication_transaction_context(self):
        """
        Gets the authentication_transaction_context of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Authentication transaction context is used as a unique identifier to link enroll and validate call. 

        :return: The authentication_transaction_context of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._authentication_transaction_context

    @authentication_transaction_context.setter
    def authentication_transaction_context(self, authentication_transaction_context):
        """
        Sets the authentication_transaction_context of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Authentication transaction context is used as a unique identifier to link enroll and validate call. 

        :param authentication_transaction_context: The authentication_transaction_context of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._authentication_transaction_context = authentication_transaction_context

    @property
    def otp_token(self):
        """
        Gets the otp_token of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        OTP entered by the card holder. 

        :return: The otp_token of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._otp_token

    @otp_token.setter
    def otp_token(self, otp_token):
        """
        Sets the otp_token of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        OTP entered by the card holder. 

        :param otp_token: The otp_token of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._otp_token = otp_token

    @property
    def authentication_type(self):
        """
        Gets the authentication_type of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Indicates the type of authentication that will be used to challenge the card holder.  Possible Values:  01 - Static  02 - Dynamic  03 - OOB (Out of Band)  04 - Decoupled  20 - OTP hosted at merchant end. (Rupay S2S flow) **NOTE**:  EMV 3-D Secure version 2.1.0 supports values 01-03.  Version 2.2.0 supports values 01-04.  Decoupled authentication is not supported at this time. 

        :return: The authentication_type of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Indicates the type of authentication that will be used to challenge the card holder.  Possible Values:  01 - Static  02 - Dynamic  03 - OOB (Out of Band)  04 - Decoupled  20 - OTP hosted at merchant end. (Rupay S2S flow) **NOTE**:  EMV 3-D Secure version 2.1.0 supports values 01-03.  Version 2.2.0 supports values 01-04.  Decoupled authentication is not supported at this time. 

        :param authentication_type: The authentication_type of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._authentication_type = authentication_type

    @property
    def effective_authentication_type(self):
        """
        Gets the effective_authentication_type of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        This field describes the type of 3DS transaction flow that took place.  It can be one of three possible flows; CH - Challenge FR - Frictionless FD - Frictionless with delegation, (challenge not generated by the issuer but by the scheme on behalf of the issuer). 

        :return: The effective_authentication_type of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._effective_authentication_type

    @effective_authentication_type.setter
    def effective_authentication_type(self, effective_authentication_type):
        """
        Sets the effective_authentication_type of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        This field describes the type of 3DS transaction flow that took place.  It can be one of three possible flows; CH - Challenge FR - Frictionless FD - Frictionless with delegation, (challenge not generated by the issuer but by the scheme on behalf of the issuer). 

        :param effective_authentication_type: The effective_authentication_type of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._effective_authentication_type = effective_authentication_type

    @property
    def response_access_token(self):
        """
        Gets the response_access_token of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        JWT returned by the 3D Secure provider when the authentication is complete. Required for Hybrid integration if you use the Cybersource-generated access token. Note: Max. length of this field is 2048 characters. 

        :return: The response_access_token of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._response_access_token

    @response_access_token.setter
    def response_access_token(self, response_access_token):
        """
        Sets the response_access_token of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        JWT returned by the 3D Secure provider when the authentication is complete. Required for Hybrid integration if you use the Cybersource-generated access token. Note: Max. length of this field is 2048 characters. 

        :param response_access_token: The response_access_token of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._response_access_token = response_access_token

    @property
    def signed_pares_status_reason(self):
        """
        Gets the signed_pares_status_reason of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Provides additional information as to why the PAResStatus has a specific value. 

        :return: The signed_pares_status_reason of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._signed_pares_status_reason

    @signed_pares_status_reason.setter
    def signed_pares_status_reason(self, signed_pares_status_reason):
        """
        Sets the signed_pares_status_reason of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Provides additional information as to why the PAResStatus has a specific value. 

        :param signed_pares_status_reason: The signed_pares_status_reason of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._signed_pares_status_reason = signed_pares_status_reason

    @property
    def signed_pares(self):
        """
        Gets the signed_pares of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Payer authentication result (PARes) message returned by the card-issuing bank. If you need to show proof of enrollment checking, you may need to decrypt and parse the string for the information required by the payment card company. For more information, see \"Storing Payer Authentication Data,\" page 160. Important The value is in base64. You must remove all carriage returns and line feeds before adding the PARes to the request. 

        :return: The signed_pares of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._signed_pares

    @signed_pares.setter
    def signed_pares(self, signed_pares):
        """
        Sets the signed_pares of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Payer authentication result (PARes) message returned by the card-issuing bank. If you need to show proof of enrollment checking, you may need to decrypt and parse the string for the information required by the payment card company. For more information, see \"Storing Payer Authentication Data,\" page 160. Important The value is in base64. You must remove all carriage returns and line feeds before adding the PARes to the request. 

        :param signed_pares: The signed_pares of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._signed_pares = signed_pares

    @property
    def white_list_status(self):
        """
        Gets the white_list_status of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Enables the communication of trusted beneficiary/whitelist status between the ACS, the DS and the 3DS Requestor.  Possible Values:  Y - 3DS Requestor is whitelisted by cardholder  N - 3DS Requestor is not whitelisted by cardholder 

        :return: The white_list_status of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._white_list_status

    @white_list_status.setter
    def white_list_status(self, white_list_status):
        """
        Sets the white_list_status of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        Enables the communication of trusted beneficiary/whitelist status between the ACS, the DS and the 3DS Requestor.  Possible Values:  Y - 3DS Requestor is whitelisted by cardholder  N - 3DS Requestor is not whitelisted by cardholder 

        :param white_list_status: The white_list_status of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._white_list_status = white_list_status

    @property
    def credential_encrypted(self):
        """
        Gets the credential_encrypted of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        A flag to indicate if the passed credential has been encrypted by the Merchant.

        :return: The credential_encrypted of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._credential_encrypted

    @credential_encrypted.setter
    def credential_encrypted(self, credential_encrypted):
        """
        Sets the credential_encrypted of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        A flag to indicate if the passed credential has been encrypted by the Merchant.

        :param credential_encrypted: The credential_encrypted of this Riskv1authenticationresultsConsumerAuthenticationInformation.
        :type: str
        """



        self._credential_encrypted = credential_encrypted

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
        if not isinstance(other, Riskv1authenticationresultsConsumerAuthenticationInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
