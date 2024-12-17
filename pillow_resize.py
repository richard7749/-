from PIL import Image
import os


# 接收資料夾路徑
def file_path():
    input_folder = input("欲批次調整圖片的資料夾路徑: ")
    output_folder = input("欲儲存的資料夾路徑或Enter以套用預設資料夾(原始碼\\resized): ") or "resized"
    return input_folder, output_folder


# 讓使用者選擇輸出圖片的寬和高
def input_size():
    while True:
        try:
            width = int(input("請輸入想輸出的圖片寬度(預設為800): ") or 800)
            height = int(input("請輸入想輸出的圖片高度(預設為500): ") or 500)
            # 確保輸入的值是正整數
            if width > 0 and height > 0:
                size = (width, height)
                return size
            else:
                print("寬度和高度必須是正數，請重新輸入。")
        except ValueError:
            print("輸入無效，請輸入正整數。")


# 批次調整圖片大小
def resize_images(input_folder, output_folder):
    size = input_size()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(('jpg', 'png', 'jpeg')):
            img_path = os.path.join(input_folder, file_name)

            try:
                img1 = Image.open(img_path)
                img2 = img1.resize(size, Image.LANCZOS)

                output_path = os.path.join(output_folder, file_name)
                img2.save(output_path)
                print("%s 已調整圖片大小" % file_name)
            except Exception as e:
                print("%s 轉換時發生錯誤：%s" % (file_name, e))


if __name__ == "__main__":
    input_folder, output_folder = file_path()
    resize_images(input_folder, output_folder)