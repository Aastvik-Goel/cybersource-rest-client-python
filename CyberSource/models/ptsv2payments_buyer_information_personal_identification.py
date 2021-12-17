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


class Ptsv2paymentsBuyerInformationPersonalIdentification(object):
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
        'type': 'str',
        'id': 'str',
        'issued_by': 'str',
        'verification_results': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'issued_by': 'issuedBy',
        'verification_results': 'verificationResults'
    }

    def __init__(self, type=None, id=None, issued_by=None, verification_results=None):
        """
        Ptsv2paymentsBuyerInformationPersonalIdentification - a model defined in Swagger
        """

        self._type = None
        self._id = None
        self._issued_by = None
        self._verification_results = None

        if type is not None:
          self.type = type
        if id is not None:
          self.id = id
        if issued_by is not None:
          self.issued_by = issued_by
        if verification_results is not None:
          self.verification_results = verification_results

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        The type of the identification.  Possible values:   - `NATIONAL`   - `CPF`   - `CPNJ`   - `CURP`   - `SSN`   - `DRIVER_LICENSE`   - `PASSPORT_NUMBER`   - `PERSONAL_ID`   - `TAX_ID`  This field is supported only on the following processors.  #### ComercioLatino Set this field to the Cadastro de Pessoas Fisicas (CPF).  #### CyberSource Latin American Processing Supported for Redecard in Brazil. Set this field to the Cadastro de Pessoas Fisicas (CPF), which is required for AVS for Redecard in Brazil. **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called CyberSource Latin American Processing. It is not for any other Latin American processors that CyberSource supports.  For processor-specific information, see the `personal_id` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The type of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        The type of the identification.  Possible values:   - `NATIONAL`   - `CPF`   - `CPNJ`   - `CURP`   - `SSN`   - `DRIVER_LICENSE`   - `PASSPORT_NUMBER`   - `PERSONAL_ID`   - `TAX_ID`  This field is supported only on the following processors.  #### ComercioLatino Set this field to the Cadastro de Pessoas Fisicas (CPF).  #### CyberSource Latin American Processing Supported for Redecard in Brazil. Set this field to the Cadastro de Pessoas Fisicas (CPF), which is required for AVS for Redecard in Brazil. **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called CyberSource Latin American Processing. It is not for any other Latin American processors that CyberSource supports.  For processor-specific information, see the `personal_id` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param type: The type of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """
        Gets the id of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        The value of the identification type. This field is supported only on the following processors.  #### ComercioLatino Set this field to the Cadastro de Pessoas Fisicas (CPF).  #### CyberSource Latin American Processing Supported for Redecard in Brazil. Set this field to the Cadastro de Pessoas Fisicas (CPF), which is required for AVS for Redecard in Brazil. **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called CyberSource Latin American Processing. It is not for any other Latin American processors that CyberSource supports.  For processor-specific information, see the `personal_id` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)    If `type = PASSPORT`, this is the cardholder's passport number. Recommended for Discover ProtectBuy. 

        :return: The id of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        The value of the identification type. This field is supported only on the following processors.  #### ComercioLatino Set this field to the Cadastro de Pessoas Fisicas (CPF).  #### CyberSource Latin American Processing Supported for Redecard in Brazil. Set this field to the Cadastro de Pessoas Fisicas (CPF), which is required for AVS for Redecard in Brazil. **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called CyberSource Latin American Processing. It is not for any other Latin American processors that CyberSource supports.  For processor-specific information, see the `personal_id` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)    If `type = PASSPORT`, this is the cardholder's passport number. Recommended for Discover ProtectBuy. 

        :param id: The id of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        :type: str
        """

        self._id = id

    @property
    def issued_by(self):
        """
        Gets the issued_by of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        The government agency that issued the driver's license or passport.  If **type**` = DRIVER_LICENSE`, this is the State or province where the customer’s driver’s license was issued.  If **type**` = PASSPORT`, this is the Issuing country for the cardholder’s passport. Recommended for Discover ProtectBuy.  Use the two-character [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  #### TeleCheck Contact your TeleCheck representative to find out whether this field is required or optional.  #### All Other Processors Not used.  For details about the country that issued the passport, see `customer_passport_country` field description in [CyberSource Payer Authentication Using the SCMP API] (https://apps.cybersource.com/library/documentation/dev_guides/Payer_Authentication_SCMP_API/html/)  For details about the state or province that issued the passport, see `driver_license_state` field description in [Electronic Check Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/) 

        :return: The issued_by of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        :rtype: str
        """
        return self._issued_by

    @issued_by.setter
    def issued_by(self, issued_by):
        """
        Sets the issued_by of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        The government agency that issued the driver's license or passport.  If **type**` = DRIVER_LICENSE`, this is the State or province where the customer’s driver’s license was issued.  If **type**` = PASSPORT`, this is the Issuing country for the cardholder’s passport. Recommended for Discover ProtectBuy.  Use the two-character [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  #### TeleCheck Contact your TeleCheck representative to find out whether this field is required or optional.  #### All Other Processors Not used.  For details about the country that issued the passport, see `customer_passport_country` field description in [CyberSource Payer Authentication Using the SCMP API] (https://apps.cybersource.com/library/documentation/dev_guides/Payer_Authentication_SCMP_API/html/)  For details about the state or province that issued the passport, see `driver_license_state` field description in [Electronic Check Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/) 

        :param issued_by: The issued_by of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        :type: str
        """

        self._issued_by = issued_by

    @property
    def verification_results(self):
        """
        Gets the verification_results of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        Verification results received from Issuer or Card Network for verification transactions. Response Only Field. 

        :return: The verification_results of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        :rtype: str
        """
        return self._verification_results

    @verification_results.setter
    def verification_results(self, verification_results):
        """
        Sets the verification_results of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        Verification results received from Issuer or Card Network for verification transactions. Response Only Field. 

        :param verification_results: The verification_results of this Ptsv2paymentsBuyerInformationPersonalIdentification.
        :type: str
        """

        self._verification_results = verification_results

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
        if not isinstance(other, Ptsv2paymentsBuyerInformationPersonalIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
