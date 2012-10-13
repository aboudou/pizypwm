import RPi.GPIO as GPIO
import threading
import time
 
class PiZyPwm(threading.Thread):

  def __init__(self, baseTime, nbSlices, gpioPin, gpioScheme):
     """ 
     Init the PiZyPwm instance. Expected parameters are :
     - baseTime : the base time in seconds for the PWM pattern. You may choose a small value (i.e 0.01 s)
     - nbSlices : the number of divisions of the PWM pattern. A single pulse will have a min duration of baseTime / nbSlices
     - gpioPin : the pin number which will act as PWM ouput
     - gpioScheme : the GPIO naming scheme (see RPi.GPIO documentation)
     """
     self.sliceTime = baseTime / nbSlices
     self.baseTime = baseTime
     self.nbSlices = nbSlices
     self.gpioPin = gpioPin
     self.terminated = False
     self.toTerminate = False
     GPIO.setmode(gpioScheme)

  def start(self, nbSlicesOn):
    """
    Start PWM output. Expected parameter is :
    - nbSlicesOn : number of divisions (on a total of nbSlices - see init() doc) to set HIGH output on the GPIO pin
    
    Exemple : with a total of 100 slices, a baseTime of 1 second, and an nbSlicesOn set to 25, the PWM pattern will
    have a duration of 1 second, will stay for 1/25 seconds on HIGH output, and 1/(100-25) seconds on LOW output.
    """
    self.nbSlicesOn = nbSlicesOn
    GPIO.setup(self.gpioPin, GPIO.OUT)
    self.thread = threading.Thread(None, self.run, None, (), {})
    self.thread.start()

  def run(self):
    """
    Run the PWM pattern into a background thread. This function should not be called outside of this class.
    """
    while self.toTerminate == False:
      GPIO.output(self.gpioPin, GPIO.HIGH)
      time.sleep(self.nbSlicesOn * self.sliceTime)
      GPIO.output(self.gpioPin, GPIO.LOW)
      time.sleep((self.nbSlices - self.nbSlicesOn) * self.sliceTime)
    self.terminated = True

  def changeNbSlicesOn(self, nbSlicesOn):
    """
    Change the duration of HIGH output of the pattern. Expected parameter is :
    - nbSlicesOn : number of divisions (on a total of nbSlices - see init() doc) to set HIGH output on the GPIO pin
    
    Exemple : with a total of 100 slices, a baseTime of 1 second, and an nbSlicesOn set to 25, the PWM pattern will
    have a duration of 1 second, will stay for 1/25 seconds on HIGH output, and 1/(100-25) seconds on LOW output.
    """
    self.nbSlicesOn = nbSlicesOn

  def changeNbSlices(self, nbSlices):
    """
    Change the number of slices of the PWM pattern. Expected parameter is :
    - nbSlices : number of divisions of the PWM pattern.
    
    Exemple : with a total of 100 slices, a baseTime of 1 second, and an nbSlicesOn set to 25, the PWM pattern will
    have a duration of 1 second, will stay for 1/25 seconds on HIGH output, and 1/(100-25) seconds on LOW output.
    """
    if self.nbSlicesOn > nbSlices:
      self.nbSlicesOn = nbSlices

    self.nbSlices = nbSlices
    self.sliceTime = self.baseTime / self.nbSlices

  def changeBaseTime(self, baseTime):
    """
    Change the base time of the PWM pattern. Expected parameter is :
    - baseTime : the base time in seconds for the PWM pattern.
    
    Exemple : with a total of 100 slices, a baseTime of 1 second, and an nbSlicesOn set to 25, the PWM pattern will
    have a duration of 1 second, will stay for 1/25 seconds on HIGH output, and 1/(100-25) seconds on LOW output.
    """
    self.baseTime = baseTime
    self.sliceTime = self.baseTime / self.nbSlices


  def stop(self):
    """
    Stops PWM output.
    """
    self.toTerminate = True
    while self.terminated == False:
      # Just wait
      time.sleep(0.01)
  
    GPIO.output(self.gpioPin, GPIO.LOW)
    GPIO.setup(self.gpioPin, GPIO.IN)
