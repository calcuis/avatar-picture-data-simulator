## avatar data simulator

Generate 10,000 samples for ai-picture-model-trainer (not a good idea though) : P

The provided Python code defines a simple avatar generator using image layers. The generator creates avatars by combining different image layers randomly, each represented by a Layer class. The layers have a specified rarity, and whether a layer should be included in the avatar is determined by a random probability based on this rarity.
Here's a breakdown of the code:

Layer Class:
- Represents an individual image layer.
- Initialized with a path to a directory containing images for the layer and a default rarity of 1.0.
- Provides a method `get_random_image_path` to select a random image from the layer.
- Defines a method `should_generate` to determine whether the layer should be included based on its rarity.

AvatarGenerator Class:
- Manages the generation of avatars using multiple layers.
- Initialized with the path to a directory containing subdirectories, each representing a layer.
- Loads layers from subdirectories, setting custom rarities for specific layers.
- Provides a method generate_image_sequence to create a sequence of image paths for the avatar.
- Uses the PIL library to composite the images and create the final avatar.
- Saves the generated avatar images to an output directory.

Overall, the code is a basic implementation of an avatar generator that combines different image layers to create diverse avatars. The rarities assigned to layers control the likelihood of specific layers being included in the final avatar, adding variability to the generated images. The generated avatars are then saved in the "./output" directory.

**Reference**

github.com/pixegami/pixel-punk-avatars
