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
from typing import Optional


def capture_image() -> Optional[np.ndarray]:
    """
    Webカメラから1枚の画像を取得する関数。

    Returns:
        np.ndarray | None: BGR形式のカメラ画像。取得失敗の場合は None。
    """
    # MyVideoCapture クラスを使ってカメラを初期化
    cam_app = MyVideoCapture()
    cam_app.run()  # カメラ映像を表示して'q'で停止
    img = cam_app.get_img()  # 最後にキャプチャした画像を取得
    return img


def change_image(background_img: np.ndarray, overlay_img: np.ndarray) -> np.ndarray:
    """
    背景画像の白色(255,255,255)を overlay_img の対応するピクセルで置き換える関数。

    Args:
        background_img (np.ndarray): 背景画像（例: google.png）
        overlay_img (np.ndarray): 置き換え元の画像（例: camera_capture.png）

    Returns:
        np.ndarray: 白色領域を置き換えた合成画像
    """
    # 背景画像のコピーを作成（元画像は変更しない）
    result_img = background_img.copy()
    
    # 画像のサイズ確認
    bg_h, bg_w, bg_c = background_img.shape
    ov_h, ov_w, ov_c = overlay_img.shape

    # サイズが異なる場合は overlay_img をリサイズ
    if (bg_h != ov_h) or (bg_w != ov_w):
        overlay_img = cv2.resize(overlay_img, (bg_w, bg_h))

    # 全ピクセルをチェックして白色なら overlay_img の値に置き換え
    for y in range(bg_h):
        for x in range(bg_w):
            b, g, r = background_img[y, x]
            if (b, g, r) == (255, 255, 255):
                result_img[y, x] = overlay_img[y, x]

    return result_img


def save_image(img: np.ndarray, filepath: str = 'output_images/merged_image.png') -> None:
    """
    合成画像を指定パスに保存する関数。

    Args:
        img (np.ndarray): 保存したい画像
        filepath (str): 保存先ファイルパス
    """
    cv2.imwrite(filepath, img)
    print(f"[INFO] 画像を保存しました: {filepath}")


def preview_image(img: np.ndarray, window_name: str = 'Preview') -> None:
    """
    画像をウィンドウに表示する関数。

    Args:
        img (np.ndarray): 表示する画像
        window_name (str): ウィンドウ名
    """
    cv2.imshow(window_name, img)
    print("[INFO] プレビュー表示中。任意のキーで閉じてください。")
    cv2.waitKey(0)  # キー入力待ち
    cv2.destroyWindow(window_name)


def k24118():
    """
    lecture05_01 メイン処理関数。
    - カメラ画像取得
    - google.png の白色領域を置換
    - 合成画像の保存とプレビュー表示
    """
    # 1. カメラ画像取得
    capture_img = capture_image()
    if capture_img is None:
        print("[ERROR] カメラ画像の取得に失敗しました。")
        return

    # 2. 背景画像読み込み
    google_img = cv2.imread('images/google.png')
    if google_img is None:
        print("[ERROR] google.png が読み込めません。")
        return

    print(f"[INFO] google_img: {google_img.shape}, capture_img: {capture_img.shape}")

    # 3. 画像合成（白色置換）
    merged_img = change_image(google_img, capture_img)

    # 4. 合成画像保存
    save_image(merged_img)

    # 5. プレビュー表示
    preview_image(merged_img)


if __name__ == "__main__":
    k24118()
