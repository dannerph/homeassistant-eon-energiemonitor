# EON Energiemonitor

This custom component integrates the EON Energiemonitor into Home Assistant. The sensor values are fetched from the API that is the backend of the EON Energiemonitor and follows the visualization in <https://energiemonitor.bayernwerk.de/demo>.

## Configuration

```yaml
eon-energiemonitor:
  region_code: XXXXXX
```

Configuration variables:

* **region_code**: The location ID you want to collect values from. You can find it by analyzing the network traffic of the webpage as shown in the following.

![alt text](doc/regionCode.png "Network traffic analysis ")
