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


class CreatePaymentRequest(object):
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
        'client_reference_information': 'Ptsv2paymentsClientReferenceInformation',
        'processing_information': 'Ptsv2paymentsProcessingInformation',
        'issuer_information': 'Ptsv2paymentsIssuerInformation',
        'payment_information': 'Ptsv2paymentsPaymentInformation',
        'order_information': 'Ptsv2paymentsOrderInformation',
        'buyer_information': 'Ptsv2paymentsBuyerInformation',
        'recipient_information': 'Ptsv2paymentsRecipientInformation',
        'device_information': 'Ptsv2paymentsDeviceInformation',
        'merchant_information': 'Ptsv2paymentsMerchantInformation',
        'aggregator_information': 'Ptsv2paymentsAggregatorInformation',
        'consumer_authentication_information': 'Ptsv2paymentsConsumerAuthenticationInformation',
        'point_of_sale_information': 'Ptsv2paymentsPointOfSaleInformation',
        'merchant_defined_information': 'list[Ptsv2paymentsMerchantDefinedInformation]',
        'merchant_defined_secure_information': 'Ptsv2paymentsMerchantDefinedSecureInformation',
        'installment_information': 'Ptsv2paymentsInstallmentInformation',
        'travel_information': 'Ptsv2paymentsTravelInformation',
        'health_care_information': 'Ptsv2paymentsHealthCareInformation',
        'promotion_information': 'Ptsv2paymentsPromotionInformation',
        'token_information': 'Ptsv2paymentsTokenInformation',
        'invoice_details': 'Ptsv2paymentsInvoiceDetails',
        'processor_information': 'Ptsv2paymentsProcessorInformation',
        'agreement_information': 'Ptsv2paymentsAgreementInformation',
        'risk_information': 'Ptsv2paymentsRiskInformation',
        'acquirer_information': 'Ptsv2paymentsAcquirerInformation',
        'recurring_payment_information': 'Ptsv2paymentsRecurringPaymentInformation',
        'hosted_payment_information': 'Ptsv2paymentsHostedPaymentInformation',
        'watchlist_screening_information': 'Ptsv2paymentsWatchlistScreeningInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'processing_information': 'processingInformation',
        'issuer_information': 'issuerInformation',
        'payment_information': 'paymentInformation',
        'order_information': 'orderInformation',
        'buyer_information': 'buyerInformation',
        'recipient_information': 'recipientInformation',
        'device_information': 'deviceInformation',
        'merchant_information': 'merchantInformation',
        'aggregator_information': 'aggregatorInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation',
        'point_of_sale_information': 'pointOfSaleInformation',
        'merchant_defined_information': 'merchantDefinedInformation',
        'merchant_defined_secure_information': 'merchantDefinedSecureInformation',
        'installment_information': 'installmentInformation',
        'travel_information': 'travelInformation',
        'health_care_information': 'healthCareInformation',
        'promotion_information': 'promotionInformation',
        'token_information': 'tokenInformation',
        'invoice_details': 'invoiceDetails',
        'processor_information': 'processorInformation',
        'agreement_information': 'agreementInformation',
        'risk_information': 'riskInformation',
        'acquirer_information': 'acquirerInformation',
        'recurring_payment_information': 'recurringPaymentInformation',
        'hosted_payment_information': 'hostedPaymentInformation',
        'watchlist_screening_information': 'watchlistScreeningInformation'
    }

    def __init__(self, client_reference_information=None, processing_information=None, issuer_information=None, payment_information=None, order_information=None, buyer_information=None, recipient_information=None, device_information=None, merchant_information=None, aggregator_information=None, consumer_authentication_information=None, point_of_sale_information=None, merchant_defined_information=None, merchant_defined_secure_information=None, installment_information=None, travel_information=None, health_care_information=None, promotion_information=None, token_information=None, invoice_details=None, processor_information=None, agreement_information=None, risk_information=None, acquirer_information=None, recurring_payment_information=None, hosted_payment_information=None, watchlist_screening_information=None):
        """
        CreatePaymentRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._processing_information = None
        self._issuer_information = None
        self._payment_information = None
        self._order_information = None
        self._buyer_information = None
        self._recipient_information = None
        self._device_information = None
        self._merchant_information = None
        self._aggregator_information = None
        self._consumer_authentication_information = None
        self._point_of_sale_information = None
        self._merchant_defined_information = None
        self._merchant_defined_secure_information = None
        self._installment_information = None
        self._travel_information = None
        self._health_care_information = None
        self._promotion_information = None
        self._token_information = None
        self._invoice_details = None
        self._processor_information = None
        self._agreement_information = None
        self._risk_information = None
        self._acquirer_information = None
        self._recurring_payment_information = None
        self._hosted_payment_information = None
        self._watchlist_screening_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if processing_information is not None:
          self.processing_information = processing_information
        if issuer_information is not None:
          self.issuer_information = issuer_information
        if payment_information is not None:
          self.payment_information = payment_information
        if order_information is not None:
          self.order_information = order_information
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if recipient_information is not None:
          self.recipient_information = recipient_information
        if device_information is not None:
          self.device_information = device_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if aggregator_information is not None:
          self.aggregator_information = aggregator_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information
        if point_of_sale_information is not None:
          self.point_of_sale_information = point_of_sale_information
        if merchant_defined_information is not None:
          self.merchant_defined_information = merchant_defined_information
        if merchant_defined_secure_information is not None:
          self.merchant_defined_secure_information = merchant_defined_secure_information
        if installment_information is not None:
          self.installment_information = installment_information
        if travel_information is not None:
          self.travel_information = travel_information
        if health_care_information is not None:
          self.health_care_information = health_care_information
        if promotion_information is not None:
          self.promotion_information = promotion_information
        if token_information is not None:
          self.token_information = token_information
        if invoice_details is not None:
          self.invoice_details = invoice_details
        if processor_information is not None:
          self.processor_information = processor_information
        if agreement_information is not None:
          self.agreement_information = agreement_information
        if risk_information is not None:
          self.risk_information = risk_information
        if acquirer_information is not None:
          self.acquirer_information = acquirer_information
        if recurring_payment_information is not None:
          self.recurring_payment_information = recurring_payment_information
        if hosted_payment_information is not None:
          self.hosted_payment_information = hosted_payment_information
        if watchlist_screening_information is not None:
          self.watchlist_screening_information = watchlist_screening_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this CreatePaymentRequest.

        :return: The client_reference_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this CreatePaymentRequest.

        :param client_reference_information: The client_reference_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsClientReferenceInformation
        """



        self._client_reference_information = client_reference_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this CreatePaymentRequest.

        :return: The processing_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this CreatePaymentRequest.

        :param processing_information: The processing_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsProcessingInformation
        """



        self._processing_information = processing_information

    @property
    def issuer_information(self):
        """
        Gets the issuer_information of this CreatePaymentRequest.

        :return: The issuer_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsIssuerInformation
        """
        return self._issuer_information

    @issuer_information.setter
    def issuer_information(self, issuer_information):
        """
        Sets the issuer_information of this CreatePaymentRequest.

        :param issuer_information: The issuer_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsIssuerInformation
        """



        self._issuer_information = issuer_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this CreatePaymentRequest.

        :return: The payment_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this CreatePaymentRequest.

        :param payment_information: The payment_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsPaymentInformation
        """



        self._payment_information = payment_information

    @property
    def order_information(self):
        """
        Gets the order_information of this CreatePaymentRequest.

        :return: The order_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this CreatePaymentRequest.

        :param order_information: The order_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsOrderInformation
        """



        self._order_information = order_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this CreatePaymentRequest.

        :return: The buyer_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this CreatePaymentRequest.

        :param buyer_information: The buyer_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsBuyerInformation
        """



        self._buyer_information = buyer_information

    @property
    def recipient_information(self):
        """
        Gets the recipient_information of this CreatePaymentRequest.

        :return: The recipient_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsRecipientInformation
        """
        return self._recipient_information

    @recipient_information.setter
    def recipient_information(self, recipient_information):
        """
        Sets the recipient_information of this CreatePaymentRequest.

        :param recipient_information: The recipient_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsRecipientInformation
        """



        self._recipient_information = recipient_information

    @property
    def device_information(self):
        """
        Gets the device_information of this CreatePaymentRequest.

        :return: The device_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this CreatePaymentRequest.

        :param device_information: The device_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsDeviceInformation
        """



        self._device_information = device_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this CreatePaymentRequest.

        :return: The merchant_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this CreatePaymentRequest.

        :param merchant_information: The merchant_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsMerchantInformation
        """



        self._merchant_information = merchant_information

    @property
    def aggregator_information(self):
        """
        Gets the aggregator_information of this CreatePaymentRequest.

        :return: The aggregator_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsAggregatorInformation
        """
        return self._aggregator_information

    @aggregator_information.setter
    def aggregator_information(self, aggregator_information):
        """
        Sets the aggregator_information of this CreatePaymentRequest.

        :param aggregator_information: The aggregator_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsAggregatorInformation
        """



        self._aggregator_information = aggregator_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this CreatePaymentRequest.

        :return: The consumer_authentication_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this CreatePaymentRequest.

        :param consumer_authentication_information: The consumer_authentication_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsConsumerAuthenticationInformation
        """



        self._consumer_authentication_information = consumer_authentication_information

    @property
    def point_of_sale_information(self):
        """
        Gets the point_of_sale_information of this CreatePaymentRequest.

        :return: The point_of_sale_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsPointOfSaleInformation
        """
        return self._point_of_sale_information

    @point_of_sale_information.setter
    def point_of_sale_information(self, point_of_sale_information):
        """
        Sets the point_of_sale_information of this CreatePaymentRequest.

        :param point_of_sale_information: The point_of_sale_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsPointOfSaleInformation
        """



        self._point_of_sale_information = point_of_sale_information

    @property
    def merchant_defined_information(self):
        """
        Gets the merchant_defined_information of this CreatePaymentRequest.
        The object containing the custom data that the merchant defines. 

        :return: The merchant_defined_information of this CreatePaymentRequest.
        :rtype: list[Ptsv2paymentsMerchantDefinedInformation]
        """
        return self._merchant_defined_information

    @merchant_defined_information.setter
    def merchant_defined_information(self, merchant_defined_information):
        """
        Sets the merchant_defined_information of this CreatePaymentRequest.
        The object containing the custom data that the merchant defines. 

        :param merchant_defined_information: The merchant_defined_information of this CreatePaymentRequest.
        :type: list[Ptsv2paymentsMerchantDefinedInformation]
        """



        self._merchant_defined_information = merchant_defined_information

    @property
    def merchant_defined_secure_information(self):
        """
        Gets the merchant_defined_secure_information of this CreatePaymentRequest.

        :return: The merchant_defined_secure_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsMerchantDefinedSecureInformation
        """
        return self._merchant_defined_secure_information

    @merchant_defined_secure_information.setter
    def merchant_defined_secure_information(self, merchant_defined_secure_information):
        """
        Sets the merchant_defined_secure_information of this CreatePaymentRequest.

        :param merchant_defined_secure_information: The merchant_defined_secure_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsMerchantDefinedSecureInformation
        """



        self._merchant_defined_secure_information = merchant_defined_secure_information

    @property
    def installment_information(self):
        """
        Gets the installment_information of this CreatePaymentRequest.

        :return: The installment_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsInstallmentInformation
        """
        return self._installment_information

    @installment_information.setter
    def installment_information(self, installment_information):
        """
        Sets the installment_information of this CreatePaymentRequest.

        :param installment_information: The installment_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsInstallmentInformation
        """



        self._installment_information = installment_information

    @property
    def travel_information(self):
        """
        Gets the travel_information of this CreatePaymentRequest.

        :return: The travel_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsTravelInformation
        """
        return self._travel_information

    @travel_information.setter
    def travel_information(self, travel_information):
        """
        Sets the travel_information of this CreatePaymentRequest.

        :param travel_information: The travel_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsTravelInformation
        """



        self._travel_information = travel_information

    @property
    def health_care_information(self):
        """
        Gets the health_care_information of this CreatePaymentRequest.

        :return: The health_care_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsHealthCareInformation
        """
        return self._health_care_information

    @health_care_information.setter
    def health_care_information(self, health_care_information):
        """
        Sets the health_care_information of this CreatePaymentRequest.

        :param health_care_information: The health_care_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsHealthCareInformation
        """



        self._health_care_information = health_care_information

    @property
    def promotion_information(self):
        """
        Gets the promotion_information of this CreatePaymentRequest.

        :return: The promotion_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsPromotionInformation
        """
        return self._promotion_information

    @promotion_information.setter
    def promotion_information(self, promotion_information):
        """
        Sets the promotion_information of this CreatePaymentRequest.

        :param promotion_information: The promotion_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsPromotionInformation
        """



        self._promotion_information = promotion_information

    @property
    def token_information(self):
        """
        Gets the token_information of this CreatePaymentRequest.

        :return: The token_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsTokenInformation
        """
        return self._token_information

    @token_information.setter
    def token_information(self, token_information):
        """
        Sets the token_information of this CreatePaymentRequest.

        :param token_information: The token_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsTokenInformation
        """



        self._token_information = token_information

    @property
    def invoice_details(self):
        """
        Gets the invoice_details of this CreatePaymentRequest.

        :return: The invoice_details of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsInvoiceDetails
        """
        return self._invoice_details

    @invoice_details.setter
    def invoice_details(self, invoice_details):
        """
        Sets the invoice_details of this CreatePaymentRequest.

        :param invoice_details: The invoice_details of this CreatePaymentRequest.
        :type: Ptsv2paymentsInvoiceDetails
        """



        self._invoice_details = invoice_details

    @property
    def processor_information(self):
        """
        Gets the processor_information of this CreatePaymentRequest.

        :return: The processor_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsProcessorInformation
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this CreatePaymentRequest.

        :param processor_information: The processor_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsProcessorInformation
        """



        self._processor_information = processor_information

    @property
    def agreement_information(self):
        """
        Gets the agreement_information of this CreatePaymentRequest.

        :return: The agreement_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsAgreementInformation
        """
        return self._agreement_information

    @agreement_information.setter
    def agreement_information(self, agreement_information):
        """
        Sets the agreement_information of this CreatePaymentRequest.

        :param agreement_information: The agreement_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsAgreementInformation
        """



        self._agreement_information = agreement_information

    @property
    def risk_information(self):
        """
        Gets the risk_information of this CreatePaymentRequest.

        :return: The risk_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsRiskInformation
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this CreatePaymentRequest.

        :param risk_information: The risk_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsRiskInformation
        """



        self._risk_information = risk_information

    @property
    def acquirer_information(self):
        """
        Gets the acquirer_information of this CreatePaymentRequest.

        :return: The acquirer_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsAcquirerInformation
        """
        return self._acquirer_information

    @acquirer_information.setter
    def acquirer_information(self, acquirer_information):
        """
        Sets the acquirer_information of this CreatePaymentRequest.

        :param acquirer_information: The acquirer_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsAcquirerInformation
        """



        self._acquirer_information = acquirer_information

    @property
    def recurring_payment_information(self):
        """
        Gets the recurring_payment_information of this CreatePaymentRequest.

        :return: The recurring_payment_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsRecurringPaymentInformation
        """
        return self._recurring_payment_information

    @recurring_payment_information.setter
    def recurring_payment_information(self, recurring_payment_information):
        """
        Sets the recurring_payment_information of this CreatePaymentRequest.

        :param recurring_payment_information: The recurring_payment_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsRecurringPaymentInformation
        """



        self._recurring_payment_information = recurring_payment_information

    @property
    def hosted_payment_information(self):
        """
        Gets the hosted_payment_information of this CreatePaymentRequest.

        :return: The hosted_payment_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsHostedPaymentInformation
        """
        return self._hosted_payment_information

    @hosted_payment_information.setter
    def hosted_payment_information(self, hosted_payment_information):
        """
        Sets the hosted_payment_information of this CreatePaymentRequest.

        :param hosted_payment_information: The hosted_payment_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsHostedPaymentInformation
        """



        self._hosted_payment_information = hosted_payment_information

    @property
    def watchlist_screening_information(self):
        """
        Gets the watchlist_screening_information of this CreatePaymentRequest.

        :return: The watchlist_screening_information of this CreatePaymentRequest.
        :rtype: Ptsv2paymentsWatchlistScreeningInformation
        """
        return self._watchlist_screening_information

    @watchlist_screening_information.setter
    def watchlist_screening_information(self, watchlist_screening_information):
        """
        Sets the watchlist_screening_information of this CreatePaymentRequest.

        :param watchlist_screening_information: The watchlist_screening_information of this CreatePaymentRequest.
        :type: Ptsv2paymentsWatchlistScreeningInformation
        """



        self._watchlist_screening_information = watchlist_screening_information

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
        if not isinstance(other, CreatePaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
