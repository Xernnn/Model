import cv2
import os

# Function to extract frames from a video
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

# Example usage: Extract frames from a video
video_path = "C:/Users/stdso/Documents/USTH/intern/Model/Video1/Video1.mp4"
output_dir = "Video2"
extract_frames(video_path, output_dir)
