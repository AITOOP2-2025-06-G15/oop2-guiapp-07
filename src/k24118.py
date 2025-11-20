from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture
from src.lecture05_01 import capture_image, change_image, save_image, preview_image
import cv2

def lecture05_01():
    # カメラ取得
    captured_img = capture_image()

    # google.png 読み込み
    google_img = cv2.imread('images/google.png')

    # 合成
    result_img = change_image(google_img, captured_img)

    # 保存
    save_image(result_img, "output_images/k24118_edited_img.png")

    # 表示（GUIで使う場合は別でも良い）
    preview_image(captured_img)
