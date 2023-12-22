import os, random
from typing import List
from PIL import Image

class Layer:
    def __init__(self, path: str):
        self.path = path

    def get_random_image_path(self):
        image_file_names = os.listdir(self.path)
        random_image_file_name = random.choice(image_file_names)
        return os.path.join(self.path, random_image_file_name)

class Generator:
    def __init__(self, images_path: str):
        self.layers: List[Layer] = self.load_image_layers(images_path)
        self.background_color = (None)
        self.output_path: str = "./data"
        os.makedirs(self.output_path, exist_ok=True)

    def load_image_layers(self, images_path: str):
        sub_paths = sorted(os.listdir(images_path))
        layers: List[Layer] = []
        for sub_path in sub_paths:
            layer_path = os.path.join(images_path, sub_path)
            layer = Layer(layer_path)
            layers.append(layer)
        return layers

    def generate_image_sequence(self):
        image_path_sequence = []
        for layer in self.layers:
            image_path = layer.get_random_image_path()
            image_path_sequence.append(image_path)
        return image_path_sequence

    def render_image(self, image_path_sequence: List[str]):

        image = Image.new("RGBA", (24, 24), self.background_color)
        for image_path in image_path_sequence:
            layer_image = Image.open(image_path)
            image = Image.alpha_composite(image, layer_image)
        return image

    def save_image(self, image: Image.Image, i: int = 0):
        image_index = str(i).zfill(3) # begin with "000"
        image_file_name = f"{image_index}.png"
        image_save_path = os.path.join(self.output_path, image_file_name)
        image.save(image_save_path)

    def generate(self, n: int = 1):
        print("Processing...")
        for i in range(n):
            image_path_sequence = self.generate_image_sequence()
            image = self.render_image(image_path_sequence)
            self.save_image(image, i)
        print("Done!")

def generate(number):
    generator = Generator("./components")
    generator.generate(number)

# specify the number of items being generated
generate(1000)
