import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(page_title="Digital Wellbeing", layout="wide")

st.title("Digital Wellbeing Analytics")
st.markdown("### How social media affects mental health")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/tiktok_instagram_global_100countries.csv')

@st.cache_resource
def load_model():
    return joblib.load('models/addiction_model.pkl')

try:
    df = load_data()
    model = load_model()
    st.success("Data loaded successfully")
except:
    st.error("Error loading data or model")
    st.stop()

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    countries = st.multiselect("Select countries", df['country'].unique(), default=df['country'].unique()[:5])
    years = st.slider("Year range", int(df['year'].min()), int(df['year'].max()), (2015, 2030))

    st.divider()
    
    st.markdown("**Author:** [Scotzz](https://github.com/scotzz)")
    st.markdown("**Data source:** [Kaggle Dataset](https://www.kaggle.com/datasets/abdulmaliklodhra/tiktok-and-instagram-addiction-dataset-20152060)")
# Filter data
filtered_df = df[(df['country'].isin(countries)) & (df['year'].between(years[0], years[1]))]

# Tabs
tab1, tab2, tab3 = st.tabs(["Overview", "Charts", "Predict"])

with tab1:
    st.subheader("Key Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("TikTok", f"{filtered_df['tiktok_minutes_daily'].mean():.0f} min/day")
    col2.metric("Instagram", f"{filtered_df['instagram_minutes_daily'].mean():.0f} min/day")
    col3.metric("Sleep", f"{filtered_df['sleep_hours'].mean():.1f} hours/day")
    col4.metric("Addiction", f"{filtered_df['addiction_score'].mean():.1f} / 100")
    
    st.divider()
    
    st.info("**Insight:** More screen time correlates with worse sleep and higher addiction scores")

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Screen Time by Country")
        screen_by_country = filtered_df.groupby('country')[['tiktok_minutes_daily', 'instagram_minutes_daily']].mean().reset_index()
        fig1 = px.bar(screen_by_country, x='country', y=['tiktok_minutes_daily', 'instagram_minutes_daily'], 
                      barmode='group', title="Minutes per day")
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Top 10 Countries by Addiction")
        addiction_top = filtered_df.groupby('country')['addiction_score'].mean().reset_index().sort_values('addiction_score', ascending=False).head(10)
        fig2 = px.bar(addiction_top, x='addiction_score', y='country', orientation='h', title="Addiction Score")
        st.plotly_chart(fig2, use_container_width=True)
    
    st.subheader("Trends Over Time")
    yearly = filtered_df.groupby('year')[['tiktok_minutes_daily', 'instagram_minutes_daily', 'addiction_score']].mean().reset_index()
    fig3 = px.line(yearly, x='year', y=['tiktok_minutes_daily', 'instagram_minutes_daily', 'addiction_score'], 
                   markers=True, title="Changes over years")
    st.plotly_chart(fig3, use_container_width=True)
    
    st.subheader("Correlation Matrix")
    corr_cols = ['tiktok_minutes_daily', 'instagram_minutes_daily', 'sleep_hours', 'addiction_score']
    fig4 = px.imshow(filtered_df[corr_cols].corr(), text_auto=True, color_continuous_scale='RdBu', aspect='auto')
    st.plotly_chart(fig4, use_container_width=True)

with tab3:
    st.subheader("Predict Addiction Level")
    st.markdown("Enter your daily digital habits to get a personalized addiction risk score.")

    col1, col2 = st.columns(2)
    
    with col1:
        tiktok_input = st.number_input("📱 TikTok (min/day)", min_value=0, max_value=500, value=120, help="Average minutes spent on TikTok per day")
        instagram_input = st.number_input("📸 Instagram (min/day)", min_value=0, max_value=500, value=90, help="Average minutes spent on Instagram per day")
    
    with col2:
        sleep_input = st.number_input("Sleep (hours/day)", min_value=0.0, max_value=24.0, value=7.0, help="Average hours of sleep per night")
        
        # ASI с подробным объяснением
        st.markdown("""
        <details>
            <summary> What is ASI (Anxiety Sensitivity Index)?</summary>
            <br>
            <b>ASI measures how afraid you are of anxiety symptoms</b> (racing heart, sweating, shortness of breath).<br><br>
            <b>How to estimate your ASI (0-100):</b><br>
            • 0-20: You don't fear anxiety at all<br>
            • 21-40: You sometimes worry about anxiety symptoms<br>
            • 41-60: You moderately fear anxiety symptoms<br>
            • 61-80: You strongly fear anxiety symptoms<br>
            • 81-100: You are terrified of anxiety symptoms<br><br>
            <i>Example: If your heart races and you think "I'm having a heart attack" → high ASI</i>
        </details>
        """, unsafe_allow_html=True)
        
        asi_input = st.number_input("ASI (Anxiety Sensitivity Index)", min_value=0.0, max_value=100.0, value=50.0, help="0-100 scale. Higher = more fear of anxiety symptoms")
    
    if st.button("Predict", type="primary"):
        try:
            input_data = pd.DataFrame([[tiktok_input, instagram_input, sleep_input, asi_input]], 
                                      columns=['tiktok_minutes_daily', 'instagram_minutes_daily', 'sleep_hours', 'ASI'])
            prediction = model.predict(input_data)[0]
            
            st.success(f"Predicted addiction level: **{prediction:.1f}** / 100")
            
            # Recommendation
            col_rec1, col_rec2 = st.columns(2)
            with col_rec1:
                if prediction > 70:
                    st.warning("**High addiction risk**\n\n- Reduce screen time\n- Take regular breaks\n- Practice digital detox")
                elif prediction > 40:
                    st.info("**Medium addiction risk**\n\n- Monitor your usage\n- Set time limits\n- Improve sleep quality")
                else:
                    st.balloons()
                    st.success("**Low addiction risk!**\n\n- Keep up healthy habits\n- Maintain digital balance")
            
            with col_rec2:
                st.markdown(f"""
                **Your input:**  
                - TikTok: {tiktok_input} min/day  
                - Instagram: {instagram_input} min/day  
                - Sleep: {sleep_input} hours/day  
                - ASI: {asi_input:.0f}
                """)
                
        except Exception as e:
            st.error(f"Prediction error: {e}")
            st.info("Make sure all fields are filled correctly.")