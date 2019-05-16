# Ptsv2paymentsProcessingInformationAuthorizationOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Authorization type.  Possible values:   - **AUTOCAPTURE**: automatic capture.  - **STANDARDCAPTURE**: standard capture.  - **VERBAL**: forced capture. Include it in the payment request for a forced capture. Include it in the capture request for a verbal payment.  **Asia, Middle East, and Africa Gateway; Cielo; Comercio Latino; and CyberSource Latin American Processing**\\ Set this field to _AUTOCAPTURE_ and include it in a bundled request to indicate that you are requesting an automatic capture. If your account is configured to enable automatic captures, set this field to STANDARDCAPTURE and include it in a standard authorization or bundled request to indicate that you are overriding an automatic capture. For more information, see \&quot;Automatic Captures,\&quot; page 33.  **Forced Capture**\\ Set this field to _VERBAL_ and include it in the authorization request to indicate that you are performing a forced capture; therefore, you receive the authorization code outside the CyberSource system. For more information, see \&quot;Forced Captures,\&quot; page 123.  **Verbal Authorization**\\ Set this field to _VERBAL_ and include it in the capture request to indicate that the request is for a verbal authorization. For more information, see \&quot;Verbal Authorizations,\&quot; page 84.  For processor-specific information, see the auth_type field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  | [optional] 
**verbal_auth_code** | **str** | Authorization code.  **Forced Capture**\\ Use this field to send the authorization code you received from a payment that you authorized outside the CyberSource system.  **Verbal Authorization**\\ Use this field in CAPTURE API to send the verbally received authorization code.  For processor-specific information, see the _auth_code_ field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  | [optional] 
**verbal_auth_transaction_id** | **str** | Transaction ID (TID). | [optional] 
**auth_indicator** | **str** | Flag that specifies the purpose of the authorization.  Possible values:  - **0**: Preauthorization  - **1**: Final authorization  To set the default for this field, contact CyberSource Customer Support. See \&quot;Final Authorization Indicator,\&quot; page 119.  Barclays and Elavon The default for Barclays and Elavon is 1 (final authorization). To change the default for this field, contact CyberSource Customer Support.  CyberSource through VisaNet When the value for this field is 0, it corresponds to the following data in the TC 33 capture file5:  - Record: CP01 TCR0  - Position: 164  - Field: Additional Authorization Indicators When the value for this field is 1, it does not correspond to any data in the TC 33 capture file.  For processor-specific information, see the auth_indicator field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  | [optional] 
**partial_auth_indicator** | **bool** | Flag that indicates whether the transaction is enabled for partial authorization or not. When your request includes this field, this value overrides the information in your CyberSource account.  For processor-specific information, see the _auth_partial_auth_indicator_ field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  **CyberSource through VisaNet**\\ To set the default for this field, contact CyberSource Customer Support. The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR0 - Position: 164 - Field: Additional Authorization Indicators  Possible values: - **true** Enable the transaction for partial authorization. - **false** Do not enable the transaction for partial authorization.  | [optional] 
**balance_inquiry** | **bool** | Flag that indicates whether to return balance information.  Possible values: - **true** - **false**  | [optional] 
**ignore_avs_result** | **bool** | Flag that indicates whether to allow the capture service to run, even when the payment receives an AVS decline.  Possible values: - **true**  Ignore the results of AVS checking and run the capture service. - **false**  (default): If the authorization receives an AVS decline, do not run the capture service.  | [optional] [default to False]
**decline_avs_flags** | **list[str]** | An array of AVS flags that cause the reply flag to be returned.  &#x60;Important&#x60; To receive declines for the AVS code N, include the value N in the array.  Possible values: - D - A - V - S - N - O  | [optional] 
**ignore_cv_result** | **bool** | Flag that indicates whether to allow the capture service to run even when the payment receives a CVN decline.  Possible values: - **true**  Ignore the results of CVN checking and run the capture service. - **false**  (default) If the authorization receives a CVN decline, do not run the capture service.  | [optional] [default to False]
**initiator** | [**Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator**](Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.md) |  | [optional] 
**bill_payment** | **bool** | Flag that indicates that this is a payment for a bill or for an existing contractual loan. See \&quot;Visa Bill Payments,\&quot; page 220, and \&quot;Visa Debt Repayments,\&quot; page 221, for lists of processors that support these features.  Possible values: - true: Bill payment or loan payment. - false (default): Not a bill payment or loan payment.  | [optional] 
**bill_payment_type** | **str** | Reason for the payment.  Possible values: - 001: Utility payment - 002: Government services - 003: Mobile phone top-up - 004: Coupon payment  The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP07 TCR0 - Position: 48-50 - Field: Bill Payment Transaction Type Identifier  This field is supported only for bill payments in Brazil with Mastercard on CyberSource through VisaNet. See Mastercard Bill Payments.  Note For information about bill payments with Visa, see Visa Bill Payments.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

