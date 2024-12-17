from PIL import Image
import os

# 設定接收資料夾路徑
def file_path():
    input_folder = input("欲套用圖片水印的資料夾路徑: ")
    output_folder = input("欲儲存的資料夾路徑或Enter以套用預設資料夾(原始碼\\img_watermarked): ") or "img_watermarked"
    return input_folder, output_folder


# 設定水印細節
def style_settings():
    # 水印圖片路徑
    watermark_path = input("輸入水印圖片的路徑+\檔名: ")

    print("請設定以下之水印樣式(欲套用預設值請按Enter鍵): ")

    # 設定透明度
    transparency = input("輸入水印透明度0-255(預設為150): ")
    transparency = int(transparency) if transparency.isdigit() else 150

    #設定水印位置
    ch_position = input(
        "選擇水印位置(1)bottom_right (2)bottom_left (3)top_right (4)top_left (5)center (預設為bottom_right): "
    ) or 1
    try:
        if int(ch_position) == 1:
            position = "bottom_right"
        elif int(ch_position) == 2:
            position = "bottom_left"
        elif int(ch_position) == 3:
            position = "top_right"
        elif int(ch_position) == 4:
            position = "top_left"
        elif int(ch_position) == 5:
            position = "center"
    except:
        print("無效的位置輸入，將套用預設值")
        position = "bottom_right"

    return watermark_path, transparency, position


# 調整水印透明度 (使用 getpixel 和 putpixel)
def adjust_tran(watermark_path, transparency):
    try:
        watermark = Image.open(watermark_path).convert("RGBA")
        width, height = watermark.size
        new_watermark = Image.new("RGBA", (width, height))

        # 遍歷每個像素，調整透明度
        for x in range(width):
            for y in range(height):
                r, g, b, a = watermark.getpixel((x, y))
                a = int(a * (transparency / 255))  # 按比例調整原有透明度
                new_watermark.putpixel((x, y), (r, g, b, a))

        return new_watermark
    except Exception as e:
        print(f"處理水印圖片時發生錯誤: {e}")
        return None


# 批次加入圖片水印
def add_watermark(input_folder, output_folder, watermark, position):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(('jpg', 'png', 'jpeg')):
            img_path = os.path.join(input_folder, file_name)

            try:
                with Image.open(img_path).convert("RGBA") as img1:
                    # layer 是一個透明的 RGBA 圖層，目的是在這個圖層上繪製水印，
                    # 然後將這個圖層與原始圖片合併，避免直接修改原始圖片。
                    layer = Image.new("RGBA", img1.size, (0, 0, 0, 0))

                    # 計算水印的位置，根據用戶指定的選項
                    if position == "bottom_right":
                        x, y = img1.width - watermark.width - 50, img1.height - watermark.height - 30
                    elif position == "bottom_left":
                        x, y = 50, img1.height - watermark.height - 50
                    elif position == "top_right":
                        x, y = img1.width - watermark.width - 50, 50
                    elif position == "top_left":
                        x, y = 50, 50
                    elif position == "center":
                        x, y = (img1.width - watermark.width) // 2, (img1.height - watermark.height) // 2
                    else:
                        raise ValueError("未知的位置選項：%s" % position)


                    # 在新圖層上放置水印
                    # layer.paste(image, box, mask)
                    # 將水印圖片(watermark) 放置到透明圖層(layer)的指定位置(x, y)，並使用watermark的透明通道進行遮罩處理
                    layer.paste(watermark, (x, y), watermark)

                    # 將透明圖層(layer) 與原始圖片(img1) 按逐像素透明度進行合成，生成帶水印的新圖片
                    watermarked_img = Image.alpha_composite(img1, layer)

                    # 保存結果
                    output_path = os.path.join(output_folder, file_name)
                    watermarked_img.convert("RGB").save(output_path, "PNG")
                    print("%s 已添加圖片水印並保存" % file_name)

            except Exception as e:
                print("%s 加入圖片水印時發生錯誤：%s" % (file_name, e))


if __name__ == "__main__":
    # 1. 獲取輸入與輸出資料夾路徑
    input_folder, output_folder = file_path()

    # 2. 獲取水印圖片設定與透明度
    watermark_path, transparency, position = style_settings()

    # 3. 調整水印透明度
    watermark = adjust_tran(watermark_path, transparency)

    # 4. 批次處理添加圖片水印
    add_watermark(input_folder, output_folder, watermark, position)