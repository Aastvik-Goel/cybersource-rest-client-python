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


class PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation(object):
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
        'date_signed': 'str',
        'date_created': 'str',
        'date_revoked': 'str',
        'encoded_html': 'str',
        'encoded_html_popup': 'str',
        'url': 'str',
        'transaction_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'date_signed': 'dateSigned',
        'date_created': 'dateCreated',
        'date_revoked': 'dateRevoked',
        'encoded_html': 'encodedHtml',
        'encoded_html_popup': 'encodedHtmlPopup',
        'url': 'url',
        'transaction_id': 'transactionId'
    }

    def __init__(self, id=None, date_signed=None, date_created=None, date_revoked=None, encoded_html=None, encoded_html_popup=None, url=None, transaction_id=None):
        """
        PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation - a model defined in Swagger
        """

        self._id = None
        self._date_signed = None
        self._date_created = None
        self._date_revoked = None
        self._encoded_html = None
        self._encoded_html_popup = None
        self._url = None
        self._transaction_id = None

        if id is not None:
          self.id = id
        if date_signed is not None:
          self.date_signed = date_signed
        if date_created is not None:
          self.date_created = date_created
        if date_revoked is not None:
          self.date_revoked = date_revoked
        if encoded_html is not None:
          self.encoded_html = encoded_html
        if encoded_html_popup is not None:
          self.encoded_html_popup = encoded_html_popup
        if url is not None:
          self.url = url
        if transaction_id is not None:
          self.transaction_id = transaction_id

    @property
    def id(self):
        """
        Gets the id of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Identifier for the mandate. 

        :return: The id of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Identifier for the mandate. 

        :param id: The id of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :type: str
        """

        self._id = id

    @property
    def date_signed(self):
        """
        Gets the date_signed of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Date the mandate has been signed.  Format YYYYMMdd

        :return: The date_signed of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :rtype: str
        """
        return self._date_signed

    @date_signed.setter
    def date_signed(self, date_signed):
        """
        Sets the date_signed of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Date the mandate has been signed.  Format YYYYMMdd

        :param date_signed: The date_signed of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :type: str
        """

        self._date_signed = date_signed

    @property
    def date_created(self):
        """
        Gets the date_created of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Date the mandate has been created.  Format YYYYMMdd

        :return: The date_created of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Date the mandate has been created.  Format YYYYMMdd

        :param date_created: The date_created of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :type: str
        """

        self._date_created = date_created

    @property
    def date_revoked(self):
        """
        Gets the date_revoked of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Date the mandate has been revoked.  Format YYYYMMdd

        :return: The date_revoked of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :rtype: str
        """
        return self._date_revoked

    @date_revoked.setter
    def date_revoked(self, date_revoked):
        """
        Sets the date_revoked of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Date the mandate has been revoked.  Format YYYYMMdd

        :param date_revoked: The date_revoked of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :type: str
        """

        self._date_revoked = date_revoked

    @property
    def encoded_html(self):
        """
        Gets the encoded_html of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Base64 encoded html string

        :return: The encoded_html of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :rtype: str
        """
        return self._encoded_html

    @encoded_html.setter
    def encoded_html(self, encoded_html):
        """
        Sets the encoded_html of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Base64 encoded html string

        :param encoded_html: The encoded_html of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :type: str
        """

        self._encoded_html = encoded_html

    @property
    def encoded_html_popup(self):
        """
        Gets the encoded_html_popup of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Base64 encoded popup html string

        :return: The encoded_html_popup of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :rtype: str
        """
        return self._encoded_html_popup

    @encoded_html_popup.setter
    def encoded_html_popup(self, encoded_html_popup):
        """
        Sets the encoded_html_popup of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        Base64 encoded popup html string

        :param encoded_html_popup: The encoded_html_popup of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :type: str
        """

        self._encoded_html_popup = encoded_html_popup

    @property
    def url(self):
        """
        Gets the url of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        URL for redirecting the customer for creating the mandate. 

        :return: The url of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        URL for redirecting the customer for creating the mandate. 

        :param url: The url of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :type: str
        """

        self._url = url

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        The Billing Agreement ID returned by processor (PayPal). 

        :return: The transaction_id of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        The Billing Agreement ID returned by processor (PayPal). 

        :param transaction_id: The transaction_id of this PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation.
        :type: str
        """

        self._transaction_id = transaction_id

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
        if not isinstance(other, PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other