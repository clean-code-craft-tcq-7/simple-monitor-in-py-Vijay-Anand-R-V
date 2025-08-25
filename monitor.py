
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

def check_bp(bp):
  if bp[0] < 90 or bp[0] > 140 or bp[1] < 60 or bp[1] > 90:
    print('Blood Pressure is out of range!')
    print_info()
    return False

  return True

def check_respiration(respiration):
  if respiration < 12 or respiration > 20:
    print('Respiration rate is out of range!')
    print_info()
    return False

  return True

def custom_checks(*kwargs):
  results = 1
  if "bp" in kwargs:
    results &= check_bp(kwargs["bp"])
  if "respiration" in kwargs:
    results &= check_respiration(kwargs["respiration"])
  return results

def vitals_ok(temperature, pulseRate, spo2, *kwargs):
  return check_temperature(temperature) & check_pulseRate(pulseRate) & check_spo2(spo2) & custom_checks(*kwargs)
