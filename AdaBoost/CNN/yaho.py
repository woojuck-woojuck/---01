

import cv2

def main():
    image_path = 'path_to_image.jpg'
    img = cv2.imread(image_path)

    if img is None:
        print(f"이미지를 로드하지 못했습니다: {image_path}")
    else:
        print("이미지가 성공적으로 로드되었습니다")
        try:
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            print("이미지를 그레이스케일로 성공적으로 변환했습니다")
        except cv2.error as e:
            print(f"색상 변환 중 OpenCV 오류 발생: {e}")

if __name__ == '__main__':
    main()