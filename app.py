import streamlit as st
import base64
import json
import os
from PIL import Image
from openai import OpenAI
from dotenv import load_dotenv
import io

# Load environment variables
load_dotenv()

# Initialize OpenRouter client
@st.cache_resource
def init_openrouter_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )

def image_to_base64(image):
    """Convert PIL image to base64 string"""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

def get_solar_analysis_prompt():
    """Return the solar analysis prompt for AI"""
    return """
    You are a solar energy expert analyzing a rooftop satellite/aerial image for solar panel installation potential.
    
    Analyze the image and provide a basic assessment in the following JSON format:
    
    {
        "rooftop_area_sqft": <estimated usable rooftop area in square feet>,
        "solar_suitability_score": <score from 1-10, where 10 is excellent>,
        "roof_orientation": "<primary roof direction: North/South/East/West>",
        "estimated_panel_capacity_kw": <total solar capacity in kilowatts>,
        "annual_energy_production_kwh": <estimated annual energy production>,
        "estimated_installation_cost": <rough cost estimate in USD>,
        "annual_savings": <estimated annual electricity bill savings>,
        "payback_period_years": <estimated payback period>,
        "key_observations": [
            "<observation 1>",
            "<observation 2>"
        ],
        "recommendations": [
            "<recommendation 1>",
            "<recommendation 2>"
        ]
    }
    
    Base your analysis on these solar industry standards:
    - Average solar panel: 400W, 21 sq ft
    - Typical installation cost: $3-4 per watt
    - Average electricity rate: $0.13/kWh
    - Solar panel efficiency: 20-22%
    - Useful roof area: 60-70% of total roof area
    
    Only return the JSON, no additional text.
    """

def analyze_rooftop_with_ai(image):
    """Analyze rooftop image using AI vision"""
    try:
        client = init_openrouter_client()
        
        # Convert image to base64
        image_base64 = image_to_base64(image)
        
        # Make API call
        response = client.chat.completions.create(
            model="anthropic/claude-3.5-sonnet",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": get_solar_analysis_prompt()},
                        {
                            "type": "image_url", 
                            "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}
                        }
                    ]
                }
            ],
            max_tokens=1500,
            temperature=0.1
        )
        
        # Parse JSON response
        analysis_text = response.choices[0].message.content
        
        # Try to extract JSON from response
        try:
            # Find JSON in the response
            start_idx = analysis_text.find('{')
            end_idx = analysis_text.rfind('}') + 1
            json_str = analysis_text[start_idx:end_idx]
            analysis = json.loads(json_str)
            return analysis, None
        except json.JSONDecodeError:
            return None, f"Could not parse AI response as JSON: {analysis_text}"
            
    except Exception as e:
        return None, f"Error analyzing image: {str(e)}"

def display_analysis_results(analysis):
    """Display the analysis results in a formatted way"""
    
    # Main metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Suitability Score", f"{analysis['solar_suitability_score']}/10")
    
    with col2:
        st.metric("Panel Capacity", f"{analysis['estimated_panel_capacity_kw']} kW")
    
    with col3:
        st.metric("Annual Production", f"{analysis['annual_energy_production_kwh']:,} kWh")
    
    with col4:
        st.metric("Payback Period", f"{analysis['payback_period_years']} years")
    
    st.divider()
    
    # Financial Analysis
    st.subheader("💰 Financial Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Installation Cost", f"${analysis['estimated_installation_cost']:,}")
    
    with col2:
        st.metric("Annual Savings", f"${analysis['annual_savings']:,}")
    
    # Technical Details
    st.subheader("🔧 Technical Details")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Rooftop Area:** {analysis['rooftop_area_sqft']:,} sq ft")
    
    with col2:
        st.write(f"**Roof Orientation:** {analysis['roof_orientation']}")
    
    # Key Observations
    st.subheader("👁️ Key Observations")
    for i, observation in enumerate(analysis['key_observations'], 1):
        st.write(f"{i}. {observation}")
    
    # Recommendations
    st.subheader("💡 Recommendations")
    for i, recommendation in enumerate(analysis['recommendations'], 1):
        st.write(f"{i}. {recommendation}")

# Streamlit App
def main():
    st.set_page_config(
        page_title="Solar Rooftop Analyzer",
        page_icon="☀️",
        layout="wide"
    )
    
    st.title("☀️ Solar Rooftop Analyzer")
    st.markdown("Upload a satellite or aerial image of a rooftop to get a comprehensive solar installation analysis.")
    
    # Sidebar for instructions
    with st.sidebar:
        st.header("📋 Instructions")
        st.write("""
        1. Upload a clear aerial/satellite image of a rooftop
        2. Wait for AI analysis (may take 30-60 seconds)
        3. Review the solar potential assessment
        4. Download the report for future reference
        
        **Best Image Tips:**
        - High resolution images work best
        - Clear view of the entire roof
        - Minimal cloud coverage
        - Recent images preferred
        """)
    
    # Main upload area
    uploaded_file = st.file_uploader(
        "Choose a rooftop image...", 
        type=['jpg', 'jpeg', 'png']
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📸 Uploaded Image")
            st.image(image, caption='Rooftop Image for Analysis', use_container_width=True)
        
        with col2:
            st.subheader("🔍 Analysis")
            
            if st.button("Analyze Solar Potential", type="primary"):
                with st.spinner("Analyzing rooftop for solar potential... This may take a minute."):
                    analysis, error = analyze_rooftop_with_ai(image)
                    
                    if error:
                        st.error(f"Analysis failed: {error}")
                        st.info("Please check your OpenRouter API key and try again.")
                    else:
                        st.success("Analysis complete!")
                        
                        # Store analysis in session state
                        st.session_state.analysis = analysis
        
        # Display results if available
        if 'analysis' in st.session_state:
            st.divider()
            st.header("📊 Solar Analysis Results")
            display_analysis_results(st.session_state.analysis)
            
            # Download report option
            st.divider()
            if st.button("📄 Download Report"):
                report_json = json.dumps(st.session_state.analysis, indent=2)
                st.download_button(
                    label="Download JSON Report",
                    data=report_json,
                    file_name="solar_analysis_report.json",
                    mime="application/json"
                )
    
    # Footer
    st.divider()
    st.markdown("---")
    st.markdown("**Solar Rooftop Analyzer** - Built with Streamlit and AI Vision Technology")

if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENROUTER_API_KEY"):
        st.error("Please set your OPENROUTER_API_KEY in the .env file")
        st.stop()
    
    main()