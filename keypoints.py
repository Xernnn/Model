import cv2
import os

def annotate(image_path, keypoints, output_image_path, keypoints_file_path):
    img = cv2.imread(image_path)
    
    # Annotate keypoints
    for name, (x, y, visibility) in keypoints.items():
        if visibility:
            cv2.circle(img, (x, y), radius=6, color=(0, 0, 255), thickness=-1)
            
    cv2.imshow("Annotated Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the annotated image
    cv2.imwrite(output_image_path, img)
    
    # Save keypoints to a text file
    with open(keypoints_file_path, 'w') as file:
        for name, (x, y, visibility) in keypoints.items():
            file.write(f"{name}: ({x}, {y}, {visibility})\n")
    
    print(f"Annotated image saved to {output_image_path}")
    print(f"Keypoints saved to {keypoints_file_path}")

image_path = "C:/Users/stdso/Documents/USTH/intern/Model/Video1/frame_0100.jpg"
output_image_path = "C:/Users/stdso/Documents/USTH/intern/Model/Video1/Video1_o/frame_0100.jpg"
keypoints_file_path = "C:/Users/stdso/Documents/USTH/intern/Model/Video1/Video1_kp/frame_0100.txt"

keypoints = {
    "nose": (744, 190, 1),
    "right_hand": (430, 280, 1),
    "right_elbow": (550, 330, 1),
    "right_shoulder": (655, 255, 1),
    "left_shoulder": (810, 265, 1),
    "left_elbow": (920, 330, 1),
    "left_hand": (1050, 300, 1),
    "right_hip": (640, 510, 1),
    "left_hip": (795, 520, 1),
    "right_knee": (0, 0, 0),
    "right_foot": (0, 0, 0),
    "left_knee": (0, 0, 0),
    "left_foot": (0, 0, 0)
}

# Ensure the directory exists
os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
os.makedirs(os.path.dirname(keypoints_file_path), exist_ok=True)

annotate(image_path, keypoints, output_image_path, keypoints_file_path)
