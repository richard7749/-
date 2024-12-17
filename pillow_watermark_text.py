from PIL import Image, ImageDraw, ImageFont
import os
import font_preview


# 設定接收資料夾路徑
def file_path():
    input_folder = input("欲套用文字水印的資料夾路徑: ")
    output_folder = input("欲儲存的資料夾路徑或Enter以套用預設資料夾(原始碼\\text_watermarked): ") or "text_watermarked"
    return input_folder, output_folder


# 設定水印細節
def style_settings():
    word = input("輸入欲加上的水印文字: ")

    print("請設定以下之水印樣式(欲套用預設值請按Enter鍵): ")

    # 字型選擇
    selected_font_path = font_preview.main()

    # 字型大小
    text_size = input("字型大小(預設為30): ")
    text_size = int(text_size) if text_size.isdigit() else 30

    # 顏色選擇
    print("選擇水印顏色： (1)Black  (2)White  (3)Gray  (4)Pink  (5)Purple  (6)Blue (7)自定義RGB")
    while True:
        color_choice = input("請輸入1-7 (預設為5): ") or 5

        try:
            if int(color_choice) == 1:
                watermark_color = (0, 0, 0)  # Black
            elif int(color_choice) == 2:
                watermark_color = (255, 255, 255)  # White
            elif int(color_choice) == 3:
                watermark_color = (128, 128, 128)  # Gray
            elif int(color_choice) == 4:
                watermark_color = (255, 192, 203)  # Pink
            elif int(color_choice) == 5:
                watermark_color = (188, 117, 255)  # Purple
            elif int(color_choice) == 6:
                watermark_color = (41, 148, 255)  # Blue
            elif int(color_choice) == 7:
                # 自定義 RGB 輸入
                while True:
                    try:
                        r_color = int(input("R (0-255): "))
                        g_color = int(input("G (0-255): "))
                        b_color = int(input("B (0-255): "))

                        # 確保每個值在合理範圍內
                        if not (0 <= r_color <= 255 and 0 <= g_color <= 255 and 0 <= b_color <= 255):
                            raise ValueError
                        watermark_color = (r_color, g_color, b_color)
                        break  # 自定義 RGB 輸入成功，退出內層迴圈
                    except ValueError:
                        print("RGB 值必須是 0-255 之間的整數，請重新輸入。")
            else:
                raise ValueError

            # 成功選擇顏色，跳出外層迴圈
            break
        except ValueError:
            print("無效的選擇，請輸入數字1-7")

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

    return word, selected_font_path, text_size, watermark_color, position


# 批次加入文字水印
def add_watermark(input_folder, output_folder, word, selected_font_path, text_size, watermark_color, position):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(('jpg', 'png', 'jpeg')):
            img_path = os.path.join(input_folder, file_name)

            try:
                with Image.open(img_path) as img1:
                    draw = ImageDraw.Draw(img1)

                    # 嘗試加載字型檔案
                    try:
                        font = ImageFont.truetype(selected_font_path, text_size)
                    except IOError:
                        print(f"警告：無法加載字型 '{selected_font_path}'，將使用默認字型")
                        font = ImageFont.load_default()

                # 使用 textbbox 計算文字的邊界框
                bbox = draw.textbbox((0, 0), word, font=font)
                word_width = bbox[2] - bbox[0]
                word_height = bbox[3] - bbox[1]

                if position == "bottom_right":
                    x, y = img1.width - word_width - 50, img1.height - word_height - 50
                elif position == "bottom_left":
                    x, y = 50, img1.height - word_height - 50
                elif position == "top_right":
                    x, y = img1.width - word_width - 50, 50
                elif position == "top_left":
                    x, y = 50, 50
                elif position == "center":
                    x, y = (img1.width - word_width) // 2, (img1.height - word_height) // 2
                else:
                    raise ValueError("未知的位置選項：%s" % position)

                # 添加水印
                draw.text((x, y), word, fill=watermark_color ,font=font)
                output_path = os.path.join(output_folder, file_name)
                img1.save(output_path)
                print("%s 已添加文字水印並保存" % file_name)

            except Exception as e:
                print("%s 加入文字水印時發生錯誤：%s" % (file_name, e))


if __name__ == "__main__":
    input_folder, output_folder = file_path()
    word, selected_font_path, text_size, watermark_color, position = style_settings()
    add_watermark(input_folder, output_folder, word, selected_font_path, text_size, watermark_color, position)