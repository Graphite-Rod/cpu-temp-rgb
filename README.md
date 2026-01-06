# cpu-temp-rgb
An awfully short python3 script that changes the rgb lightning based on cpu temperature. Uses OpenHardwareMonitor and OpenRGB.

## Usage
Install the dependencies by running `pip install -r requirements.txt` and required programs (described in [Important](#important)).
Then, simply start the script by running `python rgb.py` or `py -3 rgb.py`, depending on your python installation.
The code maps the temperature in range of 40 to 90 degress Celsius to color between 0000FF (blue) and FF0000 (red) through HSL. 
It is highly recommended to read the [Tips](#tips) after.

## Important
* This solution is for OS Windows only for now.
* You need [OpenHardwareMonitor](https://openhardwaremonitor.org/) to be running.
* You need [OpenRGB](https://openrgb.org/) to be running.
* The code modifies the color for ALL DEVICES the OpenRGB server provides. You may need to modify the code to do the opposite.

## Tips
* Both OpenRGB and OpenHardwareMonitor can be set to launch on startup in the tray (background), minimizing user action.
* The script can be renamed to `rgb.pyw` and added to startup too, avoiding the console window.
* If the code does nothing, try refreshing the device list in OpenRGB.

## Extra
I would be really glad if someone suggests a way to retrieve CPU temperature with 100% success without relying on OHW.
Any modifications are more than welcome.
