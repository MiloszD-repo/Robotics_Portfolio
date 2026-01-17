# Slit Detection Subsystem

Slits are long cuts(holes) in natural casings that are unacceptable to customers and pose a serious operational risk.  
Beyond product quality issues, slits can cause casings to become tangled inside the sorting machine, leading to downtime, material loss, and potential damage to the equipment.

This subsystem was developed to reliably detect slit defects early in the process and prevent defective casings from entering downstream machinery.

---

## My Role

I was fully responsible for the development of the Slit Detection subsystem, including concept generation, mechanical modification of existing equipment, PLC programming, sensor integration, extensive testing, and final validation.

My responsibilities included:

- Analyzing casing behavior during spooling 
- Developing and evaluating multiple detection concepts  
- Modifying an existing automated sorting machine to support the new process  
- Integrating and wiring conductivity-based sensors  
- Programming PLC logic, servo motion, and pneumatic control  
- Debugging false detections and edge-case failure modes  
- Redesigning the detection principle when initial concepts proved insufficient  
- Integrating the validated solution into the full 3D system model  

---

## Problem Definition

Slits present several challenges:

- They may not be visually apparent during processing   
- Undetected slits can cause the casing to leave the mandrel and become tangled inside the sorting machine  
- The detection method must be robust, repeatable and not damage the casings

Vision-based detection was intentionally avoided due to environmental constraints and reliability concerns.

---

## Initial Detection Concept

The initial detection approach leveraged the **process of automated spooling onto a mandrel**, combined with a **conductivity-based contact sensor**, similar to the one used for uneven end detection.

### Core Idea
- Guide the casing during spooling so that any slit would cause the casing to slip off the mandrel  
- Trigger a conductivity sensor when this displacement occurred  

---

## Prototype Implementation

To validate this idea, I built a prototype using the company’s existing automated sorting machine, which already featured a spooling system.

### System Modifications
- Added custom routing points to guide the casing  
- Mounted the conductivity-based sensor in the required detection position  
- Integrated the sensor into the machine’s control system  

### Control System Development
- Reprogrammed the machine’s PLC logic using **Siemens TIA Portal V16**  
- Implemented:
  - Servo motor control for spooling motion  
  - Pneumatic piston sequencing  
  - Sensor-based detection logic  

---

## Testing & Iteration

Extensive testing was conducted with various:

- Sensor positions  
- Spooling speeds  
- Casing conditions  

After tuning timing parameters and sensor placement, the system initially achieved reliable detection with no false positives.

---

## Failure Mode Discovery

During further testing, an unexpected casing behavior was discovered:

- Casings curled on to one side during spooling in a way that caused **all slits on the other side to go undetected**
- Even large slits could bypass the detection system entirely

This represented a critical failure mode that could not be resolved by:
- Adding additional sensors  
- Repositioning sensors  
- Refining detection logic  

---

## Revised Detection Approach

To address this limitation, I developed a new detection principle using an **existing water-pumping feature** of the machine.

### New Detection Logic
- Casings are filled with water during spooling 
- Any slit or hole causes water leakage  
- Detection is based on **contact duration**, corresponding to:
  - The amount of leaked water  
  - The size of the slit  

By shifting detection from displacement-based logic to **leak-duration analysis**, the system became independent of casing orientation or curling behavior.

---

## Validation & Optimization

Through iterative testing, I determined the optimal leakage duration threshold that:

- Detected all problematic slits  
- Avoided false positives  
- Maintained production efficiency  

The final system achieved:

- **100% detection accuracy** across tested cases  
- Robust performance under real operating conditions  

---

## Cost Optimization & System Integration in the 3D Concept Model

To reduce system cost and complexity, I further refined the design by:

- Using a **single conductivity-based sensor** per station for both:
  - Uneven end detection  
  - Slit detection  
- Mechanically linking contact surfaces while maintaining different detection zones  
- Extending the planned logic to differentiate detection states based on machine context  

This required additional complexity in the overall machine logic and state management but significantly reduced hardware cost.

---

## Outcome

The Slit Detection subsystem delivered:

- Reliable, vision-free slit detection  
- Full protection of downstream sorting machinery  
- Zero false positives after refinement  
- A cost-efficient and scalable solution  

All concept development, mechanical adaptation, PLC programming, sensor integration, testing, validation, and system integration were performed by me.
