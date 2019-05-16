# TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_id** | **str** | Identifier for the terminal at your retail location. You can define this value yourself, but consult the processor for requirements.  For Payouts: This field is applicable for CtV.  | [optional] 
**terminal_serial_number** | **str** | Terminal serial number assigned by the hardware manufacturer. This value is provided by the client software that is installed on the POS terminal.  CyberSource does not forward this value to the processor. Instead, the value is forwarded to the CyberSource reporting functionality.  This field is supported only on American Express Direct, FDC Nashville Global, and SIX.  | [optional] 
**device_id** | **str** | The description for this field is not available. | [optional] 
**partner** | [**Ptsv2paymentsClientReferenceInformationPartner**](Ptsv2paymentsClientReferenceInformationPartner.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

