## Smoothing System – Detailed Description

The smoothing system was developed to automate what had previously been a fully manual and repetitive preparation process. My goal was to replicate the operator’s manual motion in a reliable, programmable, and repeatable robotic workflow.

### Concept Development & Prototyping
I explored several conceptual approaches before selecting the most robust solution. Early work focused on understanding the operator’s motion patterns and translating them into a mechanism that could be actuated by a robot. After evaluating multiple concepts, I designed a custom gripper that, when combined with the KUKA KR 6 R900-2, could reproduce the manual smoothing movement with consistent force and positioning.

### Mechanical Design & Manufacturing
I designed the gripper from the ground up:

- Created initial sketches and semi-technical drawings on paper to refine the mechanism.
- Produced a detailed CAD model in Autodesk Inventor, including all mounting and functional elements.
- Designed custom gripper fingers, a base plate for robot mounting, and the complete mechanical assembly.
- Integrated small pneumatic pistons to actuate the mechanism.
- Prepared manufacturing drawings and fabricated the gripper using available workshop materials.
- Assembled and validated the first prototype manually before integrating it with the robot.

After initial testing, I improved the gripper’s structural strength by reinforcing critical areas and updating the design to better handle real load conditions.

### Workstation Setup & Robot Programming
In parallel with gripper development:

- I designed and assembled the workstation layout, ensuring proper robot placement for optimal reach and accessibility.
- Implemented pneumatic control directly through the KUKA robot.
- Programmed the complete smoothing sequence on the KUKA teach pendant, including motion planning, timing, safety considerations, and coordination with the rest of the system.

### Testing, Optimization & Performance Tuning
I conducted extensive testing with various quantities and configurations of casings to optimize the smoothing sequence, tune cycle times, and maximize consistency. This iterative process helped refine the smoothing process.

During integrated testing with the picking robot, a key issue emerged: some casings were being displaced or dropped during the picking process. To address this:

- I **redesigned the gripper hardware** to add a feature allowing the system to recover displaced casings.
- I **updated the robot program** to reintroduce the casings into the smoothing area for another preparation cycle.

These improvements significantly increased system reliability and enabled high overall picking accuracy across multiple smoothing cycles.

