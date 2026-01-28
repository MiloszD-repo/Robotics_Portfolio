#  Contactless End-of-Casing Detection on Mandrel

This project focused on developing a **reliable, contactless method** for detecting when a natural casing has been fully spooled onto a mandrel. The detection signal was used to stop the machine and trigger the next processing step in a high-speed automated sorting system.

Casings are spooled at speeds of up to **2 m/s** and vary significantly in length, making time-based or fixed-position detection unreliable. The existing solution required physical contact with the casing and lacked precision, motivating the development of a new sensing approach.

---

## My Role

I was responsible for the **full development and validation** of the end-of-casing detection concept, including:

- brainstorming and evaluating multiple sensing principles  
- consulting with management to select viable detection approaches  
- modifying machine motion logic to support testing  
- integrating and testing multiple contactless sensors  
- PLC, Python, and Arduino programming  
- data collection, analysis, and parameter tuning  
- electrical wiring and sensor integration  
- mechanical adaptations and 3D-printed mounts  

---

## Problem Definition

Key constraints of the detection task included:

- High casing speed (~2 m/s)
- Need for fast detection to stop the spooling process (10 ms) 
- Large variation in casing length  
- Wet and reflective environment  
- No physical contact with the casing 
- Reliable detection required to safely stop the machine  

The detection system needed to operate robustly without influencing the spooling process or damaging the product.

---

## Concept Development

After brainstorming multiple ideas and reviewing feasibility with management, I selected two **contactless sensing principles** suitable for the application:

- **Capacitive sensing**
- **mmWave radar sensing**

Both approaches are immune to mechanical wear and do not require physical interaction with the casing.

---

## Implementation & Testing

To support sensor evaluation, I first modified the PLC program of the existing sorting machine to generate the required casing motion.

I then implemented and tested both sensing approaches, including:

- sensor mounting and mechanical integration  
- real-time signal acquisition  
- data logging and analysis  
- tuning detection thresholds and timing  
- validating detection reliability at full operating speed  

Detailed descriptions of each sensing method, including hardware setup and software logic, are provided in the respective subfolders of this project.

---

## Technologies & Tools

- **PLC programming** (industrial sorting machine)  
- **Python** (data analysis, signal evaluation, UART-sensor interface)  
- **Arduino** (sensor interfacing and prototyping)  
- **Contactless sensors** (capacitive, mmWave radar)  
- **3D printing** (sensor mounts and fixtures)  
- **Electrical integration and testing**

---

## Outcome

The project successfully explored and demostrated **contactless end-of-casing detection methods** for high-speed spooling on a mandrel.
