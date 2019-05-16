# Ptsv2paymentsMerchantDefinedInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name you assign for your merchant-defined data field.  **CyberSource through VisaNet**\\ For installment payments with Mastercard in Brazil, use merchantDefinedInformation[0].key and merchantDefinedInformation[1].key for data that you want to provide to the issuer to identify the transaction.  See \&quot;Installment Payments on CyberSource through VisaNet,\&quot; page 142.  | [optional] 
**value** | **str** | The value you assign for your merchant-defined data field.  **Warning** Merchant-defined data fields are not intended to and must not be used to capture personally identifying information. Accordingly, merchants are prohibited from capturing, obtaining, and/or transmitting any personally identifying information in or via the merchant-defined data fields. Personally identifying information includes, but is not limited to, address, credit card number, social security number, driver&#39;s license number, state-issued identification number, passport number, and card verification numbers (CVV, CVC2, CVV2, CID, CVN). In the event CyberSource discovers that a merchant is capturing and/or transmitting personally identifying information via the merchant-defined data fields, whether or not intentionally, CyberSource will immediately suspend the merchant&#39;s account, which will result in a rejection of any and all transaction requests submitted by the merchant after the point of suspension.  **CyberSource through VisaNet**\\ For installment payments with Mastercard in Brazil, use merchantDefinedInformation[0].value and merchantDefinedInformation[1].value for data that you want to provide to the issuer to identify the transaction.  See \&quot;Installment Payments on CyberSource through VisaNet,\&quot; page 142.  For installment payments with Mastercard in Brazil: - The value for merchantDefinedInformation[0].value corresponds to the following data in the TC 33 capture file5:   - Record: CP07 TCR5   - Position: 25-44   - Field: Reference Field 2 - The value for merchantDefinedInformation[1].value corresponds to the following data in the TC 33 capture file5:   - Record: CP07 TCR5   - Position: 45-64   - Field: Reference Field 3  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

