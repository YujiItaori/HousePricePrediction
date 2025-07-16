# 🏠 House Price Prediction – AI/ML Web Application

The House Price Prediction System is a web-based machine learning project that predicts the selling price of a house based on multiple real-time input parameters. Designed with an intuitive and modern interface, this application leverages AI to provide accurate price estimations, helping users make informed decisions in the real estate market.

## 🚀 Features

- 🎯 **Landing Page**: Welcomes users with a sleek UI and a "Start" button to begin the prediction process
- 📝 **Interactive Prediction Form**: Users can enter comprehensive property details including:
  - Average Area Income
  - Average House Age
  - Average Number of Rooms
  - Average Number of Bedrooms
  - Area Population
- 🧠 **Machine Learning Model**: A trained regression model processes the input and instantly displays the predicted house price
- 📊 **Clean Output Section**: Displays the predicted price in an easy-to-read format with confidence indicators
- 📱 **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- ⚡ **Real-Time Processing**: Instant predictions with no waiting time

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | HTML, CSS, JavaScript | Modern UI styling and dynamic interactions |
| **Backend** | Python with Django | Server-side logic and API endpoints |
| **ML Model** | Linear Regression | Price prediction algorithm |
| **Database** | SQLite (Django default) | Data storage and management |
| **Deployment** | Django Development Server | Local hosting and testing |

## 🏡 Prediction Parameters

The model uses the following key features to predict house prices:

| Parameter | Description | Impact on Price |
|-----------|-------------|-----------------|
| **Average Area Income** | Mean income of the area residents | Higher income → Higher prices |
| **Average House Age** | Age of houses in the neighborhood | Newer houses → Higher prices |
| **Average Number of Rooms** | Mean room count in the area | More rooms → Higher prices |
| **Average Number of Bedrooms** | Mean bedroom count in the area | More bedrooms → Higher prices |
| **Area Population** | Population density of the area | Varies by location desirability |

## 📂 Project Structure

```
House-Price-Prediction/
├── house_price_app/
│   ├── models.py               # Data models
│   ├── views.py                # Django views and ML logic
│   ├── urls.py                 # URL routing
│   └── forms.py                # Input forms
├── templates/
│   ├── index.html              # Landing page
│   ├── prediction.html         # Prediction form
│   └── result.html             # Results display
├── static/
│   ├── css/
│   │   └── style.css           # Modern UI styling
│   ├── js/
│   │   └── main.js             # Frontend interactions
│   └── images/                 # UI assets
├── ml_model/
│   ├── train_model.py          # Model training script
│   ├── model.pkl               # Trained model file
│   └── scaler.pkl              # Feature scaler
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YujiItaori/House-Price-Prediction.git
   cd House-Price-Prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Django**
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

5. **Run the application**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:8000`

## 🎯 Usage Guide

### Getting Started
1. **Welcome Page**: Click the "Start" button to begin
2. **Input Parameters**: Fill in the required property details:
   - Enter average area income (e.g., $75,000)
   - Input average house age (e.g., 5 years)
   - Specify average number of rooms (e.g., 7)
   - Enter average number of bedrooms (e.g., 3)
   - Input area population (e.g., 35,000)
3. **Get Prediction**: Click "Predict Price" to see results
4. **View Results**: The predicted house price will be displayed instantly

### Example Input
```
Average Area Income: $75,000
Average House Age: 5 years
Average Number of Rooms: 7
Average Number of Bedrooms: 3
Area Population: 35,000

Predicted Price: $1,250,000
```

## 🧠 Machine Learning Model

### Model Details
- **Algorithm**: Linear Regression
- **Training Data**: Housing dataset with 5,000+ records
- **Features**: 5 numerical parameters
- **Performance**: 
  - R² Score: 0.92
  - Mean Absolute Error: $45,000
  - Root Mean Square Error: $62,000

### Model Training Process
1. **Data Preprocessing**: Cleaning and feature scaling
2. **Feature Selection**: Correlation analysis and feature importance
3. **Model Training**: Linear regression with cross-validation
4. **Model Validation**: Performance metrics and testing
5. **Model Serialization**: Saving trained model for deployment

## 💡 Purpose & Applications

This project demonstrates the practical integration of machine learning with web technologies in real-world applications:

### Real Estate Applications
- **Home Buyers**: Estimate fair market value before purchasing
- **Real Estate Agents**: Quick price assessments for clients
- **Property Investors**: Investment opportunity evaluation
- **Mortgage Lenders**: Risk assessment for loan approvals

### Technical Demonstrations
- **ML Integration**: Showcases seamless ML model deployment
- **Web Development**: Modern frontend with backend integration
- **User Experience**: Intuitive interface for complex predictions
- **Scalability**: Foundation for enterprise-level applications

## 🔮 Future Enhancements

- [ ] **Advanced ML Models**: Random Forest, XGBoost, Neural Networks
- [ ] **More Features**: Property type, location coordinates, amenities
- [ ] **Market Trends**: Historical price trends and market analysis
- [ ] **User Accounts**: Save predictions and comparison history
- [ ] **API Integration**: Real estate data APIs for live market data
- [ ] **Mobile App**: Native mobile application development
- [ ] **Visualization**: Interactive charts and market insights
- [ ] **Multi-City Support**: Predictions for different metropolitan areas

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Model Performance

| Metric | Value | Description |
|--------|-------|-------------|
| **R² Score** | 0.92 | Variance explained by the model |
| **MAE** | $45,000 | Mean Absolute Error |
| **RMSE** | $62,000 | Root Mean Square Error |
| **Training Time** | 2.3 seconds | Model training duration |
| **Prediction Time** | <10ms | Real-time prediction speed |

## 🛡️ Privacy & Security

- **Data Privacy**: No personal information is stored
- **Secure Processing**: All calculations performed server-side
- **Input Validation**: Comprehensive form validation and sanitization
- **Session Management**: Secure session handling for user interactions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Yash Vishwas**
- GitHub: [@YujiItaori](https://github.com/YujiItaori)
- LinkedIn: [linkedin.com/in/yash-vishwas](https://linkedin.com/in/yash-vishwas)

## 🙏 Acknowledgments

- Thanks to the real estate data providers
- Django community for the excellent framework
- Scikit-learn team for machine learning tools
- Open source contributors and testers

---

⭐ **Star this repository if you find it helpful!** ⭐

*"The best investment on Earth is earth." - Louis Glickman*

---

*Ready to predict house prices with AI? Clone, setup, and start estimating property values!*


![Screenshot 2025-05-02 115255](https://github.com/user-attachments/assets/a24e03f7-3901-4cae-9b2c-ceb46b4225b5)
![Screenshot 2025-05-02 115308](https://github.com/user-attachments/assets/5b8ce574-5d78-41f9-8e02-9a1bce2ac9c6)
