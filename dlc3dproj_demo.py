import deeplabcut

projExist = True
cornerDetected = True
calibrated = True
calibrated = True
calibrated = True
checkUndistortion = True
triangulated = False



if projExist is not True:
    print(".....creating a new 3d project.......")
    config_path3d = deeplabcut.create_new_project_3d('demo3d', 'yll', num_cameras=2)
else:
    config_path3d = 'C:\\Users\lingling\\Desktop\dlcProject\\dlcDemo\\demo3d-yll-2022-02-01-3d\\config.yaml'



if cornerDetected is not True: # detect corners and remove bad images
    print(".....detecting corners and removing bad images.......")
    deeplabcut.calibrate_cameras(config_path3d, cbrow=8, cbcol=6, calibrate=False, alpha=0.9)


if calibrated is not True: # calibrate
    deeplabcut.calibrate_cameras(config_path3d, cbrow=8, cbcol=6, calibrate=True, alpha=0.9)

if checkUndistortion is not True:
    deeplabcut.check_undistortion(config_path3d, cbrow=8, cbcol=6)

if ~triangulated: # Triangulation --> Take your 2D to 3D!
    print(".....Triangulation --> Take your 2D to 3D!.......")
    videos_path = r'C:\Users\lingling\Desktop\dlcProject\dlcDemo\demo3d-yll-2022-02-11-3d\COTVideos'
    deeplabcut.triangulate(config_path3d, videos_path, filterpredictions=True)


# Visualize  3D DeepLabCut Videos
triangulated_file_folder = r'C:\Users\lingling\Desktop\dlcProject\dlcDemo\demo3d-yll-2022-02-11-3d\COTVideos'
deeplabcut.create_labeled_video_3d(config_path3d, triangulated_file_folder, start=50, end=250)
