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


class TssV2TransactionsGet200Response(object):
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
        'root_id': 'str',
        'reconciliation_id': 'str',
        'merchant_id': 'str',
        'status': 'str',
        'submit_time_utc': 'str',
        'application_information': 'TssV2TransactionsGet200ResponseApplicationInformation',
        'buyer_information': 'TssV2TransactionsGet200ResponseBuyerInformation',
        'client_reference_information': 'TssV2TransactionsGet200ResponseClientReferenceInformation',
        'consumer_authentication_information': 'TssV2TransactionsGet200ResponseConsumerAuthenticationInformation',
        'device_information': 'TssV2TransactionsGet200ResponseDeviceInformation',
        'error_information': 'TssV2TransactionsGet200ResponseErrorInformation',
        'installment_information': 'TssV2TransactionsGet200ResponseInstallmentInformation',
        'fraud_marking_information': 'TssV2TransactionsGet200ResponseFraudMarkingInformation',
        'merchant_defined_information': 'list[Ptsv2paymentsMerchantDefinedInformation]',
        'merchant_information': 'TssV2TransactionsGet200ResponseMerchantInformation',
        'order_information': 'TssV2TransactionsGet200ResponseOrderInformation',
        'payment_information': 'TssV2TransactionsGet200ResponsePaymentInformation',
        'processing_information': 'TssV2TransactionsGet200ResponseProcessingInformation',
        'processor_information': 'TssV2TransactionsGet200ResponseProcessorInformation',
        'point_of_sale_information': 'TssV2TransactionsGet200ResponsePointOfSaleInformation',
        'risk_information': 'TssV2TransactionsGet200ResponseRiskInformation',
        'sender_information': 'TssV2TransactionsGet200ResponseSenderInformation',
        'links': 'TssV2TransactionsGet200ResponseLinks'
    }

    attribute_map = {
        'id': 'id',
        'root_id': 'rootId',
        'reconciliation_id': 'reconciliationId',
        'merchant_id': 'merchantId',
        'status': 'status',
        'submit_time_utc': 'submitTimeUTC',
        'application_information': 'applicationInformation',
        'buyer_information': 'buyerInformation',
        'client_reference_information': 'clientReferenceInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation',
        'device_information': 'deviceInformation',
        'error_information': 'errorInformation',
        'installment_information': 'installmentInformation',
        'fraud_marking_information': 'fraudMarkingInformation',
        'merchant_defined_information': 'merchantDefinedInformation',
        'merchant_information': 'merchantInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation',
        'processing_information': 'processingInformation',
        'processor_information': 'processorInformation',
        'point_of_sale_information': 'pointOfSaleInformation',
        'risk_information': 'riskInformation',
        'sender_information': 'senderInformation',
        'links': '_links'
    }

    def __init__(self, id=None, root_id=None, reconciliation_id=None, merchant_id=None, status=None, submit_time_utc=None, application_information=None, buyer_information=None, client_reference_information=None, consumer_authentication_information=None, device_information=None, error_information=None, installment_information=None, fraud_marking_information=None, merchant_defined_information=None, merchant_information=None, order_information=None, payment_information=None, processing_information=None, processor_information=None, point_of_sale_information=None, risk_information=None, sender_information=None, links=None):
        """
        TssV2TransactionsGet200Response - a model defined in Swagger
        """

        self._id = None
        self._root_id = None
        self._reconciliation_id = None
        self._merchant_id = None
        self._status = None
        self._submit_time_utc = None
        self._application_information = None
        self._buyer_information = None
        self._client_reference_information = None
        self._consumer_authentication_information = None
        self._device_information = None
        self._error_information = None
        self._installment_information = None
        self._fraud_marking_information = None
        self._merchant_defined_information = None
        self._merchant_information = None
        self._order_information = None
        self._payment_information = None
        self._processing_information = None
        self._processor_information = None
        self._point_of_sale_information = None
        self._risk_information = None
        self._sender_information = None
        self._links = None

        if id is not None:
          self.id = id
        if root_id is not None:
          self.root_id = root_id
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if merchant_id is not None:
          self.merchant_id = merchant_id
        if status is not None:
          self.status = status
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if application_information is not None:
          self.application_information = application_information
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information
        if device_information is not None:
          self.device_information = device_information
        if error_information is not None:
          self.error_information = error_information
        if installment_information is not None:
          self.installment_information = installment_information
        if fraud_marking_information is not None:
          self.fraud_marking_information = fraud_marking_information
        if merchant_defined_information is not None:
          self.merchant_defined_information = merchant_defined_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information
        if processing_information is not None:
          self.processing_information = processing_information
        if processor_information is not None:
          self.processor_information = processor_information
        if point_of_sale_information is not None:
          self.point_of_sale_information = point_of_sale_information
        if risk_information is not None:
          self.risk_information = risk_information
        if sender_information is not None:
          self.sender_information = sender_information
        if links is not None:
          self.links = links

    @property
    def id(self):
        """
        Gets the id of this TssV2TransactionsGet200Response.
        An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.

        :return: The id of this TssV2TransactionsGet200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TssV2TransactionsGet200Response.
        An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.

        :param id: The id of this TssV2TransactionsGet200Response.
        :type: str
        """
        if id is not None and len(id) > 26:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `26`")

        self._id = id

    @property
    def root_id(self):
        """
        Gets the root_id of this TssV2TransactionsGet200Response.
        Payment Request Id

        :return: The root_id of this TssV2TransactionsGet200Response.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """
        Sets the root_id of this TssV2TransactionsGet200Response.
        Payment Request Id

        :param root_id: The root_id of this TssV2TransactionsGet200Response.
        :type: str
        """
        if root_id is not None and len(root_id) > 26:
            raise ValueError("Invalid value for `root_id`, length must be less than or equal to `26`")

        self._root_id = root_id

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this TssV2TransactionsGet200Response.
        The reconciliation id for the submitted transaction. This value is not returned for all processors. 

        :return: The reconciliation_id of this TssV2TransactionsGet200Response.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this TssV2TransactionsGet200Response.
        The reconciliation id for the submitted transaction. This value is not returned for all processors. 

        :param reconciliation_id: The reconciliation_id of this TssV2TransactionsGet200Response.
        :type: str
        """
        if reconciliation_id is not None and len(reconciliation_id) > 60:
            raise ValueError("Invalid value for `reconciliation_id`, length must be less than or equal to `60`")

        self._reconciliation_id = reconciliation_id

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this TssV2TransactionsGet200Response.
        The description for this field is not available.

        :return: The merchant_id of this TssV2TransactionsGet200Response.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this TssV2TransactionsGet200Response.
        The description for this field is not available.

        :param merchant_id: The merchant_id of this TssV2TransactionsGet200Response.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def status(self):
        """
        Gets the status of this TssV2TransactionsGet200Response.
        The status of the submitted transaction.

        :return: The status of this TssV2TransactionsGet200Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TssV2TransactionsGet200Response.
        The status of the submitted transaction.

        :param status: The status of this TssV2TransactionsGet200Response.
        :type: str
        """

        self._status = status

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this TssV2TransactionsGet200Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :return: The submit_time_utc of this TssV2TransactionsGet200Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this TssV2TransactionsGet200Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this TssV2TransactionsGet200Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def application_information(self):
        """
        Gets the application_information of this TssV2TransactionsGet200Response.

        :return: The application_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseApplicationInformation
        """
        return self._application_information

    @application_information.setter
    def application_information(self, application_information):
        """
        Sets the application_information of this TssV2TransactionsGet200Response.

        :param application_information: The application_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseApplicationInformation
        """

        self._application_information = application_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this TssV2TransactionsGet200Response.

        :return: The buyer_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this TssV2TransactionsGet200Response.

        :param buyer_information: The buyer_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this TssV2TransactionsGet200Response.

        :return: The client_reference_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this TssV2TransactionsGet200Response.

        :param client_reference_information: The client_reference_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this TssV2TransactionsGet200Response.

        :return: The consumer_authentication_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this TssV2TransactionsGet200Response.

        :param consumer_authentication_information: The consumer_authentication_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseConsumerAuthenticationInformation
        """

        self._consumer_authentication_information = consumer_authentication_information

    @property
    def device_information(self):
        """
        Gets the device_information of this TssV2TransactionsGet200Response.

        :return: The device_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this TssV2TransactionsGet200Response.

        :param device_information: The device_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseDeviceInformation
        """

        self._device_information = device_information

    @property
    def error_information(self):
        """
        Gets the error_information of this TssV2TransactionsGet200Response.

        :return: The error_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseErrorInformation
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information):
        """
        Sets the error_information of this TssV2TransactionsGet200Response.

        :param error_information: The error_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseErrorInformation
        """

        self._error_information = error_information

    @property
    def installment_information(self):
        """
        Gets the installment_information of this TssV2TransactionsGet200Response.

        :return: The installment_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseInstallmentInformation
        """
        return self._installment_information

    @installment_information.setter
    def installment_information(self, installment_information):
        """
        Sets the installment_information of this TssV2TransactionsGet200Response.

        :param installment_information: The installment_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseInstallmentInformation
        """

        self._installment_information = installment_information

    @property
    def fraud_marking_information(self):
        """
        Gets the fraud_marking_information of this TssV2TransactionsGet200Response.

        :return: The fraud_marking_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseFraudMarkingInformation
        """
        return self._fraud_marking_information

    @fraud_marking_information.setter
    def fraud_marking_information(self, fraud_marking_information):
        """
        Sets the fraud_marking_information of this TssV2TransactionsGet200Response.

        :param fraud_marking_information: The fraud_marking_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseFraudMarkingInformation
        """

        self._fraud_marking_information = fraud_marking_information

    @property
    def merchant_defined_information(self):
        """
        Gets the merchant_defined_information of this TssV2TransactionsGet200Response.
        The description for this field is not available.

        :return: The merchant_defined_information of this TssV2TransactionsGet200Response.
        :rtype: list[Ptsv2paymentsMerchantDefinedInformation]
        """
        return self._merchant_defined_information

    @merchant_defined_information.setter
    def merchant_defined_information(self, merchant_defined_information):
        """
        Sets the merchant_defined_information of this TssV2TransactionsGet200Response.
        The description for this field is not available.

        :param merchant_defined_information: The merchant_defined_information of this TssV2TransactionsGet200Response.
        :type: list[Ptsv2paymentsMerchantDefinedInformation]
        """

        self._merchant_defined_information = merchant_defined_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this TssV2TransactionsGet200Response.

        :return: The merchant_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this TssV2TransactionsGet200Response.

        :param merchant_information: The merchant_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def order_information(self):
        """
        Gets the order_information of this TssV2TransactionsGet200Response.

        :return: The order_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this TssV2TransactionsGet200Response.

        :param order_information: The order_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this TssV2TransactionsGet200Response.

        :return: The payment_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponsePaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this TssV2TransactionsGet200Response.

        :param payment_information: The payment_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponsePaymentInformation
        """

        self._payment_information = payment_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this TssV2TransactionsGet200Response.

        :return: The processing_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this TssV2TransactionsGet200Response.

        :param processing_information: The processing_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def processor_information(self):
        """
        Gets the processor_information of this TssV2TransactionsGet200Response.

        :return: The processor_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseProcessorInformation
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this TssV2TransactionsGet200Response.

        :param processor_information: The processor_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseProcessorInformation
        """

        self._processor_information = processor_information

    @property
    def point_of_sale_information(self):
        """
        Gets the point_of_sale_information of this TssV2TransactionsGet200Response.

        :return: The point_of_sale_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponsePointOfSaleInformation
        """
        return self._point_of_sale_information

    @point_of_sale_information.setter
    def point_of_sale_information(self, point_of_sale_information):
        """
        Sets the point_of_sale_information of this TssV2TransactionsGet200Response.

        :param point_of_sale_information: The point_of_sale_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponsePointOfSaleInformation
        """

        self._point_of_sale_information = point_of_sale_information

    @property
    def risk_information(self):
        """
        Gets the risk_information of this TssV2TransactionsGet200Response.

        :return: The risk_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseRiskInformation
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this TssV2TransactionsGet200Response.

        :param risk_information: The risk_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseRiskInformation
        """

        self._risk_information = risk_information

    @property
    def sender_information(self):
        """
        Gets the sender_information of this TssV2TransactionsGet200Response.

        :return: The sender_information of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseSenderInformation
        """
        return self._sender_information

    @sender_information.setter
    def sender_information(self, sender_information):
        """
        Sets the sender_information of this TssV2TransactionsGet200Response.

        :param sender_information: The sender_information of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseSenderInformation
        """

        self._sender_information = sender_information

    @property
    def links(self):
        """
        Gets the links of this TssV2TransactionsGet200Response.

        :return: The links of this TssV2TransactionsGet200Response.
        :rtype: TssV2TransactionsGet200ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this TssV2TransactionsGet200Response.

        :param links: The links of this TssV2TransactionsGet200Response.
        :type: TssV2TransactionsGet200ResponseLinks
        """

        self._links = links

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
        if not isinstance(other, TssV2TransactionsGet200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other