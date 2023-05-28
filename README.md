# PyVeditor

The software enable you to perform video editing options on your local system. The best part of the software is its free to use with no limit on video size. Larger video might take an extra time to prosess though.

## Features 

- **Split a video by scene change** : Everytime scene is change inside the video a new video is created.
- **Merge Videos** : Merge two or more video together. Can also work 
- **Download FB Videos** : Download FB video or reels
- **Download Youtube Videos** : Download Youtube video or reels.

# How to use it.

## Install 

The package `PyVEditor` is a set of events that can be used for video editing. The events can be used using [nlp2fn](https://pypi.org/project/nlp2fn/) software. Install the software using pip

```shell
pip3 install nlp2fn 
```

## Setup ( Add video automations )

[nlp2fn](https://pypi.org/project/nlp2fn/) is free to use software under MIT licence. To use nlp2fn you just need to run the software using 

```shell
nlp2fn run
```

If you haven't used nlp2fn before you, the software will itself prompt you too add a source, else you can just add the source using prompt statement as 

```shell
What can i help you with?
>> add source
```

**Output**

```shell
A source is a collection of functions that can be executed by nlp2fn.
Each function follows a specific format, such as:
# Write your list of execute statements, this shall refer the user to this function.
# Parameters that are required by the event are properly captured with {param_name}.
statement = ["download {link} to {output_dir}"]

# This shall be the main function of your event.
# Once executed, it should perform the necessary operations and return a result.
def execute(args):
    link = args[0]
    output_dir = args[1]
    # Complete the function.
    return True

To add a source, provide the source URL or local directory path.
For a remote GitHub repository, use the following format:
https://github.com/{some_id}/{some_pro}

For a local directory, provide the full path.

Example sources:
Remote GitHub repository: https://github.com/dextrop/evt-langchain
Local directory: /path/to/my/source/directory

Enter the source URL or local directory path:
```

just input source link `https://github.com/dextrop/pyveditor`

```shell
Enter the source URL or local directory path: https://github.com/dextrop/pyveditor
```
## Using PyVEditor

One could also use PyVEditor using NLP interface, to run the interface.
```
nlp2fn run 
```
then to excess the features use the below NLP Prompts.

```shell
# Spilt videos scene by scene
What can i help you with?
>> Split {video_path} on every scene change 

# Spilt videos frame by frame
>> Split {video_link} frame by frame

# Merge all videos
>> Merge {videos}

# Merge all videos inside a folder.
>> Merge all videos inside from {folder_path}
```

## Using though single command

- `nlp2fn exec -m "Split {video_link}"`

- `nlp2fn exec -m "Download facebook video {link}"`

- `nlp2fn exec -m "Download youtube video {link}"`

- `nlp2fn exec -m "Merge {videos}"`

- `nlp2fn exec -m "Merge all videos inside from {folder_path}"`

Split /Users/jennie/Desktop/nlp2fnlibs/pyvideoeditor/testvideo/test.mp4 On Every Scene Change
