# Objecttive
Translation pptx document into various languages

# Flows
- Upload pptx document
- Extract document pages's compoents
- Identify each component / extract content (text, image, etc)
- Copy/Save each component format
- Translate the text content / update the document with translated text / applying the saved format of the component
- Use OCR to extract text from image / translate the text / embebded translated text on image
- Return the translated document

# Technologies and Libraries
### Translation
- Google translate
- Deepl

### OCR
#### Libraries
- Tesseract OCR:
    Description: An open-source OCR engine originally developed by HP and now maintained by Google.
    Strengths: Highly accurate for printed text, supports multiple languages, and customizable.
- EasyOCR:
    Description: A Python package that supports 40+ languages and provides easy-to-use OCR capabilities.
    Strengths: Excellent for multi-language support, good for complex scripts, and easy to use.
- OCRmyPDF:
    Description: Adds OCR text layers to PDF files.
    Strengths: Ideal for PDF documents, integrates well with Tesseract, and supports multiple languages.

#### API Services
- Google Cloud Vision API:
    Description: A comprehensive image analysis API that includes OCR capabilities.
    Strengths: High accuracy, supports many languages, and can handle complex documents.
- Amazon Textract:
    Description: Extracts text, forms, and tables from scanned documents.
    Strengths: Accurate, handles complex documents, and integrates well with other AWS services.
 - Microsoft Azure Computer Vision:
    Description: Provides OCR capabilities as part of Azure Cognitive Services.
    Strengths: High accuracy, supports many languages, and integrates well with other Azure services.

### PPTX document manipulation
- python-pptx:
    Description: A Python library for creating and updating PowerPoint (.pptx) files.
    Features: Supports adding slides, shapes, images, tables, and charts. It also allows you to modify text, styles, and formatting.
- PPTX-Template:
    Description: A small library built on top of python-pptx to handle templating with PowerPoint files.
    Features: Allows creating PowerPoint presentations using template-based approaches.
- Aspose.Slides for Python via .NET:
    Description: A powerful library for creating and manipulating PowerPoint files. It supports a wide range of features, including advanced formatting and complex objects.
    Features: Extensive capabilities for manipulating slides, shapes, text, images, charts, tables, and more.
- pptx2pdf:
    Description: A utility to convert PowerPoint presentations to PDF using python-pptx.
    Features: Simplifies the process of converting `.pptx` files to `.pdf`.

### Backend & Frontend
- Django & Django Rest Framework
- Flask
- ExpressJS, NodeJS
- VueJS & Axios




