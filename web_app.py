import streamlit as st
import os
import shutil
from main import process_openapi_file

import os
import streamlit as st
from dotenv import load_dotenv

# Load from .env if running locally
load_dotenv()

# Try to get from Streamlit Cloud secrets
try:
    os.environ["OPENROUTER_API_KEY"] = st.secrets["OPENROUTER_API_KEY"]
except Exception:
    # This is expected when running locally — no secrets.toml
    pass





st.set_page_config(page_title="AI API Doc Generator", layout="centered")

st.title("🤖 AI-Powered API Documentation Generator")
st.markdown("Upload an OpenAPI `.yaml`, `.yml`, or `.json` file and get complete docs with AI-generated summaries.")

# ⚠️ Free version notice
st.markdown(
    """
    <div style='border: 1px solid red; padding: 10px; margin: 20px 0; background-color: #black;'>
        <strong>⚠️ Notice:</strong> This is a <em>free version</em> of the API documentation generator.<br>
        It only supports limited AI summarization due to usage limits.<br>
        For large-scale or custom documentation solutions, please <strong>contact the developer</strong>.
    </div>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Choose your OpenAPI file", type=["yaml", "yml", "json"])

if uploaded_file:
    filename = uploaded_file.name
    input_path = os.path.join("openapi_files", filename)

    # Save uploaded file
    os.makedirs("openapi_files", exist_ok=True)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Generate Documentation"):
        with st.spinner("Generating documentation with AI..."):
            process_openapi_file(input_path)

        base_name = os.path.splitext(filename)[0]
        html_path = f"generated_docs/{base_name}_doc.html"
        md_path = f"generated_docs/{base_name}_doc.md"
        pdf_path = f"generated_docs/{base_name}_doc.pdf"

        st.success("✅ Documentation generated!")

        st.markdown("### 📄 Download Your Documentation:")
        st.download_button("⬇️ HTML", open(html_path, "rb"), file_name=html_path)
        st.download_button("⬇️ Markdown", open(md_path, "rb"), file_name=md_path)
        st.download_button("⬇️ PDF", open(pdf_path, "rb"), file_name=pdf_path)
