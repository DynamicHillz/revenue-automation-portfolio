import streamlit as st
import requests
from PIL import Image

# Configure page
st.set_page_config(
    page_title="Revenue Automation Specialist Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional look
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}
.sub-header {
    font-size: 1.5rem;
    color: #666;
    text-align: center;
    margin-bottom: 3rem;
}
.project-card {
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
    background: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.metric-card {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    margin: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<h1 class="main-header">🚀 Revenue Automation Specialist</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">HubSpot + AI + Automation Systems That Drive Business Growth</p>', unsafe_allow_html=True)

# Key metrics row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>85%</h3>
        <p>Faster Lead Processing</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>10+ Hours</h3>
        <p>Weekly Time Savings</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>35%</h3>
        <p>Conversion Improvement</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>$50K+</h3>
        <p>Annual Value Created</p>
    </div>
    """, unsafe_allow_html=True)

# Projects section
st.markdown("## 💼 Featured Projects")

# Project 1: Lead Intelligence
with st.container():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 HubSpot Lead Intelligence System
        **Problem**: Sales teams waste 10+ minutes manually researching and scoring each lead
        
        **Solution**: AI-powered system that automatically:
        - Scores leads based on 15+ data points
        - Enriches contact information 
        - Creates follow-up tasks with personalized recommendations
        - Integrates seamlessly with existing HubSpot workflows
        
        **Results**: 
        - ⚡ 95% reduction in lead qualification time
        - 📈 35% improvement in lead conversion rates
        - 💰 $25,000+ annual productivity savings
        
        **Tech Stack**: HubSpot API, n8n Automation, OpenAI, Streamlit
        """)
    
    with col2:
        if st.button("🔍 View Live Demo", key="demo1"):
            st.markdown("**[Open Lead Intelligence Demo →](https://leadintelligencedemopy.streamlit.app)**")
            st.success("Demo opening in new tab...")
        
        st.markdown("**Key Features:**")
        st.markdown("✅ Real-time lead scoring")
        st.markdown("✅ AI-powered insights")
        st.markdown("✅ HubSpot integration")
        st.markdown("✅ Automated workflows")

st.markdown("---")

# Project 2: Customer Success RAG
with st.container():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🤖 Customer Success RAG System
        **Problem**: Support teams can't quickly access customer context across multiple systems
        
        **Solution**: AI-powered knowledge system that:
        - Searches customer history, support tickets, and documentation instantly
        - Provides contextual responses with source citations
        - Integrates customer data from HubSpot with company knowledge base
        - Reduces response time from hours to seconds
        
        **Results**:
        - ⚡ 80% faster issue resolution
        - 📊 92% improvement in first-contact resolution
        - 😊 4.8/5 customer satisfaction score
        
        **Tech Stack**: RAG Architecture, LangChain, Vector Database, HubSpot API
        """)
    
    with col2:
        if st.button("🔍 View Live Demo", key="demo2"):
            st.markdown("**[Open Customer Success RAG Demo →](https://customersuccessragpy.streamlit.app)**")
            st.success("Demo opening in new tab...")
        
        st.markdown("**Key Features:**")
        st.markdown("✅ Intelligent document search")
        st.markdown("✅ Customer context integration")
        st.markdown("✅ AI-powered responses")
        st.markdown("✅ Source attribution")

st.markdown("---")

# Project 3: Revenue Operations Dashboard
with st.container():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📊 Revenue Operations Dashboard
        **Problem**: Executives spend hours compiling revenue reports from multiple systems
        
        **Solution**: Automated intelligence platform that:
        - Connects HubSpot, Google Sheets, and business systems
        - Provides real-time pipeline health monitoring
        - Generates AI-powered business insights and recommendations
        - Automates executive reporting and alerts
        
        **Results**:
        - ⏰ 12+ hours saved weekly on reporting
        - 📈 25% improvement in pipeline visibility
        - 🎯 Earlier identification of revenue risks
        
        **Tech Stack**: n8n Automation, HubSpot API, AI Analytics, Interactive Dashboards
        """)
    
    with col2:
        if st.button("🔍 View Live Demo", key="demo3"):
            st.markdown("**[Open Revenue Dashboard Demo →](https://revenuedashboardpy.streamlit.app/)**")
            st.success("Demo opening in new tab...")
        
        st.markdown("**Key Features:**")
        st.markdown("✅ Real-time revenue metrics")
        st.markdown("✅ Predictive analytics")
        st.markdown("✅ Executive dashboards")
        st.markdown("✅ Automated reporting")

# Technical skills section
st.markdown("---")
st.markdown("## 🛠️ Technical Expertise")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Revenue Operations**
    - HubSpot Administration & API
    - Sales Process Automation  
    - Pipeline Management
    - Lead Scoring & Routing
    - Revenue Analytics
    """)

with col2:
    st.markdown("""
    **AI & Automation**
    - n8n Workflow Automation
    - OpenAI API Integration
    - RAG System Architecture
    - LangChain Implementation
    - Vector Databases
    """)

with col3:
    st.markdown("""
    **Data & Analytics**
    - Business Intelligence
    - Predictive Analytics
    - Custom Dashboard Development
    - API Integrations
    - Process Optimization
    """)

# Contact and value proposition
st.markdown("---")
st.markdown("## 🎯 Ready to Automate Your Revenue Operations?")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    I specialize in building intelligent automation systems that connect HubSpot, AI, and business processes 
    to drive measurable revenue growth.
    
    **What I Bring:**
    - 🎯 Deep understanding of revenue operations challenges
    - 🤖 Cutting-edge AI and automation expertise
    - 📊 Focus on measurable business outcomes
    - ⚡ Rapid implementation and deployment
    
    **Ideal For:**
    - Revenue Operations Manager roles
    - Marketing Operations positions  
    - Business Systems Analyst opportunities
    - Sales Operations coordinator roles
    """)

with col2:
    st.markdown("### 📞 Let's Connect")
    
    if st.button("📧 Schedule Interview", key="contact"):
        st.success("Great! Please reach out via LinkedIn or email to schedule.")
    
    st.markdown("""
    **Contact Information:**
    - 💼 LinkedIn: www.linkedin.com/in/hillary-amalokwu
    - 📧 Email: amalokwuu@gmail.com
    - 💻 GitHub: https://github.com/DynamicHillz/revenue-automation-portfolio.git
    - 🌐 Portfolio: This site!
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>Built with HubSpot API, n8n Automation, OpenAI, and Streamlit</p>
    <p>© 2024 Revenue Automation Specialist Portfolio</p>
</div>

""", unsafe_allow_html=True)

