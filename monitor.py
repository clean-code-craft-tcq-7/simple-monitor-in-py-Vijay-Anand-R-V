
from time import sleep
import sys

def print_info():
  for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)

def check_temperature(temperature):
  if temperature > 102 or temperature < 95:
    print('Temperature critical!')
    print_info()
    return False

  return True

def check_pulseRate(pulseRate):
  if pulseRate < 60 or pulseRate > 100:
    print('Pulse Rate is out of range!')
    print_info()
    return False

  return True

def check_spo2(spo2):
  if spo2 < 90:
    print('Oxygen Saturation out of range!')
    print_info()
    return False

  return True

def vitals_ok(temperature, pulseRate, spo2):
  return check_temperature(temperature) & check_pulseRate(pulseRate) & check_spo2(spo2)
