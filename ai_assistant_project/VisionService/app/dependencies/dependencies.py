from VisionService.app.api.vision.services.image_generator import ImageGenerator, ThirdPartyImageGenerator


def get_image_generator() -> ImageGenerator:
    return ThirdPartyImageGenerator()  # 或者你自己的实现
