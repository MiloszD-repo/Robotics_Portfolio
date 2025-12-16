# Project Overview

This project was carried out in collaboration with the Danish Technological Institute as part of the Innobooster program funded by the Danish Innovation Fund. The objective was to develop an automated system for preparing and handling casings, replacing a manual and labor-intensive workflow. The system consisted of two main components:

1. Casing detection  
2. Casing handling — divided into:
   - Preparation for detection
   - Automated picking after detection

Two integrated high-level system prototypes were developed to demonstrate the full proof of concept.

# My Role:
- I was responsible for the complete **mechanical, electrical, software and robotic development** of the system, including concept design, cell layout, hardware integration, robot programming, custom tooling, component manufacturing, safety considerations, and full system orchestration.  
-The Danish Technological Institute developed the HALCON vision program, but I led the majority of the integration process, communication setup with the UR5e, and ensured end-to-end compatibility between detection and robotic actions.

---

## System Architecture

- **Preparation Stage:**  
  Handled by a KUKA KR 6 R900-2 robot equipped with a custom-designed gripper.

- **Picking Stage:**  
  Performed by a Universal Robots UR5e based on detection results.

- **Vision & Cell Design:**  
  A fully custom robotic cell was designed and built, incorporating a HALCON-based vision system, safety elements, and all required mechanical structures.

I designed and implemented the cell, developed the grippers, programmed the robots, wired and integrated all hardware, and connected the full workflow. The final system enabled automated handling of up to **20 casings simultaneously**, reducing operator involvement to simply placing loosely bundled casings on the table rather than mounting each one individually.

---

## Performance

The integrated prototype delivered strong and repeatable results:

- ~90% picking accuracy with one smoothing operation  
- ~95% accuracy with two smoothing operations  
- ~99% accuracy with three smoothing operations  

The workflow featured **automatic error detection and recovery**, allowing the system to trigger additional smoothing attempts when casings were misaligned or dropped. Remaining inaccuracies were primarily due to limitations in the external vision system, especially when handling larger batches that created less favorable picking poses.

---

## Iteration & Improvements

Throughout development, I carried out multiple design iterations across mechanical, electrical, and software domains:

- **Redesigned the smoothing gripper** to include a feature that allowed the system to recover casings that were displaced or dropped during the picking process and reintroduce them into the smoothing area for another attempt.
- Conducted several hardware and software refinements to improve robustness, accuracy, and cycle consistency.
- Identified key improvements for future product implementation, including:
  - Expanding the effective picking area  
  - Optimizing robot placement and reach  

---

## Outcome

The project demonstrated a highly automated and reliable casing-handling workflow with a clear path toward achieving **near-100% completion rates** in a commercial version.  

By taking ownership of the **entire mechanical, electrical, and robotics engineering scope**, I was able to deliver a fully integrated prototype system — from concept, tooling design, and automation strategy to robot programming, communication architecture, and validation testing.  
This project reflects my ability to independently design, build, integrate, and optimize complex robotic workflows.

## Key Responsibilities

- Led the complete **mechanical, electrical, and robotics development** of the system.
- Designed and built the full robotic cell, including grippers, fixtures, and safety features.
- Programmed and integrated both robots (KUKA KR 6 R900-2 and UR5e) into a unified workflow.
- Established communication between the HALCON vision system and the UR5e robot.
- Developed system logic for automated smoothing, error handling, and recovery cycles.
- Conducted iterative testing, troubleshooting, and performance optimization.
- Managed prototype integration from concept to validated proof-of-concept.
