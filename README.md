# Lost & Found Touchscreen System

*Python-based locker management demo for Raspberry Pi with 7" touch display*

## Overview

A functional touchscreen demo application for secure item reporting, featuring:

- Role-based Tkinter GUI (lost/found item interfaces)  
- Physical locker control via servo motors  
- SQLite database for access code storage  

**Hardware Requirements**:

- Raspberry Pi 4  
- 7" Capacitive Touch Display  
- SG90 Micro Servos (lock/push mechanisms)  

## Installation

```bash
# Install dependencies
sudo apt-get install python3-tk
pip install RPi.GPIO

# Clone repository
git clone https://github.com/yourusername/lost-and-found.git
cd lost-and-found
