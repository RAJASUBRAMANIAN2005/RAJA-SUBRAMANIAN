                            
Introduction


This project presents a low-cost, dual-mode drone prototype capable of operating in both 
manual and autonomous modes without relying on GPS. It addresses the challenges of highcost drone systems and limited navigation in GPS-denied environments by integrating AIbased object detection, sensor-based obstacle avoidance, and real-time wireless control. A 
camera module captures visual data for environmental awareness, the ESP32 enables 
wireless communication and live video streaming, and the Arduino Uno handles motor 
control. In manual mode, users can operate the drone via a web-based interface hosted on the 
ESP32. In autonomous mode, the system processes visual and sensor data to navigate safely. 
The design focuses on affordability, modularity, and adaptability, offering a practical and 
scalable solution for intelligent aerial systems and research in autonomous navigation.


Background of the Existing Product/Process


Autonomous drones are revolutionizing aerial navigation across various domains 
including surveillance, environmental monitoring, and disaster response. However, most 
commercially available autonomous drone systems depend on expensive components such as 
LiDAR, GPS, and high-performance processors, making them impractical for educational, 
research, or low-budget applications. At the same time, conventional remote-controlled drones 
lack the intelligence and autonomy required for dynamic environments.
To address this gap, the proposed project reverse-engineers the core functionalities of 
intelligent drones using affordable, readily available components. Instead of relying on GPS 
or LiDAR, the system utilizes a standard camera for visual perception, supported by real-time 
object detection and ultrasonic sensors for obstacle avoidance. Wireless communication 
between the AI processing unit and the flight controller is enabled via an ESP32 module, 
allowing responsive and remote interaction. By reducing hardware complexity and cost, this 
solution provides an accessible platform for experimentation, learning, and small-scale 
autonomous drone development.



Problem Statement

Current autonomous drone systems are often too expensive or technologically complex 
for educational use, hobbyist projects, and small-scale applications. While low-cost remotecontrolled drones exist, they lack intelligent features such as real-time decision-making, 
obstacle avoidance, and autonomous navigation. Additionally, most commercial systems rely 
heavily on GPS or LiDAR, limiting their accessibility and performance in indoor or GPSdenied environments. Therefore, the challenge is to design a simplified, cost-effective drone 
system that integrates real-time object detection, sensor-based obstacle avoidance, wireless 
motor control, and a user-friendly interface—all without relying on GPS or expensive 
components.



Objective of the Project

o To develop a cost-effective autonomous drone prototype that operates in both 
manual and autonomous modes.
o To implement real-time obstacle detection and environmental awareness using a 
standard camera and AI-based object detection.
o To establish wireless command communication between the AI processing unit and 
flight control system using the ESP32 module.
o To design a web-based control interface hosted on the ESP32 for live video feed, 
flight mode switching, and manual navigation.
o To ensure a modular and scalable architecture that allows future enhancements such 
as advanced sensors or improved control algorithms.





Selection of Existing Product/System

For the reverse engineering study, commercially available remote-controlled (RC) 
drones and basic autonomous aerial systems were analyzed. These systems commonly 
include a multi-rotor frame, brushless motors, electronic speed controllers (ESCs), flight 
controllers, and in more advanced models, GPS, LiDAR, or high-end processors for 
navigation and obstacle avoidance. The objective was to understand how these 
components coordinate to enable manual control and limited autonomous functionality, 
and how such features could be replicated using affordable alternatives—such as Arduino 
Uno, ESP32, ultrasonic sensors, and camera modules—to develop a cost-effective, GPSindependent drone system



Engineering and Material Study

1. Mechanical Design

o The drone uses a lightweight yet sturdy frame built from carbon fiber or ABS plastic 
to maintain airworthiness while ensuring structural integrity.
o The modular structure allows secure and flexible mounting of cameras, sensors, ESCs, 
and motor assemblies.
The compact quadcopter layout is ideal for maneuverability in both indoor testing and 
outdoor operation


2.Motors

o Brushless DC (BLDC) motors are used for propulsion, offering high speed, efficiency, 
and torque—critical for stable flight.
o Electronic Speed Controllers (ESCs) regulate motor RPMs based on Arduino or flight 
controller signals.
o Balanced propellers reduce vibration and increase flight efficiency


3.Controllers

o Arduino Uno handles real-time control of motors, sensor integration, and stability 
control.
o ESP32 is used for wireless communication, hosting the GUI, and processing 
commands from the ground station or remote device.
o Together, they enable coordination between manual and autonomous flight modes


4.Communication Modules

o The onboard ESP32 module provides built-in Wi-Fi and Bluetooth, eliminating the 
need for external RF modules.
o It allows real-time wireless telemetry and command exchange between the drone and 
the user’s device via a browser-based GUI.
o Ensures seamless mode-switching and data monitoring during flight.



5.Power Supply

o The drone is powered by a 3-cell (11.1V) LiPo battery, which delivers high current 
suitable for BLDC motors and onboard electronics.
o Voltage regulators (e.g., UBECs or 7805 ICs) are used to safely step down voltage for 
microcontrollers and sensors.
These materials and engineering choices informed the component selection for the 
proposed model to ensure durability, affordability, and efficiency.


