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


class PtsV2PaymentsOrderPost201Response(object):
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
        'client_reference_information': 'PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation',
        'processor_information': 'PtsV2PaymentsOrderPost201ResponseProcessorInformation',
        'order_information': 'PtsV2PaymentsOrderPost201ResponseOrderInformation',
        'payment_information': 'PtsV2PaymentsOrderPost201ResponsePaymentInformation',
        'processing_information': 'PtsV2PaymentsOrderPost201ResponseProcessingInformation',
        'buyer_information': 'PtsV2PaymentsOrderPost201ResponseBuyerInformation',
        'submit_time_utc': 'str',
        'status': 'str',
        'reconciliation_id': 'str',
        'risk_information': 'PtsV2PaymentsPost201ResponseRiskInformationProcessorResults'
    }

    attribute_map = {
        'id': 'id',
        'client_reference_information': 'clientReferenceInformation',
        'processor_information': 'processorInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation',
        'processing_information': 'processingInformation',
        'buyer_information': 'buyerInformation',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'reconciliation_id': 'reconciliationId',
        'risk_information': 'riskInformation'
    }

    def __init__(self, id=None, client_reference_information=None, processor_information=None, order_information=None, payment_information=None, processing_information=None, buyer_information=None, submit_time_utc=None, status=None, reconciliation_id=None, risk_information=None):
        """
        PtsV2PaymentsOrderPost201Response - a model defined in Swagger
        """

        self._id = None
        self._client_reference_information = None
        self._processor_information = None
        self._order_information = None
        self._payment_information = None
        self._processing_information = None
        self._buyer_information = None
        self._submit_time_utc = None
        self._status = None
        self._reconciliation_id = None
        self._risk_information = None

        if id is not None:
          self.id = id
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if processor_information is not None:
          self.processor_information = processor_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information
        if processing_information is not None:
          self.processing_information = processing_information
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if risk_information is not None:
          self.risk_information = risk_information

    @property
    def id(self):
        """
        Gets the id of this PtsV2PaymentsOrderPost201Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this PtsV2PaymentsOrderPost201Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PtsV2PaymentsOrderPost201Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this PtsV2PaymentsOrderPost201Response.
        :type: str
        """

        self._id = id

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this PtsV2PaymentsOrderPost201Response.

        :return: The client_reference_information of this PtsV2PaymentsOrderPost201Response.
        :rtype: PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this PtsV2PaymentsOrderPost201Response.

        :param client_reference_information: The client_reference_information of this PtsV2PaymentsOrderPost201Response.
        :type: PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def processor_information(self):
        """
        Gets the processor_information of this PtsV2PaymentsOrderPost201Response.

        :return: The processor_information of this PtsV2PaymentsOrderPost201Response.
        :rtype: PtsV2PaymentsOrderPost201ResponseProcessorInformation
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this PtsV2PaymentsOrderPost201Response.

        :param processor_information: The processor_information of this PtsV2PaymentsOrderPost201Response.
        :type: PtsV2PaymentsOrderPost201ResponseProcessorInformation
        """

        self._processor_information = processor_information

    @property
    def order_information(self):
        """
        Gets the order_information of this PtsV2PaymentsOrderPost201Response.

        :return: The order_information of this PtsV2PaymentsOrderPost201Response.
        :rtype: PtsV2PaymentsOrderPost201ResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this PtsV2PaymentsOrderPost201Response.

        :param order_information: The order_information of this PtsV2PaymentsOrderPost201Response.
        :type: PtsV2PaymentsOrderPost201ResponseOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this PtsV2PaymentsOrderPost201Response.

        :return: The payment_information of this PtsV2PaymentsOrderPost201Response.
        :rtype: PtsV2PaymentsOrderPost201ResponsePaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this PtsV2PaymentsOrderPost201Response.

        :param payment_information: The payment_information of this PtsV2PaymentsOrderPost201Response.
        :type: PtsV2PaymentsOrderPost201ResponsePaymentInformation
        """

        self._payment_information = payment_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this PtsV2PaymentsOrderPost201Response.

        :return: The processing_information of this PtsV2PaymentsOrderPost201Response.
        :rtype: PtsV2PaymentsOrderPost201ResponseProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this PtsV2PaymentsOrderPost201Response.

        :param processing_information: The processing_information of this PtsV2PaymentsOrderPost201Response.
        :type: PtsV2PaymentsOrderPost201ResponseProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this PtsV2PaymentsOrderPost201Response.

        :return: The buyer_information of this PtsV2PaymentsOrderPost201Response.
        :rtype: PtsV2PaymentsOrderPost201ResponseBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this PtsV2PaymentsOrderPost201Response.

        :param buyer_information: The buyer_information of this PtsV2PaymentsOrderPost201Response.
        :type: PtsV2PaymentsOrderPost201ResponseBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this PtsV2PaymentsOrderPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this PtsV2PaymentsOrderPost201Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this PtsV2PaymentsOrderPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this PtsV2PaymentsOrderPost201Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this PtsV2PaymentsOrderPost201Response.
        The status of the submitted transaction. Possible values:   - CREATED   - SAVED   - APPROVED   - VOIDED   - COMPLETED   - PAYER_ACTION_REQUIRED 

        :return: The status of this PtsV2PaymentsOrderPost201Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PtsV2PaymentsOrderPost201Response.
        The status of the submitted transaction. Possible values:   - CREATED   - SAVED   - APPROVED   - VOIDED   - COMPLETED   - PAYER_ACTION_REQUIRED 

        :param status: The status of this PtsV2PaymentsOrderPost201Response.
        :type: str
        """

        self._status = status

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this PtsV2PaymentsOrderPost201Response.
        Reference number for the transaction. Depending on how your Cybersource account is configured, this value could either be provided in the API request or generated by CyberSource. The actual value used in the request to the processor is provided back to you by Cybersource in the response. 

        :return: The reconciliation_id of this PtsV2PaymentsOrderPost201Response.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this PtsV2PaymentsOrderPost201Response.
        Reference number for the transaction. Depending on how your Cybersource account is configured, this value could either be provided in the API request or generated by CyberSource. The actual value used in the request to the processor is provided back to you by Cybersource in the response. 

        :param reconciliation_id: The reconciliation_id of this PtsV2PaymentsOrderPost201Response.
        :type: str
        """

        self._reconciliation_id = reconciliation_id

    @property
    def risk_information(self):
        """
        Gets the risk_information of this PtsV2PaymentsOrderPost201Response.

        :return: The risk_information of this PtsV2PaymentsOrderPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationProcessorResults
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this PtsV2PaymentsOrderPost201Response.

        :param risk_information: The risk_information of this PtsV2PaymentsOrderPost201Response.
        :type: PtsV2PaymentsPost201ResponseRiskInformationProcessorResults
        """

        self._risk_information = risk_information

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
        if not isinstance(other, PtsV2PaymentsOrderPost201Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other