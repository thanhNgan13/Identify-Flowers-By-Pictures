
# Flower Recognition Web Application

## Overview

This project is a web application designed to identify 10 different species of flowers. The application uses a Flask API backend and a VGG-16 model for image recognition. Users can upload images of flowers, and the application will predict and display the flower species.

## Flower Species Recognized
- Calla Lily
- Daisy
- Dandelion
- Frangipani
- Hibiscus
- Lotus
- Orchid
- Rose
- Sunflower
- Tulip

## Features

- **Upload Flower Images**: Users can upload images of flowers for identification.
- **AI-Powered Recognition**: The application uses a VGG-16 model to predict the species of the uploaded flower.
- **User-Friendly Interface**: Simple and intuitive web interface for easy navigation and usage.
- **Real-Time Prediction**: Provides instant predictions upon image upload.

## Tech Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning Model**: VGG-16
- **Deployment**: Can be deployed on any server supporting Flask

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)
- Virtual Environment (recommended)

### Setup

1. **Clone the repository**:
    \`\`\`bash
    git clone [https://github.com/your-username/flower-recognition-webapp.git](https://github.com/thanhNgan13/Identify-Flowers-By-Pictures.git)
    cd flower-recognition-webapp
    \`\`\`

2. **Create and activate a virtual environment**:
    \`\`\`bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    \`\`\`

3. **Install dependencies**:
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

4. **Download the VGG-16 model**:
    - Ensure you have the pre-trained VGG-16 model file (`vgg16.h5`). You can download it from Keras or another trusted source and place it in the project directory.

5. **Run the application**:
    \`\`\`bash
    flask run
    \`\`\`

6. **Access the web application**:
    Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. **Home Page**:
    - Provides an interface to upload an image of a flower.
    - ![image](https://github.com/thanhNgan13/Identify-Flowers-By-Pictures/assets/89728233/d9375a9b-d9c0-400f-9556-69f689fe669b)


2. **Upload Image**:
    - Click the "Choose File" button to select an image from your device.
    - Click the "Upload" button to submit the image.
    - ![image](https://github.com/thanhNgan13/Identify-Flowers-By-Pictures/assets/89728233/8123a0a6-b852-4054-bce2-d7627d301206)


3. **Prediction Result**:
    - After uploading, the application will display the predicted flower species along with the uploaded image.


## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgements

- The VGG-16 model used in this project is pre-trained and provided by Keras.
- Special thanks to the open-source community for providing valuable resources and tools.

---
