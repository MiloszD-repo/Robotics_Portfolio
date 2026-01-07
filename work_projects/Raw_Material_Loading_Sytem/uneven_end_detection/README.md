# Uneven End Detection Subsystem

The goal of this subsystem was to reliably detect **unevenly cut casing ends** during raw material processing. In the semi-automatic and manual workflows used previously, casings were often cut at irregular angles, and specific quality standards required these deviations to be identified and corrected before further processing. Because casings vary in diameter and behave unpredictably when placed on mandrels, the detection method had to be robust, waste-minimizing, and independent of vision systems.

---

## Problem Analysis

To understand the problem in depth, I first experimented with real casings and deliberately created uneven ends to study their behavior on mandrels. This hands-on exploration revealed several constraints:

- **Vision-based detection was not viable** due to:  
  - significant splashing water during operation  
  - highly reflective mandrel surfaces  
  - the possibility that an uneven end could wind tightly and become fully hidden from view  

- The method needed to:  
  - work across a range of casing diameters  
  - produce minimal material waste  
  - remain mechanically simple and reliable  
  - operate repeatably in a wet, dynamic environment  

These constraints motivated the search for an alternative physical method of detecting end irregularities.

---

## Concept Development

After evaluating various ideas, one promising approach emerged:  
**using targeted water jets to briefly unwind the casing, expose the dangling uneven end, and detect it using a contact sensor.**

This method showed potential during manual trials, where the water jet consistently produced a detectable movement pattern in casings with uneven ends.

---

## Prototype System Development

To validate the concept under controlled, repeatable conditions, I designed and built a full robotic prototype of the detection station:

### **Mechanical & Robotic Setup**
- Developed a custom gripper for the KUKA robot with an integrated **electric valve–controlled water jet system** to trigger the unwinding action.  
- Used the company’s custom **conductivity-based sensor** to detect the presence of an exposed uneven end.

### **Sensor & Actuator Integration**
- Tested multiple sensor placements across casing diameters to ensure universal detection.  
- Determined optimal water-jet angle, intensity, and timing to reliably expose the end with minimal waste.  
- Tuned robot motion paths and timing for consistent detection cycles.

---

## Testing & Parameter Optimization

Using the robotic prototype, I performed extensive testing to:

- identify the best sensor positioning for all common casing diameters  
- determine the exact parameters required for repeatable unwinding  
- measure detection accuracy and false-positive/negative rates 

The final configuration achieved **100% detection accuracy**, fully validating the method.

---

## Outcome & Documentation

With the concept proven, I:

- prepared a detailed technical report  
- documented sensor placement, timing parameters, and robot routines  
- created visual materials describing the detection system architecture  
- integrated the subsystem into the larger machine concept  


