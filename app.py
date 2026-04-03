YOUR_API_KEYimport streamlit as st
import google.generativeai as genai
from PIL import Image

# ==========================================
# 1. API Configuration
# ==========================================
# Get your API key from Google AI Studio and paste it here
API_KEY = "YOUR_API_KEY" 
genai.configure(api_key=API_KEY)

# Use the Flash model for fast, multimodal responses
model = genai.GenerativeModel('gemini-2.5-flash')

# ==========================================
# 2. Page Setup & UI
# ==========================================
st.set_page_config(page_title="StructurSense AI", layout="wide")

st.title("🌉 StructurSense: The Infrastructure Guardian")
st.markdown("""
Upload an image of a structural element (concrete pillar, steel girder, bridge deck). 
Our Gemini-powered multimodal AI will scan for distress indicators like fatigue cracking, spalling, and corrosion, generating an instant safety report.
""")

# ==========================================
# 3. Image Upload Module
# ==========================================
uploaded_file = st.file_uploader("Upload Inspection Photo (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Infrastructure Photo", use_container_width=True)
    
    # ==========================================
# 4. The Engineering Prompt
# ==========================================
    # This prompt forces Gemini to act as a domain expert
    inspection_prompt = """
    You are an expert structural engineer specializing in Structural Health Monitoring (SHM). 
    Analyze this image of infrastructure and provide a preliminary inspection report.
    
    Format your response exactly with these headers:
    
    ### 1. Visual Observations
    List the specific physical defects visible (e.g., concrete spalling, exposed rebar, steel corrosion, surface cracking, water stains).
    
    ### 2. Severity Assessment
    Rate the visible damage on a scale of Low, Moderate, High, or Critical. Briefly justify this rating based on the visual evidence.
    
    ### 3. Conceptual Damage Index (D)
    Provide an estimated Damage Index score out of 100 based on the formula D = Σ (w * s), where w is the assumed component weight and s is the severity. 
    Just give a reasonable estimated number based on the visual severity.
    
    ### 4. Recommended Action
    Suggest the immediate next steps (e.g., routine monitoring, human-centered manual inspection, immediate closure).
    """

    # ==========================================
# 5. Gemini API Call & Display
# ==========================================
    if st.button("Run AI Structural Analysis"):
        with st.spinner("Analyzing structural integrity..."):
            try:
                # Pass both the prompt and the image to the model
                response = model.generate_content([inspection_prompt, image])
                
                st.success("Analysis Complete!")
                
                # Display the formatted report
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
