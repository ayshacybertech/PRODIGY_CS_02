# Navigate to your project directory
cd /path/to/your/PRODIGY_CS_02  # Replace with your actual path

# Create the README file
touch README.md

# Open the README file in a text editor (you can use nano, vim, or any editor you prefer)
nano README.md  # or use vim, code (VS Code), etc.

# Add the following content in the README.md file:

# Image Encryption Tool

# This project is a simple image encryption tool that uses pixel manipulation techniques.

# Features

# - Load and manipulate image pixels
# - Swap pixels for encryption
# - Apply basic mathematical operations (e.g., XOR) to pixel values
# - Decrypt images back to their original form

# Requirements

# - Python 3.x
# - Pillow library

# Installation

# 1. Clone this repository:
#    ```bash
#    git clone https://github.com/ayshacybertech/PRODIGY_CS_02.git
#    ```

# 2. Navigate to the project directory:
#    ```bash
#    cd PRODIGY_CS_02
#    ```

# 3. Install the required libraries:
#    ```bash
#    pip install Pillow
#    ```

# Usage

# To encrypt an image, run the following command in your terminal:
# ```bash
# python image_encryption.py
# ```

# Make sure to provide the necessary input image as specified in the script.

# Contributing

# Feel free to submit issues or pull requests if you'd like to contribute to this project.

# License

# This project is licensed under the MIT License.

# Save and exit the editor (For nano, press Ctrl + X, then Y, then Enter)

# Stage and commit the changes
git add README.md
git commit -m "Add README file"

# Push the changes to GitHub
git push -u origin master
