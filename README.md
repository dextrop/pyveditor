# PyVeditor

PyVeditor is a software that allows you to perform video editing options on your local system. The best part of the software is that it is free to use and has no limit on video size, although larger videos might take extra time to process.

## Features

- **Split a video by scene change**: This feature allows you to split a video into multiple videos based on scene changes.
- **Merge Videos**: You can merge two or more videos together using this feature.
- **Download FB Videos**: This feature enables you to download Facebook videos or reels.
- **Download YouTube Videos**: You can download YouTube videos or reels using this feature.

# How to Use PyVeditor

## Setup (Add Video Automations)

PyVeditor is designed to be used with the [nlp2fn](https://pypi.org/project/nlp2fn/) software. nlp2fn is a free-to-use software under the MIT license. To use nlp2fn, follow these steps:

1. Install nlp2fn using pip:

```shell
pip3 install nlp2fn
```

2. Run the nlp2fn software:

```shell
nlp2fn run
```

If you haven't used nlp2fn before, it will prompt you to add a source. If you have used it before, you can add a source by entering the following prompt statement:

```shell
What can I help you with?
>> add source
```

**Output**

```shell
A source is a collection of functions that can be executed by nlp2fn.
Each function follows a specific format, such as:
# Write your list of execute statements, which will refer the user to this function.
# Parameters required by the event are properly captured with {param_name}.
statement = ["download {link} to {output_dir}"]

# This should be the main function of your event.
# Once executed, it should perform the necessary operations and return a result.
def execute(args):
    link = args[0]
    output_dir = args[1]
    # Complete the function.
    return True
```

To add the PyVEditor source, input the source link: `https://github.com/dextrop/pyveditor`

```shell
Enter the source URL or local directory path: https://github.com/dextrop/pyveditor
```

## Using PyVEditor

You can also use PyVEditor through the NLP interface. To run the interface, use the following command:

```shell
nlp2fn run
```

Once the interface is running, you can access the features using the following NLP prompts:

```shell
# Split videos scene by scene
What can I help you with?
>> Split {video_path} on every scene change 

# Split videos frame by frame
>> Split {video_link} frame by frame

# Merge all videos
>> Merge {videos}

# Merge all videos inside a folder
>> Merge all videos inside from {folder_path}
```

## Using Single Commands

You can use PyVEditor features through single commands using the `nlp2fn exec` command. Here are some examples:

- `nlp2fn exec -m "Split {video_link}"`
- `nlp2fn exec -m "Download Facebook video {link}"`
- `nlp2fn exec -m "Download YouTube video {link}"`
- `nlp2fn exec -m "Merge {videos}

"`
- `nlp2fn exec -m "Merge all videos inside from {folder_path}"`

Make sure to replace `{video_link}`, `{link}`, `{videos}`, and `{folder_path}` with the appropriate values.