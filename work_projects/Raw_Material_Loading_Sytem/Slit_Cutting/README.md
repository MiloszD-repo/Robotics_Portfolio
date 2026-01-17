# Slit Cutting Subsystem

Following the successful implementation of the Slit Detection subsystem, the next step was to remove the detected defective sections in a controlled, repeatable, and waste-minimized manner.

This subsystem extends the previously developed cutting solution used for uneven end removal, adapting it to accurately cut slits based on detected defect positions.

---

## My Role

I was responsible for adapting the existing cutting hardware and robotic logic to support slit removal.  
This included motion planning, robot programming, system integration, testing, and validation.

---

## System Approach

The slit detection process provided a **rough positional estimate** of the detected defect.  
This information was used to guide the robot to the cutting region, where the cutting process was executed using the same integrated gripping and cutting mechanism developed for uneven end cutting.

Key aspects of the approach:

- Reuse of the existing gripper and cutting mechanism  
- Modification of robot paths and sequencing to accommodate slit locations  
- Minimal additional hardware changes  

---

## Robotic Workflow & Programming

The subsystem was implemented by:

- Reprogramming robot motion paths to align with slit positions  
- Adjusting gripping and tensioning logic to stabilize the casing during cutting  
- Refining the sequencing of movements to ensure clean, straight cuts  
- Synchronizing detection signals with cutting execution  

Iterative testing allowed for rapid refinement of motion timing and positioning.

---

## Testing & Results

After multiple test cycles and minor refinements, the subsystem achieved:

- **100% slit removal accuracy**  
- **Clean and repeatable cuts**  
- **Minimal trimming waste**  
- Reliable operation across different casing conditions  

---

## Outcome

The Slit Cutting subsystem delivered an efficient and robust extension of the existing cutting solution, enabling full automation of slit removal without additional mechanical complexity.

All robot programming, motion refinement, testing, and validation for this subsystem were completed by me.

---

### Gripper Design Adaptation for Positional Uncertainty

Because both slit and uneven-end detection provided only approximate defect positions, the final system design needed to tolerate positional uncertainty while maintaining reliable gripping.

To address this, the gripping section of the end effector was **extended in the final 3D concept**, ensuring that the casing could be securely captured even when the detected defect location was not exact. This design choice increased robustness without introducing additional sensing or mechanical complexity and allowed the cutting operation to remain reliable across all tested scenarios.

