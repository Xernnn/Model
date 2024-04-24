import cv2
import os

def annotate(image_path, keypoints, output_image_path, keypoints_file_path):
    img = cv2.imread(image_path)
    
    for name, (x, y, visibility) in keypoints.items():
        if visibility:
            cv2.circle(img, (x, y), radius=6, color=(0, 0, 255), thickness=-1)
            
    cv2.imshow("Annotated Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite(output_image_path, img)
    
    with open(keypoints_file_path, 'w') as file:
        for name, (x, y, visibility) in keypoints.items():
            file.write(f"{name}: ({x}, {y}, {visibility})\n")
    
    print(f"Annotated image saved to {output_image_path}")
    print(f"Keypoints saved to {keypoints_file_path}")

# Sửa path của 2 cái dưới thôi
path = "C:/Users/stdso/Documents/USTH/intern/Model_main/Video1" # Điền Video path như file trước vào, nhưng bỏ phần Video ở cuối đi
picture = "frame_0100" # File ảnh đang làm việc. Mỗi lần +1 để sang ảnh tiếp theo
# Nhớ là ảnh bắt đầu từ 0000 chứ không phải 0001

image_path = f"{path}/Frame/{picture}.jpg"
output_image_path = f"{path}/Output/{picture}.jpg"
keypoints_file_path = f"{path}/Keypoints/{picture}.txt"

# Chỉnh các đốm đỏ cho đúng với cả vị trí được cảm quan 2 thông số đầu, thông số cuối là xem nó tồn tại trên ảnh hay không.
# Số đầu cho chiều ngang (chiều x), số thứ 2 cho chiều dọc (chiều y)
keypoints = {
    "nose": (6744, 190, 1), # Mũi
    "left_hand": (430, 280, 1), # Bàn tay trái
    "left_elbow": (550, 330, 1), # Khửu tay trái
    "left_shoulder": (655, 255, 1), # Vai trái
    "right_shoulder": (810, 265, 1), # Vai phải
    "right_elbow": (920, 330, 1), # Khửu tay phải
    "right_hand": (1050, 300, 1), # Bàn tay phải
    "left_hip": (640, 510, 1), # Hông trái
    "right_hip": (795, 520, 1), # Hông phải
    "left_knee": (0, 0, 0), # Đầu gối trái
    "left_foot": (0, 0, 0), # Bàn chân trái
    "right_knee": (0, 0, 0), # Đầu gối phái
    "right_foot": (0, 0, 0) # Bàn chân phải
}

# Ensure the directory exists
os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
os.makedirs(os.path.dirname(keypoints_file_path), exist_ok=True)

annotate(image_path, keypoints, output_image_path, keypoints_file_path)
