import docx
import os

# Load the document
doc = docx.Document('Untrust attribution Debug.docx')

# Create images directory if not exists
if not os.path.exists('images'):
    os.makedirs('images')

# Extract and save all images first
image_rels = []
for rel in doc.part.rels.values():
    if "image" in rel.reltype:
        image_rels.append(rel)

# Save images
for i, rel in enumerate(image_rels, 1):
    img_name = f"image_{i}.png"
    with open(f"images/{img_name}", "wb") as f:
        f.write(rel.target_part.blob)

# Now, create markdown content with inline images
md_content = "# Debugging Report\n\n"

image_index = 0
for para in doc.paragraphs:
    para_md = ""
    for run in para.runs:
        para_md += run.text
        # Check for inline images
        drawings = run._element.xpath('.//w:drawing')
        if drawings:
            image_index += 1
            img_name = f"image_{image_index}.png"
            para_md += f"\n\n![Image {image_index}](images/{img_name})\n\n"
    if para_md.strip():
        md_content += para_md + "\n\n"

# Write to new md file
with open('debug_report_proper.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("Extraction complete with proper image placement. Markdown file: debug_report_proper.md")