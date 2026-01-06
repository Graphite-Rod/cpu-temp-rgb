from openrgb import OpenRGBClient
from openrgb.utils import RGBColor
from typing import Tuple
import colorsys
import time
import wmi
w = wmi.WMI(namespace="root\OpenHardwareMonitor")

while True:
    try:
        cli = OpenRGBClient()
        break
    except Exception as e:
        print(e)

# print(f"Found devices: {[device.name for device in cli.devices]}")

def mix_hsl(colorA: Tuple[int, int, int], 
                  colorB: Tuple[int, int, int], 
                  proportion: float) -> Tuple[int, int, int]:
    proportion = max(0.0, min(1.0, proportion))
    r1, g1, b1 = [x / 255.0 for x in colorA]
    r2, g2, b2 = [x / 255.0 for x in colorB]
    h1, l1, s1 = colorsys.rgb_to_hls(r1, g1, b1)
    h2, l2, s2 = colorsys.rgb_to_hls(r2, g2, b2)
    dh = h2 - h1
    if abs(dh) > 0.5:
        if h1 < h2:
            h1 += 1
        else:
            h2 += 1
    h_mixed = ((1 - proportion) * h1 + proportion * h2) % 1.0
    l_mixed = (1 - proportion) * l1 + proportion * l2
    s_mixed = (1 - proportion) * s1 + proportion * s2
    r_mixed, g_mixed, b_mixed = colorsys.hls_to_rgb(h_mixed, l_mixed, s_mixed)

    return (
        int(round(r_mixed * 255)),
        int(round(g_mixed * 255)),
        int(round(b_mixed * 255))
    )

def fix(color: Tuple[int, int, int]):
    #return (color[2], color[0], color[1]) #Uncomment and edit this if you have any troubles with incorrect color channels.
    return color

def cpu_temp():
    try:
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.Name==u'CPU Package':
                return sensor.Value
    except Exception as e:
        print(e)
        return 0

colorA = (0, 0, 255) #Coldest color
colorB = (255, 0, 0) #Hottest color

while True:
    try:
        color = RGBColor(*fix(mix_hsl(colorA, colorB, (cpu_temp()-40)/(90-40)))) #Change values here to alter the boundaries for mapping.
        #print(cpu_temp(), (cpu_temp()-40)/(90-40))
        for device in cli.devices:
            device.set_color(color)
    except Exception as e:
        print(e)
    time.sleep(0.3)
