## Python Image Background Remover
A simple yet effective Python script to remove backgrounds from images using popular image processing libraries. This tool is perfect for quickly isolating subjects in photos for various applications like e-commerce, graphic design, or personal projects.

### ✨ Features<br>
Automated Background Removal: Intelligently identifies and removes the background from an image.
Supports Common Image Formats: Works with JPG, PNG, WEBP, and more.
Customizable Output: Save the processed image with a transparent background (PNG).
Easy to Use: Command-line interface for straightforward operation. 
Lightweight: Built with commonly used Python libraries.<br> 
 
### 🚀 Installation
To get started with the Python Image Background Remover, follow these steps:

#### Clone the repository: 
```bash
git clone https://github.com/yourusername/python-image-background-remover.git
cd python-image-background-remover
``` 
#### Create a virtual environment (recommended):
```bash
python -m venv venv
```
#### Activate the virtual environment:

#### On Windows:
```bash
.\venv\Scripts\activate
````
#### On macOS/Linux:
```bash
source venv/bin/activate
```
#### Install the required dependencies:
```bash
pip install rembg
```
### 💡 Usage

After installation, you can use the script from your terminal.
```bash
python main.py --input <input_image_path> --output <output_image_path>
```
#### Example:

To remove the background from my_photo.jpg and save it as my_photo_no_bg.png:
```bash
python main.py --input images/my_photo.jpg --output output/my_photo_no_bg.png
```
#### Command-line Arguments:

```--input or -i:``` (Required) Path to the input image file.

```--output or -o:``` (Required) Path where the output image with the removed background will be saved. Ensure the output path has a .png extension for transparency.
<br>
### 📦 Dependencies
The project relies on the following Python libraries, which are listed in ```requirements.txt:```

#### Pillow (PIL Fork): For image opening, manipulation, and saving.

#### rembg: A powerful library for background removal.<br>

### 🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

Fork the repository.

Create a new branch ```(git checkout -b feature/YourFeature).```

Make your changes.

Commit your changes ```(git commit -m 'Add some feature').```

Push to the branch ```git push origin feature/YourFeature).```

Open a Pull Request.<br>

### 📄 License
This project is licensed under the MIT License - see the ```LICENSE``` file for details.



Project Link: https://github.com/yourusername/python-image-background-remover
