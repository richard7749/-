from PIL import Image, ImageDraw, ImageFont
import os


def main():
    """
    字型樣式選擇的主流程
    """
    # 定義字型存放的資料夾名稱
    font_folder = "font_ttf"
    # 定義字型檔案列表，使用 os.path.join 動態生成完整路徑，確保跨平台兼容性
    font_files = [
        os.path.join(font_folder, "Arial.ttf"),
        os.path.join(font_folder, "AlexBrush-Regular.ttf"),
        os.path.join(font_folder, "Playball.ttf"),
        os.path.join(font_folder, "DancingScript-Bold.ttf"),
        os.path.join(font_folder, "kaiu.ttf")
    ]

    # 調用 choose_font 函數，生成字型預覽並讓使用者選擇字型
    selected_font = choose_font(font_files)
    # 打印時只顯示文件名，不顯示資料夾路徑
    print(f"您選擇的字型是：{os.path.basename(selected_font)}")
    return selected_font


def font_preview(
    font_list, preview_text="Text watermark style preview"
):
    """
    生成字型預覽圖片
    font_list: 字型文件路徑列表
    preview_text: 預覽的文字
    """

    # 設置圖片大小和背景顏色
    width, height = 1000, 100 * len(font_list)
    img = Image.new("RGB", (width, height), color=(255, 255, 255))

    draw = ImageDraw.Draw(img)
    y = 50

    for i, font_path in enumerate(font_list):
        try:
            font = ImageFont.truetype(font_path, 30)

            # 只提取字型文件名（不包含資料夾路徑）
            font_name = os.path.basename(font_path)
            # 設定文字內容，包含字型序號與名稱
            text = f"{i+1}. {font_name} - {preview_text}"
        except Exception as e:
            # 如果字型加載失敗，提示使用者該字型無效
            font_name = os.path.basename(font_path)  # 只顯示文件名
            font = ImageFont.load_default()
            text = f"{i+1}. 無效字型 ({font_name})"

        # 在圖片上繪製字型預覽
        draw.text((100, y), text, fill=(0, 0, 0), font=font)
        y += 50

    # 預覽圖片
    img.show()


def choose_font(font_list):
    """
    讓使用者從字型預覽中選擇一個字型
    """

    # 生成字型預覽圖片
    font_preview(font_list)

    # 提示使用者查看圖片並選擇字型
    print("請根據生成的字型預覽圖片來選擇字型")
    print("*** 字型僅支援英文，繁體中文請選擇(5)kaiu.ttf ***")
    while True:
        choice = input(f"輸入字型序號1-{len(font_list)}(或按Enter使用預設字型)： ") or "0"
        if choice.isdigit() and 0 <= int(choice) <= len(font_list):
            choice = int(choice)
            if choice == 0:
                return "Arial.ttf"  # 預設字型
            return font_list[choice - 1]  # 返回選擇的字型
        else:
            print("輸入無效，請重新輸入序號。")


if __name__ == "__main__":
    main()
