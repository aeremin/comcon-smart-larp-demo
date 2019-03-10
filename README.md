Parts involved:

[zigbee2mqtt](https://zigbee2mqtt.io) - Converts ZigBee events to mqtt messages and vice versa
[Explanation of configuration file](https://www.zigbee2mqtt.io/configuration/configuration.html)
Few things in particular:
* Default channel is 11, controlled by advanced.channel.
* Default network key is 01:03:05:07:09:0b:0d:0f:00:02:04:06:08:0a:0c:0d (controlled by advanced.network_key).

[Home Assistant](https://home-assistant.io) - Software hub. Integrates well with various devices and services.
Installed via Hassbian approach (so everything else installed on top of it).

[Node Red](https://nodered.org/) - Allows for visual programming of workflows logic.
Have a lot of integrations via so-called palettes (e.g. node-red-contrib-home-assistant-websocket palette used to integrate with Home Assistant).

