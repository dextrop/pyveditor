import time

from moviepy.editor import VideoFileClip, concatenate_videoclips

STATEMENT = "Merge {videos}"

def execute(args):
    video_paths = args["videos"].replace(" ", "").split(",")
    output_path = "merged-" + str(time.time()).replace(".", "-") + "mp4"
    clips = []

    # Load each video clip
    for path in video_paths:
        clip = VideoFileClip(path)
        clips.append(clip)

    # Concatenate the video clips
    final_clip = concatenate_videoclips(clips)

    # Write the final merged video to the output path
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close the video clips
    for clip in clips:
        clip.close()