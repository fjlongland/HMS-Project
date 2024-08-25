import os
import cv2


SourceFileName = "C:\\Users\\Admin\Desktop\\HMS test file source\\test video.mp4"
DestinationFileName = "C:\\Users\\Admin\\Desktop\\HMS tets file destination\\Destination\\test video parsed.mp4"

cap = cv2.VideoCapture(SourceFileName)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
faramesize = (width, height)

print(fps)
print(width)
print(height)
print(fourcc)


out = cv2.VideoWriter(DestinationFileName, fourcc, fps, faramesize)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)

cap.release()
out.release()

print(f"video saved to {DestinationFileName}")


