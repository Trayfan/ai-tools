from PIL import ImageGrab

class GetScreen():
    def get_screen(self, image_name):
        # grab fullscreen
        im = ImageGrab.grab()
        # save image file
        im.save(image_name)