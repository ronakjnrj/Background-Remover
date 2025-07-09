    from rembg import remove
    from PIL import Image
    input_path = 'path/to/your/input_image.png'  # Replace with your image path
    output_path = 'path/to/your/output_image.png' # Replace with your desired output path

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input_image_data = i.read()
            output_image_data = remove(input_image_data)
            o.write(output_image_data)
