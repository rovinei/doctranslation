from google.cloud import vision
from google.oauth2 import service_account

class GoogleCloudVisionOCRService:

    def __init__(self, service_account_key_file):
        self.service_account_key_file = service_account_key_file
        self.client = self._initialize_client()

    def _initialize_client(self):
        credentials = service_account.Credentials.from_service_account_file(self.service_account_key_file)
        client = vision.ImageAnnotatorClient(credentials=credentials)
        return client

    def perform_ocr(self, image_path):
        # Read the image file
        with open(image_path, 'rb') as image_file:
            content = image_file.read()

        # Construct the image object
        image = vision.Image(content=content)

        # Perform text detection
        response = self.client.text_detection(image=image)
        texts = response.text_annotations

        if response.error.message:
            raise Exception(f'{response.error.message}')

        # Extract detected text
        detected_texts = []
        for text in texts:
            detected_texts.append(text.description)

        return detected_texts
