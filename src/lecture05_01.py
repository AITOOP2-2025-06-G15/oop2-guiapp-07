# k24108_image_processing.py
import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

# ---------------------------------------------
# 1. カメラ画像取得
# ---------------------------------------------
def capture_image() -> np.ndarray:
    """
    Webカメラから1枚画像を取得する関数

    Returns:
        np.ndarray: BGR形式の取得画像
    """
    # MyVideoCaptureクラスを使ってカメラキャプチャ
    app = MyVideoCapture()
    app.run()  # 'q' を押すと終了して1枚取得
    img = app.get_img()
    
    if img is None:
        raise ValueError("カメラ画像が取得できませんでした。")
    
    return img

# ---------------------------------------------
# 2. 画像合成（白色を置換）
# ---------------------------------------------
def change_image(base_img: np.ndarray, overlay_img: np.ndarray) -> np.ndarray:
    """
    base_img の白色部分 (255,255,255) を overlay_img で置き換える関数

    Args:
        base_img (np.ndarray): 背景画像（置換対象の白色あり）
        overlay_img (np.ndarray): 置換する画像

    Returns:
        np.ndarray: 合成後の画像
    """
    result_img = base_img.copy()
    
    b_h, b_w, _ = base_img.shape
    o_h, o_w, _ = overlay_img.shape
    
    # 白色の部分を置換
    for y in range(b_h):
        for x in range(b_w):
            b, g, r = base_img[y, x]
            if (b, g, r) == (255, 255, 255):
                # overlay_img を繰り返して埋める場合
                result_img[y, x] = overlay_img[y % o_h, x % o_w]
    
    return result_img

# ---------------------------------------------
# 3. 画像保存
# ---------------------------------------------
def save_image(img: np.ndarray, filepath: str) -> None:
    """
    画像を指定パスに保存する関数

    Args:
        img (np.ndarray): 保存する画像
        filepath (str): 保存先ファイルパス
    """
    cv2.imwrite(filepath, img)

# ---------------------------------------------
# 4. 画像表示（テスト・GUI用）
# ---------------------------------------------
def preview_image(img: np.ndarray, window_name: str = "preview") -> None:
    """
    画像を表示する関数。確認用。

    Args:
        img (np.ndarray): 表示する画像
        window_name (str): ウィンドウ名
    """
    cv2.imshow(window_name, img)
    cv2.waitKey(0)  # キー入力待ち
    cv2.destroyAllWindows()

# ---------------------------------------------
# テスト用 main
# ---------------------------------------------
if __name__ == "__main__":
    # カメラ画像取得
    capture_img = capture_image()
    
    # 合成元画像を読み込み
    google_img = cv2.imread('images/google.png')
    
    # 合成処理
    edited_img = change_image(google_img, capture_img)
    
    # 保存
    save_image(edited_img, "output_images/k24108_edited_img.png")
    
    # 確認表示
    preview_image(capture_img)
