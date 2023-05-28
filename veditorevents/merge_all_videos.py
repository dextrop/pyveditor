import os

STATEMENT = "Merge all videos inside from {folder_path}"

def get_video_files(directory):
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']  # Add more extensions as needed
    video_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension.lower() in video_extensions:
                video_files.append(os.path.join(root, file))


    return video_files

def execute(args):
    directory = args["folder_path"]
    video_files = get_video_files(directory)
    files_text = (",").join(video_files)
    os.system(f'nlp2fn exec -m "Merge {files_text}"')