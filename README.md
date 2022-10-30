# GREGORY

⋅⋅⋅Tested to work with the NodeMCU [esp32](https://sg.cytron.io/p-nodemcu-esp32) with required libraries and Touchdesigner 2022.280240.
NodeMCU needs firmware to be flashed on the board before anything can be uploaded. This [link](https://nodemcu.readthedocs.io/en/latest/flash/) was useful
How I did it was to cloud build the firmware using this [link](https://nodemcu-build.com/) and with MCUPyFlasher app - download the version which is most applicable for you [here](https://github.com/marcelstoer/nodemcu-pyflasher/releases) . After which on arduino go to library manager and dl the OSC and Esp32 Libraries so u can start working with arduino using the IDE.
⋅⋅⋅Touchdesigner has a couple of gotchas, first of which is setting up the inline and outline rules for your firewall, the second is formatting the osc out. The osc out chop in this instance is not very good- check the chop execute dat in the file for details
