import os

import cv2
import imagehash
from PIL import Image

STATEMENT = "Split {video_link}"

def calculate_frame_hash(frame):
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize frame to a smaller resolution (optional, for faster processing)
    resized_frame = cv2.resize(gray_frame, (160, 90))

    # Convert the resized frame to an Image object
    image = Image.fromarray(resized_frame)

    # Calculate perceptual hash of the resized frame
    frame_hash = imagehash.phash(image)

    return frame_hash


def split_video_by_scene_changes(input_file, output_prefix):
    # Open the video file
    video = cv2.VideoCapture(input_file)

    print("Video File opened")

    # Get the video's frames per second (fps)
    fps = video.get(cv2.CAP_PROP_FPS)

    # Initialize variables for scene change detection
    scene_changes = []

    # Read the first frame
    success, prev_frame = video.read()
    if not success:
        print("Error reading video file")
        return

    # Calculate hash of the first frame
    prev_frame_hash = calculate_frame_hash(prev_frame)

    # Iterate through the remaining frames
    frame_number = 1
    while True:
        success, curr_frame = video.read()
        if not success:
            break

        # Calculate hash of the current frame
        curr_frame_hash = calculate_frame_hash(curr_frame)

        # Compare the hashes to detect scene changes
        hash_difference = prev_frame_hash - curr_frame_hash
        if hash_difference > 20:  # Adjust this value as needed
            scene_changes.append(frame_number)

        prev_frame_hash = curr_frame_hash
        frame_number += 1

    # Split the video based on scene changes
    for i, scene_start in enumerate(scene_changes):
        if i + 1 < len(scene_changes):
            scene_end = scene_changes[i + 1] - 1
        else:
            scene_end = frame_number - 1

        # Set the output filename
        output_file = f"{output_prefix}/scene_{i + 1}.mp4"

        # Create a new video writer for the scene
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(output_file, fourcc, fps, (prev_frame.shape[1], prev_frame.shape[0]))

        # Set the video position to the start frame of the scene
        video.set(cv2.CAP_PROP_POS_FRAMES, scene_start)

        # Write the scene frames to the output video file
        while scene_start <= scene_end:
            success, frame = video.read()
            if not success:
                break

            video_writer.write(frame)
            scene_start += 1

        video_writer.release()

        print(f"Scene {i + 1} saved to {output_file}")

    video.release()


def execute(args):
    if "video_link" in args:
        video_path = args["video_link"]
        output_folder = video_path.split(".")[0]
        print (f"Making Dir {output_folder}")
        os.makedirs(output_folder)
        split_video_by_scene_changes(
            video_path, output_folder
        )