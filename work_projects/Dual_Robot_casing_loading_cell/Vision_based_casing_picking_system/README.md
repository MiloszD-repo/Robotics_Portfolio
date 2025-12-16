## Picking System – Detailed Description

After achieving consistent results with the smoothing/preparation system, development of the picking system began. The goal of this subsystem was to reliably grasp the prepared casings using the UR5e robot and the detection information provided by the HALCON vision program. I was responsible for the complete mechanical, electrical, and robotic integration required to turn the detection output into a stable, repeatable picking process.

### Robot Placement & Cell Layout
The first step was determining the optimal placement of the UR5e within the workstation. The robot needed to remain out of the smoothing robot’s workspace while still being able to reach all prepared casings. I evaluated multiple cell configurations and chose a location that balanced reachability, safety, and overall workflow efficiency.

### Pneumatic System & Gripper Integration
Since the UR5e does not include internal pneumatic control, I designed and assembled an external pneumatic system for the picking gripper. This included:

- Valve selection and installation  
- Air pressure regulation and routing  
- Electrical connections for actuation  
- Creating open/close control logic for the UR program  

I then programmed the corresponding gripper control commands on the robot to support precise, fast, and reliable actuation during picking.

### Initial Picking Tests & Motion Development
Before integrating vision detection, I tested the picking workflow manually using basic robot movements. These early tests allowed me to:

- Determine the optimal gripping orientation  
- Find appropriate approach, pick, and retreat positions  
- Measure safe distances for collision avoidance  
- Establish timing requirements  

From these tests, I gathered the parameters needed to build the initial automated picking sequence.

### Vision System Calibration & Integration
To connect detection with robotic motion, the spatial relationship between the camera and the robot needed to be calibrated. Working with the specialist from the Danish Technological Institute, I performed:

- Vision-to-robot coordinate calibration  
- Camera alignment 
- Workspace preparation to improve detection accuracy  

I then studied the detection program’s outputs in detail to understand the structure of the coordinates, detection types, and filtering logic. This understanding allowed me to fully integrate the detection results into the robot’s motion pipeline.

### Communication Architecture
I established **Ethernet-based communication** between the vision computer and the UR5e. This required:

- Structuring message formats  
- Building a protocol for sending pick coordinates  
- Handling cases where no object was detected  
- Ensuring synchronization between detection and robot execution  

This communication layer was essential for enabling autonomous picking based on live detection data.

### Robot Programming & Integration with Detection
I developed a modified version of the robot program that could:

- Trigger the detection process from the UR5e  
- Receive and parse pick point coordinates  
- Determine whether casings were detected or if the robot should wait  
- Execute safe and efficient picking motions based on detection results  

I then ran iterative testing to refine robot behavior, improve cycle time, and enhance robustness. During this phase, I provided feedback to improve the detection algorithm, especially regarding edge cases and borderline detections.

### Full Workflow Integration & Iteration
Once both the smoothing and picking systems were functional independently, I integrated them into a complete automated workflow. This required balancing timing, robot motion planning, and the sequencing of all actions.

As testing progressed, a limitation in the detection algorithm became clear: with larger numbers of casings, the system occasionally produced unfavorable picking points. This resulted in unsuccessful picks or displaced casings.

To address this issue, I introduced a new system-level feature:

- **Automatic recovery for unfavorable detections**, allowing the robot to handle errors gracefully  
- Integration with the updated smoothing system to reprepare displaced casings  
- Adjustments to robot behavior based on detection confidence and casing orientation  

These improvements significantly enhanced overall system reliability and allowed the picking robot to work effectively even under challenging detection conditions.

