import os
import yaml
import json
import markdown2
import pdfkit 
from jinja2 import Environment, FileSystemLoader
from ai_assistant import generate_summary


# === 1. Helper: Extract Metadata ===
def extract_metadata(openapi_data):
    api_info = {
        "title": openapi_data["info"].get("title", "Untitled API"),
        "version": openapi_data["info"].get("version", ""),
        "paths": []
    }

    for path, methods in openapi_data.get("paths", {}).items():
        for method, details in methods.items():
            # Use existing summary or generate one with AI
            summary = details.get("summary", "").strip()
            if not summary:
                summary = generate_summary(path, method, details.get("parameters", []))

            endpoint = {
                "path": path,
                "method": method.upper(),
                "summary": summary,
                "parameters": details.get("parameters", []),
                "responses": details.get("responses", {})
            }
            api_info["paths"].append(endpoint)

    return api_info

# === 2. Render HTML ===
def render_html(metadata, output_path):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('doc_template.html')
    output = template.render(metadata)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

# === 3. Convert HTML to Markdown ===
def render_markdown(html_path, md_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    markdown = markdown2.markdown(html_content)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown)

# === 4. Convert HTML to PDF ===
def render_pdf(html_path, pdf_path):
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_file(html_path, pdf_path, configuration=config)

# === 5. Main Processing ===
def process_openapi_file(filepath):
    print(f"Processing: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        if filepath.endswith('.json'):
            openapi_data = json.load(f)
        else:
            openapi_data = yaml.safe_load(f)

    metadata = extract_metadata(openapi_data)

    filename = os.path.splitext(os.path.basename(filepath))[0]
    html_path = f'generated_docs/{filename}_doc.html'
    md_path = f'generated_docs/{filename}_doc.md'
    pdf_path = f'generated_docs/{filename}_doc.pdf'

    render_html(metadata, html_path)
    render_markdown(html_path, md_path)
    render_pdf(html_path, pdf_path)

    print(f"✅ Documentation for {filename} generated.\n")

# === 6. Batch Loop for All Files ===
def generate_all_docs():
    input_dir = 'openapi_files'
    os.makedirs('generated_docs', exist_ok=True)

    for file in os.listdir(input_dir):
        if file.endswith('.yaml') or file.endswith('.yml') or file.endswith('.json'):
            filepath = os.path.join(input_dir, file)
            process_openapi_file(filepath)

# === Entry Point ===
if __name__ == "__main__":
    generate_all_docs()
