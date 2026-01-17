from flask import Flask, send_file, jsonify
import socket
import time
import struct
import os
import numpy as np
import pyrealsense2 as rs
from datetime import datetime
from PIL import Image
import threading
import subprocess
import requests
import serial
import rtde_receive
import rtde_control
import pyrealsense2 as rs
import cv2
import numpy as npc


app = Flask(__name__)

IP = "localhost"
port = "33000"
letf=False
right=False
serviceIP = "127.0.0.1"
servicePort = "5000"
depth="100"
depth2 = float(depth)/100
starting_pos=[-0.947, -0.325, 0.612, 0.0, 0.0, 1.621]
positions = [-0.947, 0.099, 1.015, 0.0, 0.0, 1.621]
positions2 = [-0.947, -0.250, 1.015, 0.0, 0.0, 1.621]#UPDATE BEFORE LAUNCH
waypoint=[-0.62,0.1,1.426,0.0,0.0,1.621]
waypoint2=[0.568,-1.292,-1.467,-1.952,-1.576,-2.142]
waypoint3=[0.593, -1.526, -0.789, -2.396, -1.573, -2.143]
waypoint4=[1.290, -1.597, -0.618, -2.496, -1.573, -2.850]
drop_pos=[0.01,0.7,1.369,0.0,0.0,0.0]
drop_pos2=[0.005,0.7,1.02,0.0,0.0,0.0]
drop_pos3=[0.368,0.7,1.02,0.0,0.0,0.0]
shelf_floor = 0.986 #UPDATE BEFORE LAUNCH

def get_closest_blue_box_x(show_image=True, exposure=300, min_area=2000, depth_mm=0.0):
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    pipeline.start(config)

    device = pipeline.get_active_profile().get_device()
    sensor = device.query_sensors()[1]  
    sensor.set_option(rs.option.enable_auto_exposure, 0)  
    sensor.set_option(rs.option.exposure, exposure)       

    try:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            print("Error: Unable to capture color frame.")
            return None

        image = np.asanyarray(color_frame.get_data())
        hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Adjust color ranges to your environment if needed
        lower_blue = np.array([100, 150, 50])
        upper_blue = np.array([140, 255, 255])

        mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        image_center_x = image.shape[1] // 2
        closest_x = None
        min_distance = float("inf")

        for contour in contours:
            if cv2.contourArea(contour) >= min_area:
                M = cv2.moments(contour)
                if M["m00"] > 0:
                    cX = int(M["m10"] / M["m00"])
                    relative_cX = cX - image_center_x
                    distance = relative_cX
                    if distance < min_distance:
                        min_distance = distance
                        closest_x = relative_cX

                    if show_image:
                        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
                        cv2.circle(image, (cX, int(M["m01"] / M["m00"])), 5, (0, 0, 255), -1)

        if closest_x is not None and depth_mm > 0.0:
            focal_length_px = 597.933  # Use your calibrated focal length in pixels
            # Convert pixel offset to mm
            offset_mm = (closest_x * depth_mm) / focal_length_px
            
            # Camera offset: If the camera is 40 mm to the left, adjust accordingly.
            # If you want the movement in mm:
            movement_mm = offset_mm - 40.0
            print(f"Offset from camera center: {offset_mm} mm")
            print(f"Offset from gripper center: {movement_mm} mm")

            # Convert to meters if your robot API expects meters:
            movement_m = movement_mm / 1000.0
            print(f"Movement from gripper center (m): {movement_m}")
        else:
            print("No valid blue box detected or depth not provided.")

        if show_image:
            cv2.imshow("Blue Box Detection", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return movement_m
    finally:
        pipeline.stop()

        
class URRobot:
    def __init__(self):
        self.robot_ip = "192.168.12.40"
        self.port = 30003
        self.socket = None
        self.rtde_c = None
        self.rtde_r = None
        self.position_tolerance = 0.0005  # 1mm tolerance
        
        
    def connect(self):
        try:
            # Initialize RTDE control and receive interfaces
            self.rtde_c = rtde_control.RTDEControlInterface(self.robot_ip)
            self.rtde_r = rtde_receive.RTDEReceiveInterface(self.robot_ip)
            
            # Initialize socket connection
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.robot_ip, self.port))
            
            # Try to initialize ESP32
            success = False
            for command in ["nstart", "ustart"]:
                response = self.send_esp32_command(command)
                if response:
                    success = True
                    break
            
            if not success:
                print("Failed to initialize ESP32")
                return False
                
            print("Connected to robot and initialized ESP32")
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False
            
    def disconnect(self):
        if self.socket:
            self.socket.close()
        if self.rtde_c:
            self.rtde_c.disconnect()
        if self.rtde_r:
            self.rtde_r.disconnect()
        print("Disconnected from robot")

    def send_esp32_command(self, command):
        try:
            ser = serial.Serial('COM15', 57600, timeout=1)
            
            time.sleep(0.05)  # Wait for connection to stabilize
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            
            print(f"Sending command: {command}")
            ser.write((command + '\n').encode())
        
            start_time = time.time()
            max_wait = 60 if command in ["nstart", "ustart"] else 30
        
            while time.time() - start_time < max_wait:
                if ser.in_waiting:
                    response = ser.readline().decode('utf-8').strip()
                    print(f"Raw ESP32 response: '{response}'")
                
                    if command == "t":
                        try:
                             # Split the response by comma and convert to floats for comparison
                            distances = [float(x) for x in response.split(',')]
                            # Get the lower value as string
                            original_values = response.split(',')
                            value = original_values[distances.index(min(distances))]
                            # Convert to float, divide by 100.0, and convert back to string
                            value = str(float(value))
                            print(f"Parsed distances: {distances}")
                            print(f"Using lower value divided by 100: {value}")
                            ser.close()
                            return value
                        except ValueError:
                            print("Invalid number response for command 't'")
                            break
                    elif command == "v":
                        try:
                            return response
                        except ValueError:
                            print("Invalid number response for command 'v'")
                            break    
                    elif command.startswith('b'):  # Handle any command that starts with 'b'
                        try:
                            value = float(response)
                            print(f"Converted to meters: {value}")
                            if value<0:
                                value*=-1
                                value=(value-100)/2.0
                            else:
                                value=(value-100)/2.0
                                value*=-1
                            ser.close()
                            return value/1000.0
                        except ValueError:
                            print("Invalid number response")
                            break
                    else:
                        ser.close()
                        if response == "true": return True
                        elif response == "false": return False
                        else:
                            print(f"Invalid response: '{response}'")
                            return None
                
                time.sleep(0.1)
            
            ser.close()
            print(f"No response received after {max_wait} seconds")
            return None
        
        except Exception as e:
            print(f"ESP32 error: {e}")
            if 'ser' in locals():
                ser.close()
            return None


    def move_to_position(self, position):
        """Move robot to a single position using RTDE control"""
        try:
            self.rtde_c.moveL(position)
            return self.wait_for_move_completion(position)
        except Exception as e:
            print(f"Move error: {e}")
            return False
    
    def find_shelf_edge(self, starting_pos, step_size=0.007):  # 2mm steps
        current_pos = starting_pos.copy()
        ser = serial.Serial('COM15', 57600, timeout=1)
        ser.reset_output_buffer()
        ser.reset_input_buffer()
        time.sleep(2)
        ser.write(("v" + '\n').encode())
   
        while True:
            if ser.in_waiting:
                response = ser.readline().decode('utf-8').strip()
                print(f"Response: {response}")
                if response == "1":
                    actual_pos = self.rtde_r.getActualTCPPose()
                    ser.close()
                    return actual_pos[2] +0.03

            current_pos[2] -= step_size
            self.move_to_position(current_pos)
            time.sleep(0.1)
        


    def wait_for_move_completion(self, target_pos, timeout=30):
        """Wait for robot to reach target position"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            actual_pos = self.rtde_r.getActualTCPPose()
            if all(abs(a - t) < self.position_tolerance for a, t in zip(actual_pos[:3], target_pos[:3])):
                return True
            time.sleep(0.1)
        return False
    
    
    def pickup_box(self, start_pos, box_pos, box_size):
        self.rtde_c.setPayload(1.65,[0.001,0.019,0.039])
        ser = serial.Serial('COM15', 57600, timeout=1)
        time.sleep(2)
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        ser.close()
        if not self.move_to_position(start_pos):
            raise Exception("Failed to move to starting position")
        
        
        if not self.move_to_position(box_pos):
            raise Exception("Failed to move to starting position")
        
        response = self.send_esp32_command(f"d200")
        if not response:
            print("Warning: Unexpected ESP32 response")
            
        depth = self.send_esp32_command("t")
        depth_mm = float(depth)

            
        depth_mm += 420.0  
        
        response = self.send_esp32_command(f"d{(box_size +150)}")
        if not response:
            print("Warning: Unexpected ESP32 response")
        time.sleep(1)   
        
        neoPos = get_closest_blue_box_x(depth_mm=depth_mm)
        if neoPos is not None:
            
            new_pos = box_pos.copy()
            new_pos[1] += neoPos  

            if not self.move_to_position(new_pos):
                raise Exception("Failed to move to adjusted position")
            else:
                print("No box detected.")
            
        print(f"New y pos {new_pos[1]}")
            
        neoPos = get_closest_blue_box_x(depth_mm=depth_mm)
        if neoPos is not None:
           

            new_pos = new_pos.copy()
            new_pos[1] += neoPos  

            if not self.move_to_position(new_pos):
                raise Exception("Failed to move to adjusted position")
            else:
                print("No box detected.")
        
        print(f"New y pos {new_pos[1]}")
        
            
        if not self.move_to_position(new_pos):
            raise Exception("Failed to move to camera position")

        response = self.send_esp32_command(f"b{box_size-100}")
        
        
            
        new_pos[1] += response
        
        if not self.move_to_position(new_pos):
            raise Exception("Failed to move to adjusted position")

        response = self.send_esp32_command(f"d{(box_size + 30)}")
        if not response:
            print("Warning: Unexpected ESP32 response")
            
        new_pos[2] = self.find_shelf_edge(new_pos)
        
        if not self.move_to_position(new_pos):
            raise Exception("Failed to move to shelf edge")

        
        
        pos = 0.290 + depth/1000.0
        
        
        final_pos = new_pos.copy()
        final_pos[0] -= pos

        if not self.move_to_position(final_pos):
            raise Exception("Failed to move forward")
        final_pos[2]+=-0.01 
        if not self.move_to_position(final_pos):
            raise Exception("Failed to move forward")  
        response = self.send_esp32_command(f"d{(box_size - 15)}")
        if not response:
            print("Warning: Unexpected ESP32 response")
        time.sleep(2)    
        grab_pos = final_pos.copy()
        grab_pos[2] += 0.065
        
        if not self.move_to_position(grab_pos):
            raise Exception("Failed to move to grab height")
            
        self.rtde_c.setPayload(4.8,[0.001,0.019,0.039])
        
        grab_pos[0] += pos+0.15
        if not self.move_to_position(grab_pos):
            raise Exception("Failed final movement")

        return True
    def drop_box(self, start_pos, box_pos, box_size):
        self.rtde_c.setPayload(4.8,[0.001,0.019,0.039])
        ser = serial.Serial('COM15', 57600, timeout=1)
        time.sleep(2)
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        ser.close()
        if not self.move_to_position(start_pos):
            raise Exception("Failed to move to starting position")
        
        current_joint_positions = self.rtde_r.getActualQ()
        
        current_joint_positions[0]=2.25
        self.rtde_c.moveJ(current_joint_positions, speed=1.0, acceleration=1.0)

        # Wait for the movement to complete
        while not self.rtde_c.isSteady():
            time.sleep(0.1)
        # Define the target joint positions (in radians)
        
        
        if not self.move_to_position(box_pos):
            raise Exception("Failed to move to starting position")
        
        new_pos = box_pos.copy()
        new_pos[1]+=0.4
        if not self.move_to_position(new_pos):
            raise Exception("Failed to move to camera position")
        new_pos = new_pos.copy()
        new_pos[2]-=0.025
        if not self.move_to_position(new_pos):
            raise Exception("Failed to move to camera position")
        
        response = self.send_esp32_command(f"d{(box_size +60)}")
        if not response:
            print("Warning: Unexpected ESP32 response")
        self.rtde_c.setPayload(1.65,[0.001,0.019,0.039])
        final_pos = new_pos.copy()
        final_pos[1] -= 0.4
        if not self.move_to_position(final_pos):
            raise Exception("Failed to move forward")
        
        self.rtde_c.moveJ(waypoint2, speed=1.0, acceleration=1.0)
        self.rtde_c.moveJ(waypoint3, speed=1.0, acceleration=1.0)
        self.rtde_c.moveJ(waypoint4, speed=1.0, acceleration=1.0)
        joint_q = [2.3141, -1.4518, -0.5459, -2.7213, -1.5734, -3.8998]
        self.rtde_c.moveJ(joint_q, speed=1.0, acceleration=1.0)

        # Wait for the movement to complete
        while not self.rtde_c.isSteady():
            time.sleep(0.1)
            
        joint_q2 = [3.2179, -1.3348, -0.8826, -2.5848, -1.5725, -2.9233]
        self.rtde_c.moveJ(joint_q2, speed=1.0, acceleration=1.0)
        letf=False
        right=False
        # Wait for the movement to complete
        while not self.rtde_c.isSteady():
            time.sleep(0.1)    
        return True
    def camera(self, start_pos, box_pos, box_size):
            self.rtde_c.setPayload(1.65,[0.001,0.019,0.039])
            ser = serial.Serial('COM15', 57600, timeout=1)
            time.sleep(2)
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            ser.close()
            if not self.move_to_position(start_pos):
                raise Exception("Failed to move to starting position")
            
            
            if not self.move_to_position(box_pos):
                raise Exception("Failed to move to starting position")
            
            response = self.send_esp32_command(f"d200")
            if not response:
                print("Warning: Unexpected ESP32 response")
                
            depth = self.send_esp32_command("t")
            depth_mm = float(depth)

            
            depth_mm += 420.0  # 4 cm = 40 mm
            
            response = self.send_esp32_command(f"d{(box_size +150)}")
            if not response:
                print("Warning: Unexpected ESP32 response")
            time.sleep(1)   
            
            neoPos = get_closest_blue_box_x(depth_mm=depth_mm)
            if neoPos is not None:
                
                new_pos = box_pos.copy()
                new_pos[1] += neoPos  

                if not self.move_to_position(new_pos):
                    raise Exception("Failed to move to adjusted position")
                else:
                    print("No box detected.")
            
            print(f"New y pos {new_pos[1]}")
            
            neoPos = get_closest_blue_box_x(depth_mm=depth_mm)
            if neoPos is not None:
                

                new_pos = new_pos.copy()
                new_pos[1] += neoPos  
                if not self.move_to_position(new_pos):
                    raise Exception("Failed to move to adjusted position")
                else:
                    print("No box detected.")
            
            print(f"New y pos {new_pos[1]}")
            
           
            
                
            neoPos = get_closest_blue_box_x(depth_mm=depth_mm)
            if neoPos is not None:
                new_pos = new_pos.copy()
                new_pos[1] += neoPos  

                if not self.move_to_position(new_pos):
                    raise Exception("Failed to move to adjusted position")
                else:
                    print("No box detected.")
            
            print(f"New y pos {new_pos[1]}")
            
            
            
                
           
            neoPos = get_closest_blue_box_x(depth_mm=depth_mm)
            if neoPos is not None:
                


                new_pos = new_pos.copy()
                new_pos[1] += neoPos 

                if not self.move_to_position(new_pos):
                    raise Exception("Failed to move to adjusted position")
                else:
                    print("No box detected.")
            
            print(f"New y pos {new_pos[1]}")
            
            
            
                
            if not self.move_to_position(new_pos):
                raise Exception("Failed to move to camera position")

  

    
@app.route('/')
def status():
    return '200'

@app.route('/dispatch', methods=['GET'])
def dispatch():
    capture_frames()
    temp_image_path = "./image.png"
    abPath = os.path.abspath("image.png")
    print(abPath)
    executable_path = "./GrabberRec.exe"
    try:
        result = subprocess.run(
            [executable_path, abPath,depth],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return jsonify({"error": "C++ executable failed", "details": result.stderr}), 500

        x = 0;
        y = 0;
        pixelX = 0;
        pixelY = 0;
        output = result.stdout.splitlines()
        print(result)
        for value in output:
            if value[0] == "X":
                x = value.split(":")[1];
                x=float(x)
                x=x/100.0
            elif value[0] == "Y":
                y = value.split(":")[1];
                y=float(y)
                y=y/100.0
            elif value[3] == "X":
                pixelX = value.split(":")[1];
                pixelX2 = ((float(pixelX)-319.707)*depth2)/597.933
            elif value[3] == "Y":
                pixelY = value.split(":")[1];
                pixelY2 = ((float(pixelY)-243.543)*depth2)/597.933
        print(x,y,pixelX,pixelY)

        return [float(pixelX2),float(pixelY2)]
    finally:
        print("Hello")

@app.route('/test')
def capture_frames():
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)

    profile = pipeline.start(config)
    sensor = pipeline.get_active_profile().get_device().query_sensors()[1]
    sensor.set_option(rs.option.exposure, 500.000)

    capture_dir = r"./"
    if not os.path.exists(capture_dir):
        os.makedirs(capture_dir)

    frame = pipeline.wait_for_frames()
    color_frame = frame.get_color_frame()

    if color_frame:
        color_image = np.asanyarray(color_frame.get_data())
        filename = os.path.join(capture_dir, 'image.png')
        img = Image.fromarray(color_image)
        img.save(filename)
        print("success")
    
    pipeline.stop()
    return "200"


def main():
   robot = URRobot()
   try:
       if not robot.connect():
           raise Exception("Failed to connect to robot")
           
       robot.pickup_box(starting_pos, positions2, 300)
       robot.drop_box(waypoint,drop_pos3,300)
       robot.pickup_box(starting_pos, positions, 300)
       robot.drop_box(waypoint,drop_pos2,300)
       
       robot.pickup_box(starting_pos, starting_pos, 300)
       robot.drop_box(waypoint,drop_pos,300)    
   except Exception as e:
       print(f"\nError occurred: {str(e)}")
   finally:
       robot.disconnect()

if __name__ == '__main__':
    main()
    app.run(host=IP, port=int(port), debug=True)