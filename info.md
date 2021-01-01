# Bayernwerk Energiemonitor

This custom component integrates the Bayernwerk Energiemonitor into Home Assistant. A Demo can be found here: <https://energiemonitor.bayernwerk.de/demo>

## Configuration

```yaml
bw-energymonitor:
  region_code: XXXXXX
```

Configuration variables:

* **region_code**: The location ID you want to collect values from. You can find it by analyzing the network traffic of the webpage as shown in the following.

![alt text](doc/regionCode.png "Network traffic analysis ")
