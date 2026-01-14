import fitz  # PyMuPDF
import os

pdf_path = ""
output_dir =  "extracted_images"

os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
img_count = 0

for page_index in range(len(doc)):
    page = doc[page_index]
    images = page.get_images(full=True)
    
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        img_count += 1
        image_filename = f"image_{img_count}.{image_ext}"

        with open(os.path.join(output_dir, image_filename), "wb") as f:
            f.write(image_bytes)
            
print(f"✅ Extracted {img_count} images successfully!")