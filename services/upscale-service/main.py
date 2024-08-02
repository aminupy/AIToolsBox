import cv2
import time
import os


base_dir = os.getcwd()



models_path = os.path.join(base_dir, "models/")


def upscale(image_path, ratio):
    img = cv2.imread(image_path)
    search_string = r"\www"
    img_name = image_path[image_path.rfind(search_string[0]) + 1:]
    print(img_name)
    if ratio not in [2, 3, 4] :
        raise ValueError
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    model = os.path.join(models_path, f"ESPCN_x{ratio}.pb")
    sr.readModel(model)
    sr.setModel('espcn', ratio)
    timer = time.time()
    print(f"{ratio}x upscaling image...")
    upscaled = sr.upsample(img)
    cv2.imwrite(f"{ratio}x_{img_name}",upscaled)
    print("done")
    now_time = time.time()
    timer = now_time - timer
    print(f"time spent : {int(timer)} seconds")
    return os.path.join(base_dir, image_path)





print(upscale("images\sample.jpg",2))