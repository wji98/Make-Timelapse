# Make-Timelapse
This script processes source videos in a specified directory and stitches them together to generate a timelapse video

This project uses moviepy. To install, run the following command:

```
pip install moviepy
```

Go into the file create_timelapse.py and edit the parameters, including the directory where your source videos are stored, and run the script:

```
python create_timelapse.py
```

Your timelapse (with audiotrack removed) will be written as an mp4 file in the same directory as the source folder under the name "timelapse.mp4"

Note: writing the mp4 file is time intensive, similar to how exporting a video in a video editor is time intensive as well.
