# 导入 Pin and time 库.
from machine import Pin
import time 

# 定义避障传感器和led的引脚. 
sensor_avoid = Pin(15, Pin.IN)
led = Pin(2, Pin.OUT)

while True: 
      value = sensor_avoid.value()
      if value == 0:
          print("0  ALARM! Obstacles detected!")
          led.value(1)
          time.sleep(0.5)
          led.value(0)
          time.sleep(0.5)         
      else:
          led.value(0)