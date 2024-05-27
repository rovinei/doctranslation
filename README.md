## Prerequistite
#### Create python environment
Create a python virtual environtment with Python version 3.11.9.
`pyenv` is recommended.

#### Setup project
Run this command `make init`
Please read through `Makefile` to understand the process

## Management console CLI command example
```
python manage.py translate_document \
 --document-path=/Users/vinei/Projects/Utility/docTranslation/media/test.pptx \
 --target-language=en-US \
--source-language=fr-FR
```