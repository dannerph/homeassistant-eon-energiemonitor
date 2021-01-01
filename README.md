# Bayernwerk Energiemonitor [[Home Assistant](https://www.home-assistant.io/) Component]

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

This custom component integrates the Bayernwerk Energiemonitor into Home Assistant. A Demo can be found here: <https://energiemonitor.bayernwerk.de/demo>

## Installation

Copy content of custom_components to your local custom_components folder and add the following lines to your configuration.

## Configuration

```yaml
bw-energymonitor:
  region_code: XXXXXX
```

Configuration variables:

* **region_code**: The location ID you want to collect values from. You can find it by analyzing the network traffic of the webpage as shown in the following.

![alt text](doc/regionCode.png "Network traffic analysis ")
