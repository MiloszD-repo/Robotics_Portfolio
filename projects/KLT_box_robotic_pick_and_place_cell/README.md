# Smart Gripper System for Automatic Warehouse Pick & Place  
### University Project – Team of Robotics & Software Engineers  

Video of end result: 
https://youtu.be/a3piznOsmRs

This project focused on improving the reliability and autonomy of pick-and-place operations for Enabled Robotics solutions combining **MiR mobile robots** with **UR collaborative robots**. The existing system depended on physical QR markers for pose estimation, which was unreliable and sensitive to misalignment. Our goal was to develop a **low-cost, markerless alternative** using vision and distance sensing.

The result was a fully functional prototype system capable of detecting, localizing, and picking KLT warehouse boxes with high repeatability, even when the actual box location differed from the expected position by **20–30 cm**.

---

## Objectives
- Replace QR-based pose estimation with a **markerless dual-sensor approach**  
- Enable reliable picking of boxes with varied sizes and misalignment  
- Develop a **smart gripper** equipped with multi-sensor perception  
- Demonstrate end-to-end automation with UR + MiR  
- Build a mock commercial concept, including business model and investor presentation  

---

## System Overview

The system consisted of:
- A **custom smart gripper** for KLT boxes  
- **2D camera** for coarse box localization  
- **Dual ToF sensors** for fine positioning and gap detection  
- A **warehouse management system** (developed by software engineers on the team)  
- UR robot control over Ethernet, programmed in URScript  
- Arduino-based gripper control  
- Complete robotic cell layout and operational workflow

The system estimated box position using:
1. Rough coordinates from the warehouse management system  
2. Coarse 2D visual localization  
3. Fine position refinement using ToF gap scanning  
4. Computation of final pick pose  
5. Autonomous pick via UR robot  

---

## My Role

I served as **team lead** and was responsible for coordinating the project across robotics and software engineers. My individual contributions included:

### **Concept & System Architecture**
- Co-developed the idea for the dual-positioning system combining **2D vision** + **ToF scanning**  
- Defined how ToF sensors should be used to find gaps between boxes and compute refined poses  
- Designed the robotic **cell layout**, ensuring reachability, cycle flow, and system integration  
- Created workflow plans and algorithms for how the UR robot would perform detection and picking  

### **Robotics, Integration & Control**
- Fully responsible for programming and controlling the **UR robot**
- Established Etherenet communication with UR for online programming and automatic control of the robot
- Implemented Serial communication between UR and the Arduino-powered gripper  
- Integrated all subsystems: gripper, sensors, camera, UR control, and WMS  
- Co-developed the vision and detection logic with another robotics engineer  
- Tested, iterated, and refined robot motion and system behavior  

### **Leadership & Coordination**
- Managed task distribution and team workflow  
- Coordinated work between robotics and software engineers  
- Oversaw integration of the WMS, vision module, and hardware components  
- Delivered the final pitch presentation to mock investors  

---

## Mechanical Contribution
A teammate designed the mechanical structure of the gripper, while I focused on:
- Sensor placement  
- Gripper interaction logic  
- Integration with UR robot  
- Control behavior and communication protocol  

---

## Results

- Achieved reliable picking performance on **multiple box sizes**  
- System successfully compensated for **20–30 cm misalignment** between expected and actual box position  
- Achieved high repeatability and accuracy using the dual-sensor approach  
- Developed a **low-cost, markerless** alternative to Enabled Robotics’ QR-based solution  
- Successfully presented a commercial concept with investor-style pitch  
- Received **grade 12 (highest possible)**

---

## Technologies & Tools
- **Universal Robots (URScript, Ethernet communication, Python, Serial Communication)**  
- **Arduino for gripper control**  
- **ToF distance sensing**  
- **2D vision**  
- **Custom gripper integration**  
- **Python for perception logic**  
- **Warehouse management system (WMS)**  
