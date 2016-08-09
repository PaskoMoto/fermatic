# fermatic
Python script to monitor cellid number information via d-bus protocol.
Tested & developed in a Jolla Phone.

This script does the following:
If your device is camped in one of the cells of your list it disables all PDP contexts and activates your WIFI interface (i.e: as if you were at home). Conversely, if you're not in the HOME set of cellids, your WiFi interface is disabled and the internet PDP context is (re)activated.
This allows you to avoid broadcasting of your WiFi interface mac address when you're not at home.

Requirements.
.- Create a forder called 'fermatic' under /home/nemo/.
.- You have to create a file called cellid.txt with a list of all the cellid's you want to trigger your action.
.- You have to insert the value of your IMSI number in the appropriate place. (replace YOUR_IMSI_NUMBER_HERE string with your IMSI number)
.- If you are planning to create a new .service file to start the service after reboots create a file called log.txt with permissions 666 and owner:group like nemo:nemo inside the folder /home/nemo/fermatic/

With a few tweaks it should also be possible to activate an VPN connection when you are not at home & deactivate it when you are at home.
