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


class PtsV2PaymentsReversalsPost201Response(object):
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
        'links': 'PtsV2IncrementalAuthorizationPatch201ResponseLinks',
        'id': 'str',
        'submit_time_utc': 'str',
        'status': 'str',
        'reconciliation_id': 'str',
        'client_reference_information': 'PtsV2PaymentsPost201ResponseClientReferenceInformation',
        'reversal_amount_details': 'PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails',
        'processor_information': 'PtsV2PaymentsReversalsPost201ResponseProcessorInformation',
        'issuer_information': 'PtsV2PaymentsReversalsPost201ResponseIssuerInformation',
        'authorization_information': 'PtsV2PaymentsReversalsPost201ResponseAuthorizationInformation',
        'point_of_sale_information': 'Ptsv2paymentsidreversalsPointOfSaleInformation'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'reconciliation_id': 'reconciliationId',
        'client_reference_information': 'clientReferenceInformation',
        'reversal_amount_details': 'reversalAmountDetails',
        'processor_information': 'processorInformation',
        'issuer_information': 'issuerInformation',
        'authorization_information': 'authorizationInformation',
        'point_of_sale_information': 'pointOfSaleInformation'
    }

    def __init__(self, links=None, id=None, submit_time_utc=None, status=None, reconciliation_id=None, client_reference_information=None, reversal_amount_details=None, processor_information=None, issuer_information=None, authorization_information=None, point_of_sale_information=None):
        """
        PtsV2PaymentsReversalsPost201Response - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._submit_time_utc = None
        self._status = None
        self._reconciliation_id = None
        self._client_reference_information = None
        self._reversal_amount_details = None
        self._processor_information = None
        self._issuer_information = None
        self._authorization_information = None
        self._point_of_sale_information = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if reversal_amount_details is not None:
          self.reversal_amount_details = reversal_amount_details
        if processor_information is not None:
          self.processor_information = processor_information
        if issuer_information is not None:
          self.issuer_information = issuer_information
        if authorization_information is not None:
          self.authorization_information = authorization_information
        if point_of_sale_information is not None:
          self.point_of_sale_information = point_of_sale_information

    @property
    def links(self):
        """
        Gets the links of this PtsV2PaymentsReversalsPost201Response.

        :return: The links of this PtsV2PaymentsReversalsPost201Response.
        :rtype: PtsV2IncrementalAuthorizationPatch201ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PtsV2PaymentsReversalsPost201Response.

        :param links: The links of this PtsV2PaymentsReversalsPost201Response.
        :type: PtsV2IncrementalAuthorizationPatch201ResponseLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this PtsV2PaymentsReversalsPost201Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this PtsV2PaymentsReversalsPost201Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PtsV2PaymentsReversalsPost201Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this PtsV2PaymentsReversalsPost201Response.
        :type: str
        """

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this PtsV2PaymentsReversalsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this PtsV2PaymentsReversalsPost201Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this PtsV2PaymentsReversalsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this PtsV2PaymentsReversalsPost201Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this PtsV2PaymentsReversalsPost201Response.
        The status of the submitted transaction.  Possible values:  - REVERSED  - PARTIALLY_REVERSED 

        :return: The status of this PtsV2PaymentsReversalsPost201Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PtsV2PaymentsReversalsPost201Response.
        The status of the submitted transaction.  Possible values:  - REVERSED  - PARTIALLY_REVERSED 

        :param status: The status of this PtsV2PaymentsReversalsPost201Response.
        :type: str
        """

        self._status = status

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this PtsV2PaymentsReversalsPost201Response.
        Reference number for the transaction. Depending on how your Cybersource account is configured, this value could either be provided in the API request or generated by CyberSource. The actual value used in the request to the processor is provided back to you by Cybersource in the response. 

        :return: The reconciliation_id of this PtsV2PaymentsReversalsPost201Response.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this PtsV2PaymentsReversalsPost201Response.
        Reference number for the transaction. Depending on how your Cybersource account is configured, this value could either be provided in the API request or generated by CyberSource. The actual value used in the request to the processor is provided back to you by Cybersource in the response. 

        :param reconciliation_id: The reconciliation_id of this PtsV2PaymentsReversalsPost201Response.
        :type: str
        """

        self._reconciliation_id = reconciliation_id

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this PtsV2PaymentsReversalsPost201Response.

        :return: The client_reference_information of this PtsV2PaymentsReversalsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this PtsV2PaymentsReversalsPost201Response.

        :param client_reference_information: The client_reference_information of this PtsV2PaymentsReversalsPost201Response.
        :type: PtsV2PaymentsPost201ResponseClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def reversal_amount_details(self):
        """
        Gets the reversal_amount_details of this PtsV2PaymentsReversalsPost201Response.

        :return: The reversal_amount_details of this PtsV2PaymentsReversalsPost201Response.
        :rtype: PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails
        """
        return self._reversal_amount_details

    @reversal_amount_details.setter
    def reversal_amount_details(self, reversal_amount_details):
        """
        Sets the reversal_amount_details of this PtsV2PaymentsReversalsPost201Response.

        :param reversal_amount_details: The reversal_amount_details of this PtsV2PaymentsReversalsPost201Response.
        :type: PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails
        """

        self._reversal_amount_details = reversal_amount_details

    @property
    def processor_information(self):
        """
        Gets the processor_information of this PtsV2PaymentsReversalsPost201Response.

        :return: The processor_information of this PtsV2PaymentsReversalsPost201Response.
        :rtype: PtsV2PaymentsReversalsPost201ResponseProcessorInformation
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this PtsV2PaymentsReversalsPost201Response.

        :param processor_information: The processor_information of this PtsV2PaymentsReversalsPost201Response.
        :type: PtsV2PaymentsReversalsPost201ResponseProcessorInformation
        """

        self._processor_information = processor_information

    @property
    def issuer_information(self):
        """
        Gets the issuer_information of this PtsV2PaymentsReversalsPost201Response.

        :return: The issuer_information of this PtsV2PaymentsReversalsPost201Response.
        :rtype: PtsV2PaymentsReversalsPost201ResponseIssuerInformation
        """
        return self._issuer_information

    @issuer_information.setter
    def issuer_information(self, issuer_information):
        """
        Sets the issuer_information of this PtsV2PaymentsReversalsPost201Response.

        :param issuer_information: The issuer_information of this PtsV2PaymentsReversalsPost201Response.
        :type: PtsV2PaymentsReversalsPost201ResponseIssuerInformation
        """

        self._issuer_information = issuer_information

    @property
    def authorization_information(self):
        """
        Gets the authorization_information of this PtsV2PaymentsReversalsPost201Response.

        :return: The authorization_information of this PtsV2PaymentsReversalsPost201Response.
        :rtype: PtsV2PaymentsReversalsPost201ResponseAuthorizationInformation
        """
        return self._authorization_information

    @authorization_information.setter
    def authorization_information(self, authorization_information):
        """
        Sets the authorization_information of this PtsV2PaymentsReversalsPost201Response.

        :param authorization_information: The authorization_information of this PtsV2PaymentsReversalsPost201Response.
        :type: PtsV2PaymentsReversalsPost201ResponseAuthorizationInformation
        """

        self._authorization_information = authorization_information

    @property
    def point_of_sale_information(self):
        """
        Gets the point_of_sale_information of this PtsV2PaymentsReversalsPost201Response.

        :return: The point_of_sale_information of this PtsV2PaymentsReversalsPost201Response.
        :rtype: Ptsv2paymentsidreversalsPointOfSaleInformation
        """
        return self._point_of_sale_information

    @point_of_sale_information.setter
    def point_of_sale_information(self, point_of_sale_information):
        """
        Sets the point_of_sale_information of this PtsV2PaymentsReversalsPost201Response.

        :param point_of_sale_information: The point_of_sale_information of this PtsV2PaymentsReversalsPost201Response.
        :type: Ptsv2paymentsidreversalsPointOfSaleInformation
        """

        self._point_of_sale_information = point_of_sale_information

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
        if not isinstance(other, PtsV2PaymentsReversalsPost201Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
