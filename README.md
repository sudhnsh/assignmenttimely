# Assignment Submission - TimelyAI

The assignment required the recreation of a specific template using the Python Pillow library. Here's a summary of the task and how to run the provided code.

## Task Description

The task was to create an output template using Pillow in Python, based on the provided input:

- **Input**: Image file, brand name (text), and service name (text)
- **Output**: The specified template

## How to Run the Code

Follow these steps to run the code:

1. **Clone the Repository**:

```bash
git clone https://github.com/sudhnsh/assignmenttimely
```

2. **Edit Input Data**:

Modify the information in the `inputdata.py` file according to your preferences. This file contains the following parameters:

- `text1`: Brand name (text)
- `text2`: Service name (text)
- `imagepath`: Path to the image file
- `font`: Choose from two available fonts for text rendering.

3. **Install Requirements**:

Use the following command to install all the necessary requirements:

```bash
pip install -r requirement.txt 
```

4. **Generate the Output**:

To generate the output file, execute one of the following commands:

```bash
python main.py
```
OR

```bash
python3 main.py
```

## Methodology

The code follows this methodology:

1. It starts with fixing the ratio of the image and fixing the image size as 1080x1080 
2. Then, adding a gray rectangle to the image.
3. Then, it adds the provided image to the template.
4. The brand name (text1) is added.
5. Finally, the service name (text2) is added to the template. The font size adjusts based on the length of the text.

Please note that this code is designed to create a template based on the provided input, including brand and service names, and is implemented in Python using the Pillow library.

