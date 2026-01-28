# Created by: Michael Klements
# For Raspberry Pi Desktop Case with OLED Stats Display
# Base on Adafruit CircuitPython & SSD1306 Libraries
# Installation & Setup Instructions - https://www.the-diy-life.com/add-an-oled-stats-display-to-raspberry-pi-os-bullseye/
import time
import board
import busio
import digitalio
import RPi.GPIO as GPIO

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

#sound
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
p=GPIO.PWM(18,262)

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

#369 count
countingstr=""
count =0
tsny=48

# Display Refresh
LOOPTIME = 1.0

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 16)
#font = ImageFont.load_default()

while True:
    #369 count ++
    count+=1
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    # cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f\", $(NF-2)}'"
    # CPU = subprocess.check_output(cmd, shell = True )
    # cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    # MemUsage = subprocess.check_output(cmd, shell = True )
    # cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    # Disk = subprocess.check_output(cmd, shell = True )
    # cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    # Temp = subprocess.check_output(cmd, shell = True )

    # Pi Stats Display
    draw.text((0, 0), "IP: " + str(IP,'utf-8'), font=font, fill=255)
    # draw.text((0, 16), str(CPU,'utf-8') + "LA", font=font, fill=255)
    # draw.text((80, 16), str(Temp,'utf-8') , font=font, fill=255)
    # draw.text((0, 32), str(MemUsage,'utf-8'), font=font, fill=255)
    # draw.text((0, 48), str(Disk,'utf-8'), font=font, fill=255)
    cmd = time.localtime()
    tsn = str(count)
    if(count%10==0):
        countingstr=""
    if((tsn.find("3")!=-1 or tsn.find("6")!=-1 or tsn.find("9")!= -1)):
        p.start(50)
        p.ChangeFrequency(262)
        time.sleep(0.2)
        countingstr+="X,"
        p.stop()
    else:
        countingstr+=tsn+","
        
    time_string = "{:02d} : {:02d} : {:02d}".format(cmd.tm_hour, cmd.tm_min, cmd.tm_sec)
    draw.text((0, 16), "Time : " + time_string, font=font, fill=255)
    draw.text((0, 32), "369 Game!!", font=font, fill=255)
    draw.text((0,48),countingstr,font=font, fill=255)
    
    # Display image
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME)
