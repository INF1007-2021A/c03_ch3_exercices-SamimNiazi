#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    average = (a+b+c)/3
    return average


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_rads = (angle_degs * (math.pi/180)), (angle_mins * (math.pi/(60 * 180))), (angle_secs * (math.pi/(180 *3600)))
    return angle_rads


def to_degrees(angle_rads: float) -> tuple:
    degrees = angle_rads * (180/math.pi)
    minutes = angle_rads * (60*180/math.pi)
    seconds = angle_rads * (3600*180/math.pi)
    return degrees, minutes, seconds


def to_celsius(temperature: float) -> float:
    to_farenheit = (temperature * (1.8)) + 32
    return to_farenheit


def to_farenheit(temperature: float) -> float:
    to_celsius = (temperature - 32)* (5/9)
    return to_celsius


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
