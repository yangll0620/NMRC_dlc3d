# NMRC_dlc3d

Using 3d Deeplabcut in NMRC

## Key Steps

1. Activate deeplabcut environment in Anaconda

    `conda activate DEEPLABCUT`

2.  Extract Calibration Images

    `ffmpeg -i v_20220114-142831_camera0.avi -vframes 500 cam0\camera-0-%03d.jpg`
    
    `ffmpeg -i v_20220114-142831_camera1.avi -vframes 500 cam1\camera-1-%03d.jpg`

3. Select Pairs of Calibration Images from Extracted Images (at 70 Pairs)

> Aim for at least 70 pairs of images

    > camera-0-001.jpg and camera-1-001.jpg are one pair.
    > camera-0-033.jpg and camera-1-033.jpg are another pair.

> Keep the orientation of the chessboard same and do not rotate more than 30 degrees.

> Cover several distances, and within each distance, cover all parts of the image view (all corners and center).


## Documentation from Deeplabcut Official Website
https://github.com/DeepLabCut/DeepLabCut/blob/master/docs/Overviewof3D.md


