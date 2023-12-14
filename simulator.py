import os, random
from typing import List
from PIL import Image

class Layer:
    def __init__(self, path: str):
        self.path = path
        self.rarity: float = 1.0

    def get_random_image_path(self):
        image_file_names = os.listdir(self.path)
        random_image_file_name = random.choice(image_file_names)
        return os.path.join(self.path, random_image_file_name)

    def should_generate(self) -> bool:
        return random.random() < self.rarity

class AvatarGenerator:
    def __init__(self, images_path: str):
        self.layers: List[Layer] = self.load_image_layers(images_path)
        self.background_color = (None)
        self.output_path: str = "./output"
        os.makedirs(self.output_path, exist_ok=True)

    def load_image_layers(self, images_path: str):
        sub_paths = sorted(os.listdir(images_path))
        layers: List[Layer] = []
        for sub_path in sub_paths:
            layer_path = os.path.join(images_path, sub_path)
            layer = Layer(layer_path)
            layers.append(layer)
        layers[2].rarity = 0.80
        layers[3].rarity = 0.15
        return layers

    def generate_image_sequence(self):
        image_path_sequence = []
        for layer in self.layers:
            if layer.should_generate():
                image_path = layer.get_random_image_path()
                image_path_sequence.append(image_path)
        return image_path_sequence

    def render_avatar_image(self, image_path_sequence: List[str]):

        image = Image.new("RGBA", (24, 24), self.background_color)
        for image_path in image_path_sequence:
            layer_image = Image.open(image_path)
            image = Image.alpha_composite(image, layer_image)
        return image

    def save_image(self, image: Image.Image, i: int = 0):
        image_index = str(i).zfill(4)
        image_file_name = f"punk{image_index}.png"
        image_save_path = os.path.join(self.output_path, image_file_name)
        image.save(image_save_path)

    def generate_avatar(self, n: int = 1):
        print("Processing...")
        for i in range(n):
            image_path_sequence = self.generate_image_sequence()
            image = self.render_avatar_image(image_path_sequence)
            self.save_image(image, i)
        print("Done!")

def generate_avatar(number):
    generator = AvatarGenerator("./components")
    generator.generate_avatar(number)

generate_avatar(10000) # sample size = 10k
