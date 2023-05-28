import youtube_dl

STATEMENT = "Download {type} video {link}"

supported_channel = ["youtube", "facebook"]

def execute(args):
    type = args["type"]
    if type not in supported_channel:
        raise ValueError(f"Unable to download video from {type}")

    url = args["link"]
    save_path = url.split("/")[-1] + ".mp4"
    ydl_opts = {
        'outtmpl': save_path,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"Video downloaded successfully to {save_path}")

