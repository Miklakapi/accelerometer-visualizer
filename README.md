# Raspberry_LED_Cube

![license](https://img.shields.io/badge/license-MIT-blue)
![linux](https://img.shields.io/badge/os-Linux-green)
![language](https://img.shields.io/badge/language-Python3.9-blue)
![version](https://img.shields.io/badge/version-1.0.0-success)
![status](https://img.shields.io/badge/status-production-green)

A program that uses an accelerometer and a Raspberry Pi to visualize the movements of the device on the website. 

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)

## General info
A Python program that manages the MPU-6050 accelerometer and its data. Via the web application on flask, it sends data to the website
and converts them into a living 3D model that shows the movements of the device.

## Technologies
Project is created with:

* Python 3.9
* Flask
* Package to manage GPIO `RPi.GPIO`
* Tree.js

## Setup
To run this project, run:
```python3 /src/app.py```

## Features
* Moving 3D model on the website
* Managing the read data to reduce measurement errors
* LoopRate system that reduces the loop speed to reduce unnecessary load on the device

## Status
The project's development has been completed.
