# Purchase Tracking Analysis

## Current Status
Duplicate purchase events previously caused by overlapping triggers from the Fueld app on BigCommerce and GTM tags have been resolved. Purchase events are now correctly flowing to GA4.

## Identified Issues
Despite the cleanup, several issues persist:
- **Missing Orders from External Platforms**: Amazon and eBay orders, which are added via API, are not being captured in GA4.
- **Missing Orders Due to Reporting Lag**: Some orders fail to appear in reports due to delays in data processing.
- **Incorrect Date Attribution**: Certain orders are recorded on the wrong day, distorting daily performance metrics.

## Root Cause Analysis
The problems likely stem from how purchase data is sent and how the payload is handled in the current implementation. Key areas to investigate:

### Data Transmission Method
- **API Integration Gaps**: Orders from Amazon and eBay are processed through APIs that may not trigger the standard purchase event pathways used for direct BigCommerce transactions.
- **Event Firing Logic**: The conditions for firing purchase events might not account for all order sources, leading to incomplete data capture.

### Payload Handling
- **Data Structure Inconsistencies**: The payload sent to GA4 may lack uniformity, especially for API-driven orders, resulting in missing or malformed events.
- **Timestamp and Attribution Errors**: Incorrect handling of order timestamps or attribution parameters could cause orders to be logged on erroneous dates.
- **Lag in Processing**: Delays in payload processing or buffering might cause some events to be dropped or delayed beyond reporting thresholds.

To confirm these hypotheses, a thorough review of the current GTM and GA4 configurations is recommended, including:
- Examining the purchase event triggers and tags.
- Auditing API integrations for completeness.
- Testing payload structures across different order types.

## Recommendations
1. **Audit Current Implementation**: Perform a detailed code review of GTM tags, triggers, and GA4 event configurations to identify discrepancies in data handling.
2. **Enhance API Capture**: Implement or modify API webhooks to ensure Amazon and eBay orders trigger appropriate GA4 events.
3. **Improve Timestamp Accuracy**: Standardize timestamp handling to reflect actual order dates accurately.
4. **Implement Monitoring**: Add logging and alerts for purchase events to detect and address lags or missing data in real-time.
5. **Testing and Validation**: Conduct comprehensive testing across all order sources to validate data integrity before deployment.

Addressing these issues will ensure accurate and reliable purchase tracking in GA4.