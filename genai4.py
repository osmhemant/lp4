from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import matplotlib.pyplot as plt

# Load your image
image_path = "C:/Users/heman/OneDrive/Desktop/icsgenai/content.jpg"
image = Image.open(image_path).convert("RGB")

# Load model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Process the image
inputs = processor(images=image, return_tensors="pt").to(device)

# Generate caption
out = model.generate(**inputs, max_length=50)
caption = processor.decode(out[0], skip_special_tokens=True)

# Show result
print("📝 Generated Caption:", caption)
plt.imshow(image)
plt.title(caption)
plt.axis("off")
plt.show()
