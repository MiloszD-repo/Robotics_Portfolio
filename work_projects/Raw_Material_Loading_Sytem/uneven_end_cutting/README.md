# Uneven End Cutting Subsystem

With a reliable method for detecting uneven casing ends established, the next challenge was to remove the defective sections cleanly, consistently, and with minimal waste. Natural casings are soft, elastic, and highly deformable, and production standards require that after cutting, the difference between the longest and shortest edge must not exceed **1 cm**. Achieving a precise, low-waste cut on such material required both mechanical innovation and carefully controlled robotic motion.

---

## My Role

I was responsible for the **complete development** of this subsystem—from analyzing the physical behavior of casings and defining cutting requirements, to designing and fabricating the integrated gripper-cutter, programming the robot sequence, performing iterative testing, and validating the final solution.  
This included:

- manual experimentation to understand cutting mechanics  
- generation and evaluation of mechanical concepts  
- full mechanical design and manufacturing drawings  
- building the integrated gripping, tensioning, and cutting robotic end effector  
- programming and refining the entire robot workflow  
- optimizing trimming length to minimize waste  
- validating the subsystem with extensive prototype testing
- overall robotic cell design  

---

## Problem Analysis

To understand how to produce a compliant cut, I performed manual cutting tests on casings mounted on mandrels. Through these experiments, several key insights emerged:

- **Tension is critical**—without proper tension, the casing stretches unevenly or tears during cutting  
- A clean, straight cut is only possible under **controlled and constant tension**  
- Cutting too far forward wastes valuable material; cutting too close does not eliminate the uneven end  
- The system must accommodate various casing diameters while maintaining cut quality  
- Minimizing trimming waste is essential for maintaining product yield  

These findings guided the design of the automated cutting approach.

---

## Concept Development

Based on the manual insights, the automated cutting method needed to:

1. Expose the uneven end via the water-spray detection technique  
2. Grip the casing securely without damaging it  
3. Apply precise tension to stabilize the material  
4. Execute a controlled cutting motion  
5. Produce clean geometry across all casing diameters  

I ultimately designed a **single integrated gripper** that performed all stages: spraying, detecting, gripping, tensioning, and cutting.

---

## Mechanical Design & Fabrication

I designed and built the full cutting-enabled gripper for the KUKA robot, including:

### **Integrated Gripper + Cutting Mechanism**
- Custom 3D-printed components for contact surfaces  
- Recycled elements from an older gripper for structural strength  
- Small pneumatic pistons for actuation 
- Pneumatic piston operated razor-blade cutting knife
- An adjustable mounting system to fine-tune:
  - knife-to-grip distance    
  - trimming length (to minimize waste)

Before fabrication, I created detailed technical drawings defining dimensions.

---

## Robotic Workflow & Programming

I implemented a multi-stage robotic routine involving:

1. Water spraying to unwind the casing  
2. Sensor-based uneven-end confirmation  
3. Gripping  
4. Precise tensioning  
5. Cutting using the integrated knife  
6. Reset and preparation for the next cycle

Each stage was individually tuned to minimize trimming waste while achieving consistent, standard-compliant cuts.

---

## Testing & Results

After iterative refinement of mechanics and robot sequencing, the system achieved:

- **Near-100% cutting accuracy**  
- **Cuts within the ≤1 cm deviation standard**  
- **Minimal trimming waste** due to optimized knife offset 
- Reliable performance across all tested casing diameters  
- Successful operation in a fully automated mockup station  

The validated design was then incorporated into the larger 3D system model.
# Uneven End Cutting Subsystem

With a reliable method for detecting uneven casing ends established, the next challenge was to remove the defective sections cleanly, consistently, and with minimal waste. Natural casings are soft, elastic, and highly deformable, and production standards require that after cutting, the difference between the longest and shortest edge must not exceed **1 cm**. Achieving a precise, low-waste cut on such material required both mechanical innovation and carefully controlled robotic motion.

---

## My Role

I was responsible for the **complete development** of this subsystem—from analyzing the physical behavior of casings and defining cutting requirements, to designing and fabricating the integrated gripper-cutter, programming the robot sequence, performing iterative testing, and validating the final solution.  
This included:

- manual experimentation to understand cutting mechanics  
- generation and evaluation of mechanical concepts  
- full mechanical design and manufacturing drawings  
- building the integrated gripping, tensioning, and cutting robotic end effector  
- programming and refining the entire robot workflow  
- optimizing trimming length to minimize waste  
- validating the subsystem with extensive prototype testing
- overall robotic cell design  

---

## Problem Analysis

To understand how to produce a compliant cut, I performed manual cutting tests on casings mounted on mandrels. Through these experiments, several key insights emerged:

- **Tension is critical**—without proper tension, the casing stretches unevenly or tears during cutting  
- A clean, straight cut is only possible under **controlled and constant tension**  
- Cutting too far forward wastes valuable material; cutting too close does not eliminate the uneven end  
- The system must accommodate various casing diameters while maintaining cut quality  
- Minimizing trimming waste is essential for maintaining product yield  

These findings guided the design of the automated cutting approach.

---

## Concept Development

Based on the manual insights, the automated cutting method needed to:

1. Expose the uneven end via the water-spray detection technique  
2. Grip the casing securely without damaging it  
3. Apply precise tension to stabilize the material  
4. Execute a controlled cutting motion  
5. Produce clean geometry across all casing diameters  

I ultimately designed a **single integrated gripper** that performed all stages: spraying, detecting, gripping, tensioning, and cutting.

---

## Mechanical Design & Fabrication

I designed and built the full cutting-enabled gripper for the KUKA robot, including:

### **Integrated Gripper + Cutting Mechanism**
- Custom 3D-printed components for contact surfaces  
- Recycled elements from an older gripper for structural strength  
- Small pneumatic pistons for actuation 
- Pneumatic piston operated razor-blade cutting knife
- An adjustable mounting system to fine-tune:
  - knife-to-grip distance    
  - trimming length (to minimize waste)

Before fabrication, I created detailed technical drawings defining dimensions.

---

## Robotic Workflow & Programming

I implemented a multi-stage robotic routine involving:

1. Water spraying to unwind the casing  
2. Sensor-based uneven-end confirmation  
3. Gripping  
4. Precise tensioning  
5. Cutting using the integrated knife  
6. Reset and preparation for the next cycle

Each stage was individually tuned to minimize trimming waste while achieving consistent, standard-compliant cuts.

---

## Testing & Results

After iterative refinement of mechanics and robot sequencing, the system achieved:

- **Near-100% cutting accuracy**  
- **Cuts within the ≤1 cm deviation standard**  
- **Minimal trimming waste** due to optimized knife offset 
- Reliable performance across all tested casing diameters  
- Successful operation in a fully automated mockup station  

The validated design was then incorporated into the larger 3D system model.

Visual documentation showing casings **before cutting** and **after uneven-end removal** is included in the folder.
---

## Outcome

The Uneven End Cutting subsystem delivered:

- Clean, repeatable, and precise cuts on highly deformable material  
- Minimal material waste and high efficiency  
- A simplified workflow through full integration of cutting into the gripper   

All mechanical design, fabrication, robot programming, integration, testing, and validation for this subsystem were completed by me.

---

## Outcome

The Uneven End Cutting subsystem delivered:

- Clean, repeatable, and precise cuts on highly deformable material  
- Minimal material waste and high efficiency  
- A simplified workflow through full integration of cutting into the gripper   

All mechanical design, fabrication, robot programming, integration, testing, and validation for this subsystem were completed by me.
