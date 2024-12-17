import sys
import pillow_resize
import pillow_watermark_text
import pillow_watermark_img


def choose_menu():
    while True:
        print("")
        print("請選擇欲執行的功能: (1)調整圖片大小 (2)添加文字水印 (3)添加圖片水印 (4)離開程式")
        choice = input("請輸入選項 1/2/3/4： ")

        if choice == '1':
            # 調整圖片大小
            input_folder, output_folder = pillow_resize.file_path()
            pillow_resize.resize_images(input_folder, output_folder)

        elif choice == '2':
            # 添加文字水印
            input_folder, output_folder = pillow_watermark_text.file_path()
            word, selected_font_path, text_size, watermark_color, position = pillow_watermark_text.style_settings()
            pillow_watermark_text.add_watermark(input_folder, output_folder, word, selected_font_path, text_size, watermark_color, position)

        elif choice == '3':
            # 添加圖片水印
            input_folder, output_folder = pillow_watermark_img.file_path()
            watermark_path, transparency, position = pillow_watermark_img.style_settings()
            watermark = pillow_watermark_img.adjust_tran(watermark_path, transparency)
            pillow_watermark_img.add_watermark(input_folder, output_folder, watermark, position)

        elif choice == '4':
            exit_fun()

        else:
            print("無效的選擇，請重新輸入。")


def exit_fun():
    print("已退出程式")
    sys.exit()


if __name__ == "__main__":
    choose_menu()

