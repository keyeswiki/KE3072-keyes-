#导入引脚和时间模块
from machine import Pin  
import time  
 
# 定义避障传感器，led的引脚
sensor_avoid = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(18, machine.Pin.OUT)
 
while True:
      value = sensor_avoid.value()
      if value == 0:
          print("0  ALARM! Obstacles detected!")
          led.value(1)
          time.sleep(0.2)
          led.value(0)
          time.sleep(0.2)         
      else:
          led.value(0)