# Mascara Packaging Machine – PLC Control System Upgrade  

## Project Overview

This freelance project involved modernizing the control system of a semi-automated mascara packaging machine.  
The machine was originally controlled using electrical relay logic, which limited flexibility, diagnosability, and scalability.

My task was to redesign and implement the machine control logic as a PLC-based solution using Function Block Diagram (FBD) programming on an SR-12MTDC controller in SuperCAD.

---

## Scope of Work

The machine operated using pneumatic pistons activated in a strict sequence, with feedback provided by limit switches.  
The new control system needed to ensure accurate sequencing and safe operation.

---

## Control Logic Design

### Pneumatic Sequence Control
- Implemented deterministic piston activation and retraction logic  
- Interlocked movements based on limit switch feedback  

### Safety Mechanisms
- Prevented unsafe restarts if the machine was stopped mid-cycle  
- Added logic to block conflicting piston commands  

### Counting & Monitoring
- Integrated a cycle counter 

---

## Tools & Technologies

- **PLC**: SR-12MTDC  
- **Programming**: Function Block Diagram (FBD)  
- **Software**: SuperCAD  
- **Actuation**: Pneumatic pistons  
- **Sensors**: Magnetic limit switches  

---

## Outcome

- Successfully replaced relay-based control logic with a PLC solution  
- Improved reliability and clarity of the machine control system  
- Increased operational safety during interruptions and restarts  
- Enabled easier future modifications and troubleshooting  

This project demonstrates hands-on experience with industrial automation, pneumatic sequencing, and safety-oriented PLC programming in a real production environment.
