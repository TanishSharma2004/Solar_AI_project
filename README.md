# Solar Rooftop Analyzer

An AI-powered tool that analyzes satellite imagery to assess rooftop solar installation potential, providing comprehensive reports on energy production, costs, and ROI for homeowners and solar professionals.

## Project Overview

This intelligent system leverages computer vision AI to analyze rooftop satellite images and deliver accurate solar potential assessments. Built for the solar industry internship assessment, it demonstrates the integration of multiple AI services to solve real-world solar installation challenges.

### Key Features

- **AI-Powered Analysis**: Uses GPT-4 Vision to analyze rooftop characteristics
- **Comprehensive Reports**: Detailed solar potential, cost analysis, and ROI calculations
- **Financial Modeling**: Installation costs, annual savings, and payback period estimates
- **Environmental Impact**: CO₂ reduction calculations
- **User-Friendly Interface**: Intuitive drag-and-drop image upload
- **Exportable Reports**: Download analysis results in JSON format

##  Technology Stack

- **Frontend**: Streamlit
- **AI Integration**: OpenRouter API (GPT-4 Vision)
- **Image Processing**: PIL (Python Imaging Library)
- **Backend**: Python 3.8+
- **Deployment**: Streamlit Cloud ready

##  Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenRouter API key (https://openrouter.ai)

### Installation

1. **Clone the repository**
   ```bash
   git clone 
   cd solar-rooftop-analyzer
   ```

2. **Create virtual environment**
   ```bash
   
   python -m venv venv
   venv\Scripts\activate


   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENROUTER_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8501`

##  Usage Guide

### Basic Workflow

1. **Upload Image**: Drag and drop a satellite/aerial image of a rooftop
2. **Analyze**: Click "Analyze Solar Potential" button
3. **Review Results**: Get comprehensive solar assessment
4. **Download Report**: Export detailed analysis as JSON

### Best Practices for Images

- **High Resolution**: Use clear, high-quality satellite images
- **Full Roof Coverage**: Ensure the entire rooftop is visible
- **Recent Images**: Use current images for accurate analysis
- **Good Lighting**: Avoid heavily shadowed or cloudy images

### Sample Analysis Output

The tool provides:
- **Suitability Score**: 1-10 rating for solar installation
- **Technical Specs**: Panel capacity, energy production estimates
- **Financial Analysis**: Installation costs, savings, payback period
- **Environmental Impact**: CO₂ reduction calculations
- **Professional Recommendations**: Expert installation advice

##  Project Structure

```
solar-rooftop-analyzer/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not in repo)
├── README.md             # Project documentation
├── examples/             # Sample rooftop images
│   ├── house1.jpg
│   └── house2.jpg
└── docs/                 # Additional documentation
    └── deployment.md
```

##  Technical Implementation

### AI Integration

The system uses OpenRouter's API to access GPT-4 Vision for image analysis:
- **Vision AI**: Analyzes rooftop characteristics, shading, and orientation
- **Structured Output**: Returns JSON-formatted analysis data
- **Error Handling**: Robust error management for API calls

### Solar Calculations

Based on industry standards:
- **Panel Specifications**: 400W panels, 21 sq ft each
- **Installation Costs**: $3-4 per watt
- **Electricity Rates**: $0.13/kWh average
- **System Efficiency**: 20-22% panel efficiency
- **Degradation**: 0.5% annual system degradation

### Key Algorithms

1. **Rooftop Area Estimation**: AI-powered measurement from satellite imagery
2. **Shading Analysis**: Assessment of trees, buildings, and obstacles
3. **Orientation Detection**: Roof direction and tilt analysis
4. **Financial Modeling**: NPV, payback period, and ROI calculations

##  Example Analysis Results

```json
{
  "rooftop_area_sqft": 1200,
  "solar_suitability_score": 8,
  "estimated_panel_capacity_kw": 12.5,
  "annual_energy_production_kwh": 15750,
  "estimated_installation_cost": 37500,
  "annual_savings": 2047,
  "payback_period_years": 18.3,
  "co2_reduction_tons_per_year": 7.9
}
```

## Deployment

### Local Deployment
The app runs locally using Streamlit's built-in server.

### Cloud Deployment (Streamlit Cloud)
1. Push code to GitHub repository
2. Connect to Streamlit Cloud
3. Add environment variables in Streamlit Cloud settings
4. Deploy with one click

### Environment Variables for Deployment
```env
OPENROUTER_API_KEY=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
```

## 🧪 Testing

### Manual Testing
1. Use provided sample images in `/examples` folder
2. Test various rooftop (residential, commercial)
3. Validate AI responses for accuracy

### Sample Test Images
https://www.shutterstock.com/search/aerial-view-flat-roof` - Typical residential rooftop

### Sample Test Results
https://www.loom.com/share/d8b5db944e1741888dc16b72b15a0417?sid=4253ff08-353e-411d-83a1-9a4127faee12

## Future Enhancements

### Planned Features
- **Multiple Image Analysis**: Analyze multiple roof angles
- **3D Modeling**: Generate 3D roof models from satellite data
- **Weather Integration**: Include local weather data in calculations
- **Database Storage**: Store analysis history and user accounts
- **Mobile App**: React Native mobile application
- **API Endpoints**: RESTful API for integration with other systems

### Technical Improvements
- **Caching**: Implement Redis for faster repeat analyses
- **Batch Processing**: Analyze multiple properties simultaneously
- **Machine Learning**: Custom-trained models for better accuracy
- **Real-time Data**: Integration with solar irradiance databases


### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Assessment Criteria Met

### Technical Implementation (80%)
- **AI Integration (40%)**: GPT-4 Vision integration with structured prompts
- **Development Skills (40%)**: Clean Streamlit web interface with proper error handling

### Documentation (20%)
- **Setup Instructions**: Complete installation and deployment guide
- **Implementation Docs**: Technical details and architecture
- **Use Cases**: Example analyses and sample images
- **Future Improvements**: Roadmap for enhancements

### Solar Industry Knowledge
- **Panel Technology**: 400W panel specifications and efficiency calculations
- **Installation Process**: Cost estimation and technical requirements
- **ROI Analysis**: Payback period and financial modeling
- **Industry Standards**: Code compliance and safety considerations

---

**Built for the Solar Industry** | *Empowering renewable energy adoption through AI*
