import cv2
import time
import os






models_path = "models/"

def upscale_2x(image_path):
    img = cv2.imread(image_path)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    model = os.path.join(models_path, "ESPCN_x2.pb")
    sr.readModel(model)
    sr.setModel('espcn', 2)
    timer = time.time()
    print("2x upscaling image...")
    upscaled = sr.upsample(img)
    cv2.imwrite("result.jpg",upscaled)
    print("done")
    now_time = time.time()
    timer = now_time - timer
    print(f"time spent {int(timer)} seconds")


def upscale_3x(image_path):
    img = cv2.imread(image_path)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    model = os.path.join(models_path, "ESPCN_x3.pb")
    sr.readModel(model)
    sr.setModel('espcn', 3)
    timer = time.time()
    print("3x upscaling image...")
    upscaled = sr.upsample(img)
    cv2.imwrite("result.jpg",upscaled)
    print("done")
    now_time = time.time()
    timer = now_time - timer
    print(f"time spent {int(timer)} seconds")

def upscale_4x(image_path):
    img = cv2.imread(image_path)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    model = os.path.join(models_path, "ESPCN_x4.pb")
    sr.readModel(model)
    sr.setModel('espcn', 4)
    timer = time.time()
    print("4x upscaling image...")
    upscaled = sr.upsample(img)
    cv2.imwrite("result.jpg",upscaled)
    print("done")
    now_time = time.time()
    timer = now_time - timer
    print(f"time spent {int(timer)} seconds")


upscale_4x("images/logo.jpg")