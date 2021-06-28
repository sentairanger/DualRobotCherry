# Import libraries
import cherrypy
import logging
from gpiozero import OutputDevice, PWMOutputDevice, LED, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

# import factories
factory = PiGPIOFactory(host='192.168.0.22')
factory2 = PiGPIOFactory(host='192.168.0.21')

# Define motor pins, leds and servos
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

linus_eye = LED(16, pin_factory=factory)
torvalds_eye = LED(25, pin_factory=factory2)

angular_servo = AngularServo(22, min_angle=-90, max_angle=90, pin_factory=factory)
angular_servo2 = AngularServo(23, min_angle=-90, max_angle=90, pin_factory=factory)

#Define class and functions for movement, servo movement and pwm control
class DualRobot(object):
    @cherrypy.expose
    # main index file
    def index(self):
        return open("dual_cherry.html")
    @cherrypy.expose
    def forward(self):
        pin1.off()
        pin2.on()
        pin3.on()
        pin4.off()
        return open("dual_cherry.html")
    @cherrypy.expose
    def backward(self):
        pin1.on()
        pin2.off()
        pin3.off()
        pin4.on()
        return open("dual_cherry.html")
    @cherrypy.expose
    def left(self):
        pin1.on()
        pin2.off()
        pin3.on()
        pin4.off()
        return open("dual_cherry.html")
    @cherrypy.expose
    def right(self):
        pin1.off()
        pin2.on()
        pin3.off()
        pin4.on()
        return open("dual_cherry.html")
    @cherrypy.expose
    def stop(self):
        pin1.off()
        pin2.off()
        pin3.off()
        pin4.off()
        return open("dual_cherry.html")
    @cherrypy.expose
    def torvaldson(self):
        torvalds_eye.on()
        return open("dual_cherry.html")
    @cherrypy.expose
    def torvaldsoff(self):
        torvalds_eye.off()
        return open("dual_cherry.html")
    @cherrypy.expose
    def eyeon(self):
        linus_eye.on()
        return open("dual_cherry.html")
    @cherrypy.expose
    def eyeoff(self):
        linus_eye.off()
        return open("dual_cherry.html")
    @cherrypy.expose
    def north(self):
        motor_in1.on()
        motor_in2.off()
        motor_in3.on()
        motor_in4.off()
        return open("dual_cherry.html")
    @cherrypy.expose
    def south(self):
        motor_in1.off()
        motor_in2.on()
        motor_in3.off()
        motor_in4.on()
        return open("dual_cherry.html")
    @cherrypy.expose
    def west(self):
        motor_in1.on()
        motor_in2.off()
        motor_in3.off()
        motor_in4.on()
        return open("dual_cherry.html")
    @cherrypy.expose
    def east(self):
        motor_in1.off()
        motor_in2.on()
        motor_in3.on()
        motor_in4.off()
        return open("dual_cherry.html")
    @cherrypy.expose
    def stoptwo(self):
        motor_in1.off()
        motor_in2.off()
        motor_in3.off()
        motor_in4.off()
        return open("dual_cherry.html")
    @cherrypy.expose
    def servoarm(self, degree=0, degree2=0):
        angular_servo.angle = int(degree)
        angular_servo2.angle = int(degree2)
        return open("dual_cherry.html")
    @cherrypy.expose
    def motorpwm(self, speed=0, speed2=0):
        en_1.value = int(speed) / 10
        en_2.value = int(speed2) / 10
        return open("dual_cherry.html")

if __name__ == '__main__':
    # log everything into the app.log file
    logging.basicConfig(filename="app.log", level=logging.DEBUG)
    cherrypy.quickstart(DualRobot())



