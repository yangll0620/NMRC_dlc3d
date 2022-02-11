# NMRC_dlc3d

Using 3d Deeplabcut in NMRC

## Key Steps

1. Activate deeplabcut environment in Anaconda

    `conda activate DEEPLABCUT`

2.  Extract and Select Calibration Images 

2-1 Extract Images from videos through running the following codes

When recording videos: 

> Keep the orientation of the chessboard same and do not rotate more than 30 degrees.

> Cover several distances, and within each distance, cover all parts of the image view (all corners and center).

    `ffmpeg -i v_20220114-142831_camera0.avi -vframes 500 cam0\camera-0-%03d.jpg`
    
    `ffmpeg -i v_20220114-142831_camera1.avi -vframes 500 cam1\camera-1-%03d.jpg`

2-2. Select Pairs of Calibration Images from Extracted Images (at 70 Pairs) 

> Aim for at least 70 pairs of images

    > camera-0-001.jpg and camera-1-001.jpg are one pair.
    > camera-0-033.jpg and camera-1-033.jpg are another pair.

3. Place the Calibration Images into the calibration_images directory.

4. Calibration

4-1 Edit the config.yaml file to set the camera names.

4-2 Run the following code (detect corners and remove bad images)

`deeplabcut.calibrate_cameras(config_path3d, cbrow=8, cbcol=6, calibrate=False, alpha=0.9)`

4-3 Run the calibrate_cameras() function again with calibrate=True (computes the intrinsic and extrinsic parameters for each camera)

`deeplabcut.calibrate_cameras(config_path3d, cbrow=8, cbcol=6, calibrate=True, alpha=0.9)`

5. Check for Undistortion (not fully understand what to get and how to check the results)

`deeplabcut.check_undistortion(config_path3d, cbrow=8, cbcol=6)`


## Documentation from Deeplabcut Official Website
https://github.com/DeepLabCut/DeepLabCut/blob/master/docs/Overviewof3D.md


