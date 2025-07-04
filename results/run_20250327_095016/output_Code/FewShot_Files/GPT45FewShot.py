from PIL import Image, ImageEnhance

class ImageProcessor:
    """
    This is a class to process image, including loading, saving, resizing, rotating, and adjusting the brightness of images.
    """

    def __init__(self):
        """
        Initialize self.image
        """
        self.image = None

    def load_image(self, image_path):
        """
        Use Image util in PIL to open an image
        :param image_path: str, path of image that is to be loaded
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
        """
        # Open the image and set it to self.image
        self.image = Image.open(image_path)

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        >>> processor.load_image('test.jpg')
        >>> processor.save_image('test2.jpg')
        """
        # Save the image to the specified path if it's loaded
        if self.image:
            self.image.save(save_path)

    def resize_image(self, width, height):
        """
        Resize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(300, 300)
        >>> processor.image.width
        300
        >>> processor.image.height
        300
        """
        # Resize the image to the specified width and height if it's loaded
        if self.image:
            self.image = self.image.resize((width, height))

    def rotate_image(self, degrees):
        """
        Rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        >>> processor.load_image('test.jpg')
        >>> processor.rotate_image(90)
        """
        # Rotate the image by the specified degree if it's loaded
        if self.image:
            self.image = self.image.rotate(degrees, expand=True)

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
        # Adjust the brightness of the image by the specified factor if it's loaded
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)