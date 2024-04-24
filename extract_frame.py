import cv2
import os

def extract_frames(video_path, output_dir):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    os.makedirs(output_dir, exist_ok=True)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1
    
    cap.release()
    print(f"Extracted {frame_count} frames.")

# Copy cái Video path vào đây
video_path = "C:/Users/stdso/Documents/USTH/intern/Model_main/Video1/Video1.mp4"

# Cũng copy cái video path vào đây, nhưng thay tên đuôi Video.mp4 bằng "Frame"
output_dir = "C:/Users/stdso/Documents/USTH/intern/Model_main/Video1/Frame" 
os.makedirs(output_dir, exist_ok=True)
extract_frames(video_path, output_dir)
