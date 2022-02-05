import deeplabcut
deeplabcut.create_new_project_3d('demo3d', 'yll', num_cameras=2)

config_path3d = 'C:\\Users\lingling\\Desktop\dlcProject\\dlcDemo\\demo3d-yll-2022-02-01-3d\\config.yaml'


# detect corners and remove bad images
deeplabcut.calibrate_cameras(config_path3d, cbrow=8, cbcol=6, calibrate=False, alpha=0.9)

# calibrate
deeplabcut.calibrate_cameras(config_path3d, cbrow=8, cbcol=6, calibrate=True, alpha=0.9)