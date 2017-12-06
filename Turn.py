#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 대한 우회전/좌회전 모듈
"""

"""
편의를 위해 R.py 만 import 하면 많은 Method 를 쓸 수 있게 구축하였습니다.

"""
import R
import time
from Run import *


def right() :
    """LightMotor는 전진 RightMotor는 후진하게 하여 right포인트턴을 한다."""
    print ("Right Turn")
    LeftMotor(1)
    RightMotor(0)
    LeftPwm.ChangeDutyCycle(R.speed*0.65)
    RightPwm.ChangeDutyCycle(R.speed*0.65)
    """상황에 따라 사용
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)
    #"""

def left() :
    """LightMotor는 후진 RightMotor는 전진하게 하여 left포인트턴을 한다."""
    print ("Left Turn")
    LeftMotor(0)
    RightMotor(1)
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)
    """상황에 따라 사용
    LeftPwm.ChangeDutyCycle(R.speed*0.7)
    RightPwm.ChangeDutyCycle(R.speed*0.7)
    """

def smallRight() :
    """작은 미세조정을 한다"""
    print ("smallRight")
    LeftMotor(1)
    RightMotor(0)
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)

def smallLeft() :
    """작은 미세조정을 한다"""
    print ("smallLeft")
    LeftMotor(0)
    RightMotor(1)
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)

def rightChk() :
    """오른쪽 가는 것을 체크한다"""
    print "==== RIGHT CHK ====>"

    R.forward()
    time.sleep(0.1)

    while True :
        sensor = R.FiveSensor.get()
        print "Outing",
        print sensor
        if not R.LineSensor.cmpStatus(sensor, R.LineSensor.forwardCase) :
            break
        R.right()
        time.sleep(0.01)

    while True :
        sensor = R.FiveSensor.get()
        print "Ining",
        print sensor
        if R.LineSensor.cmpStatus(sensor, R.LineSensor.forwardCase) :
            break
        R.right()
        time.sleep(0.01)
    print "<==== RIGHT CHK ===="
    # time.sleep(0.1)

def UTurn() :
    """ U-Turn """
    while True :
        sensor = R.FiveSensor.get()
        print "U-Turn",
        print sensor
        if R.LineSensor.cmpStatus(sensor, R.LineSensor.forwardCase) :
            break
        R.right()
        time.sleep(0.01)




















    #
