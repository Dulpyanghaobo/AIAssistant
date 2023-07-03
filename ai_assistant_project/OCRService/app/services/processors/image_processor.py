from OCRService.app.services.processors.IInputProcessor import IInputProcessor

class ImageProcessor(IInputProcessor):
    def process(self, image_file):
        # 处理图像文件
        print("ImageProcessor process")
        pass