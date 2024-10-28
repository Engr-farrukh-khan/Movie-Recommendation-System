# 🎬 Movie Recommendation System - Netflix Style 🍿

Welcome to my **Movie Recommendation System** with a Netflix-inspired design! This project uses **Machine Learning** and a **content-based recommendation algorithm** to provide movie suggestions. Featuring dark-themed aesthetics and modern hover effects, the app is visually engaging and easy to navigate. Built with **Streamlit** for simplicity, the app is also fully responsive.

---

## 🌟 Features

- **Personalized Recommendations**: Get relevant movie recommendations instantly with a similarity-based model.
- **Dark Mode Design**: Inspired by Netflix’s dark UI, the app has a sleek red and black theme.
- **Dynamic API Integration**: Automatically fetches movie posters and details using the **TMDb API**.
- **Hover Effects and Animations**: Smooth CSS transitions and glow effects add to the user experience.
- **Fully Responsive**: Adapts seamlessly to various screen sizes, providing a consistent experience on any device.

---

## 🚀 Technologies Used

- **Python & Streamlit**: Powering the app with a user-friendly interface.
- **Machine Learning (Content-Based Filtering)**: Provides precise movie recommendations.
- **TMDb API**: For dynamic movie data and images.
- **CSS & Tailwind/Bootstrap**: Styled for a professional, eye-catching Netflix vibe.

---

## 📂 File Structure

- `app.py`: Main application file for the Streamlit-based recommendation system.
- `similarity.pkl`: Pre-computed similarity matrix for quick recommendations.
- `movies_dict.pkl`: Movie dataset used for recommendation.

---
## 🌐 How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone <repo_link>
2. **Install Dependencies:**:
   ```bash
   pip install -r requirements.txt
3. **Run the App:**:
   ```bash
    streamlit run app.py
