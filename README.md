# Digital Wellbeing Analytics

Analysis of how social media (TikTok, Instagram) affects mental health, sleep quality, and digital addiction.

---

## 📌 Description

This project analyzes the relationship between social media usage and mental wellbeing. Using a synthetic dataset spanning 45 years (2015–2060), we explore trends in screen time, addiction scores, sleep patterns, and anxiety sensitivity across 100+ countries.

The interactive dashboard allows users to:
- Explore screen time patterns by country
- View correlations between social media use and mental health
- Predict personal addiction risk based on daily habits

---

## 📊 Data Source

| Attribute | Details |
|-----------|---------|
| **Dataset** | [TikTok & Instagram Addiction Dataset (2015–2060)](https://www.kaggle.com/datasets/abdulmaliklodhra/tiktok-and-instagram-addiction-dataset-20152060) |
| **Records** | 10,000+ |
| **Countries** | 100+ |
| **Time Period** | 2015–2060 |
| **Key Metrics** | TikTok minutes, Instagram minutes, sleep hours, addiction score, ASI (Anxiety Sensitivity Index) |

---

## 🔧 Technologies

| Category | Tools |
|----------|-------|
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn (Random Forest Regressor) |
| Visualization | Plotly, Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Version Control | Git, GitHub |

---

## 📈 Key Findings

| Correlation | Value | Strength |
|-------------|-------|----------|
| Screen Time → Addiction | **+0.85** | Strong positive |
| Screen Time → Sleep | **-0.65** | Moderate negative |
| Screen Time → Anxiety (ASI) | **+0.64** | Moderate positive |

**Most important feature for predicting addiction:** TikTok daily minutes

**Top affected countries:** See interactive dashboard for detailed ranking

---

## 🚀 Installation & Run

```bash
# Clone repository
git clone https://github.com/Scotzz/digital-wellbeing-analytics.git
cd digital-wellbeing-analytics

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run app.py