# Waste Sorting & Casing Length Detection Subsystem

After cutting operations following slit or uneven-end detection, it was necessary to determine whether the remaining cut-off casing section constituted **trimming waste** or was still **usable material** that should re-enter the processing flow.

This subsystem was developed to automatically measure the effective length of cut casing sections and sort them accordingly, ensuring minimal material waste while maintaining full compliance with production standards.

---

## My Role

I was fully responsible for the development of this subsystem, including concept generation, mechanical and electrical modifications, sensor integration, robot programming, iterative testing, and final validation.

My responsibilities included:

- Developing a non-vision-based length detection method  
- Modifying the gripper and station to support conductivity-based sensing  
- Programming robot motion and sorting logic  
- Resolving mechanical handling issues discovered during testing  
- Refining the final design in the full 3D concept model  

---

## Problem Definition

Following cutting operations, especially slit cutting, the remaining casing length could fall into two categories:

- **Below minimum acceptable length** → trimming waste  
- **At or above minimum acceptable length** → reusable casing  

The system required a reliable, repeatable, and scalable way to automatically distinguish between these two cases and route the material accordingly.

---

## Detection Concept

Given the successful use of conductivity-based sensing in previous subsystems, I decided to reuse this principle for length detection.

### Core Idea
- Use electrical conductivity to determine whether the remaining casing section exceeds the minimum acceptable length  
- Base the decision on whether a conductive path is established between the gripper and a fixed reference surface  

---

## Mechanical & Electrical Modifications

To enable this detection method, several system modifications were required:

### Gripper Adaptation
- Modified the gripper to allow electrical conductivity through the casing  
- Ensured reliable contact without damaging the material  

### Station Modification
- Added a **steel reference plate** connected to the conductivity sensor  
- Positioned the plate to correspond to the minimum acceptable casing length  

When the casing length was sufficient, a conductive signal was generated; shorter lengths produced no signal.

---

## Robotic Logic & Sorting

I implemented robot logic such that:

- The robot moved the casing into a defined measurement position  
- Conductivity feedback determined the casing length category  
- Based on the result:
  - **Usable casing** was routed back into the processing flow  
  - **Trimming waste** was directed to a discard path  

This logic was fully integrated into the robot’s motion sequence.

---

## Handling Challenges & Refinements

During testing, two additional challenges were identified and resolved:

### Long Casing Entanglement
- Longer leftover casings occasionally became tangled on the guiding hook  
- I redesigned the hook to include a **pneumatically actuated latch**, which opened at the correct moment to prevent entanglement  

### Gripper Release Reliability
- Due to the rough and porous casing surface, some casings remained stuck in the gripper after opening  
- I added a **water-spray-based release mechanism** to reliably detach the casing from the gripper  

Both solutions were validated through repeated testing.

---

## Testing & Results

After iterative refinement of mechanics and robot logic, the subsystem achieved:

- **100% accurate length-based sorting**  
- Reliable release and handling across casing lengths  
- Stable operation without tangling or misclassification  

---

## System Integration & Finalization

Once all key assumptions were validated—including:

- Sensor and reference plate placement  
- Gripper conductivity design  
- Hook and release mechanisms  
- Sorting logic and robot sequencing  

The subsystem was refined and incorporated into the final 3D concept model.

---

## Outcome

The Waste Sorting & Casing Length Detection subsystem completed the full preprocessing pipeline by enabling:

- Automatic distinction between usable material and trimming waste  
- Minimal material loss  
- Fully autonomous operation  

Together with the previously developed subsystems, this validated that **all commissioned preprocessing functions were fully achievable and automatable**.  
Each subsystem was designed to operate independently or in combination, enabling scalable, high-throughput solutions—such as proposed cells capable of processing **multiple casings simultaneously**—and providing deep insight into robotic handling of natural casings prior to sorting.
