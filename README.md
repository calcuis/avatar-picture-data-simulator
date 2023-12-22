## avatar data simulator

Generate 10,000 samples for ai-picture-model-trainer : P

This Python code defines an image generator using the Pillow library (PIL). The generator creates composite images by sequentially selecting a random image from each layer and combining them.

Here's an explanation of the code:

Layer Class:
- The Layer class represents a layer in the image generation process, associated with a directory containing images.
- `__init__(self, path: str)`: initializes a layer with a given path.
- `get_random_image_path(self)`: returns a randomly selected image path from the layer's directory.

Generator Class:
- The Generator class manages the image generation process.
- `__init__(self, images_path: str)`: initializes the generator with a base path for the layers, sets the background color to None, defines the output path for generated images as "./data," and creates the output - directory if it doesn't exist. It also loads the layers from the specified images_path during initialization.
- load_image_layers(self, images_path: str): loads and returns a list of Layer objects based on subdirectories in the specified images_path.
- `generate_image_sequence(self)`: generates a sequence of image paths by sequentially selecting a random image from each layer.
- `render_image(self, image_path_sequence: List[str])`: creates a composite image by alpha-compositing the images from the generated sequence onto a blank canvas. The canvas size is 24x24 pixels.
- `save_image(self, image: Image.Image, i: int = 0)`: saves the generated image with a filename based on the iteration index.
- `generate(self, n: int = 1)`: initiates the image generation process. It generates a sequence of images for each iteration, renders the composite image, and saves it. The number of iterations is specified by the parameter n, with a default value of 1.

`generate` Function:
- The generate function is defined outside the classes and serves as a convenient way to create a Generator instance and generate a specified number of images (1000 in this case) from the layers located in the "./components" directory.
- 
Script Execution:
- The script concludes by calling generate(1000), which triggers the generation of 1000 composite images; the number of generation is editable.

The code assumes that each subdirectory in "./components" represents a separate layer, and images within each layer directory are combined to create the final composite image. The generated images are saved in the "./data" directory.

**Reference**

github.com/pixegami/pixel-punk-avatars
