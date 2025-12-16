# Project Overview

This project was carried out in collaboration with the Danish Technological Institute as part of the Innobooster program funded by the Danish Innovation Fund. The development focused on automating the preparation and handling of casings and consisted of two main components:

1. Casing detection  
2. Casing handling — divided into:
   - Preparation for detection
   - Picking after detection

To demonstrate the proof of concept, two high-level system prototypes were developed and integrated into a complete automated workflow.

---

## System Architecture

- **Preparation Stage:**  
  Handled by a KUKA KR 6 R900-2 equipped with a custom-designed gripper.

- **Picking Stage:**  
  Performed by a Universal Robots UR5e based on detection results.

- **Vision & Cell Design:**  
  A fully custom robotic cell was designed and manufactured, integrating a HALCON vision system, structural components, and safety features.

The integrated prototype enabled automated handling of up to 20 casings simultaneously, replacing a manual process where operators had to mount casings onto hooks one by one. In the new workflow, the operator simply placed bundled casings loosely on the table.

---

## Performance

The proof-of-concept system achieved:

- ~90% picking accuracy with one smoothing operation  
- ~95% picking accuracy with two smoothing operations  
- ~99% picking accuracy with three smoothing operations  

The system supported automatic error detection and recovery, allowing additional smoothing cycles when a casing was improperly positioned or unsuccessfully picked. Remaining inaccuracies primarily stemmed from limitations in the external vision system, especially as the number of casings increased and less favorable picking poses were generated.

---

## Iteration & Improvements

Several shortcomings observed in early prototypes were addressed through:

- Redesign of the smoothing gripper to include an additional feature that allowed it to retrieve casings that were displaced or dropped during the picking process, enabling them to be reintroduced into the smoothing area for another preparation cycle.
- Multiple hardware and software iterations to improve system robustness, accuracy, and repeatability.
- Identification of key improvements for the final product version, including:
  - Increasing the effective picking area
  - Adjusting robot reach and overall cell layout

---

## Outcome

The project demonstrated a highly automated and reliable workflow for casing handling with excellent performance and a clear path toward achieving near-100% completion rates in the full-scale product. The development involved extensive prototyping, system integration, and iterative testing across both mechanical and software domains.
