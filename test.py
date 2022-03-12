import io
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="django-image-search-f9ff8c0300dc.json"

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('ImageSearcher/uploads/81e6d95007f541d9bbc1c1d1f9636c5b.jpeg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = [label.description for label in response.label_annotations]
print(labels)

text = client.text_detection(image=image)
texts = text.text_annotations
text = [i.description.strip() for i in texts]
text = ' '.join(text)
print(text)

safe = client.safe_search_detection(image=image)
safety = [type(safe)]

#print(safe)