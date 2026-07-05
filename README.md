# 🌾 OptiCrop: Smart Agricultural Production Optimization Engine

OptiCrop is a Machine Learning-based web application that helps farmers decide which crop is best suited to grow on their land, based on soil nutrients and climate conditions. Given seven inputs — Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall — the app instantly recommends the most suitable crop along with a confidence score and two backup suggestions.

Built as part of the **SmartBridge AI/ML Virtual Internship 2026**.

**Team:** Duddu Vijaya Padma Priya, Kasa Sahithya

---

## Problem Statement

Farmers in rural India often select crops based on guesswork, tradition, or informal advice rather than scientific analysis, leading to poor yield and financial loss. OptiCrop replaces this guesswork with a simple, accessible, data-driven crop advisory tool.

## Features

- Takes 7 soil and climate parameters as input
- Predicts the single best-suited crop using a trained Random Forest classifier
- Displays a confidence score for the prediction
- Shows the top 3 alternate crop suggestions
- Simple, clean Streamlit web interface — no installation needed for end users once deployed

## Tech Stack

| Component | Technology |
|---|---|
| Model | scikit-learn (Random Forest Classifier) |
| Web Framework | Streamlit |
| Data Handling | pandas, numpy |
| Language | Python 3.8+ |

## Project Structure

```
5. Project Development Phase/
├── app.py                    # Streamlit web application (run this to launch the site)
├── model.pkl                  # Pre-trained Random Forest model
├── train_model.py              # Script used to train model.pkl from the dataset
├── Crop_recommendation.csv      # Training dataset (2200 records, 22 crop classes)
├── requirements.txt             # Python dependencies
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd "5. Project Development Phase"
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App Locally

```bash
streamlit run app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

### (Optional) Re-training the Model

`model.pkl` is already included and ready to use, so this step is **not required** to run the app. The training dataset (`Crop_recommendation.csv`, 2200 records) is bundled in this folder. Only do this if you want to retrain:

```bash
python train_model.py
```
This regenerates `model.pkl` from `Crop_recommendation.csv`.

**Dataset source:** [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) (Kaggle) — included here as `Crop_recommendation.csv`.

## Deployment

This app is built for one-click deployment on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push this folder to a public GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in, and click "New app".
3. Select your repository and set the main file path to `app.py`.
4. Click "Deploy".

**Live App URL:** https://opticrop-smart-agriculture-6uvb6quyslcraqxnjroose.streamlit.app/

## Screenshots

Are in Project Documentation


## Model Details

- **Algorithm:** Random Forest Classifier (100 estimators)
- **Input Features:** N, P, K, temperature, humidity, ph, rainfall
- **Output Classes:** 22 crop types (e.g., rice, maize, mango, banana, coffee, etc.)
- **Dataset:** [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) (Kaggle)

## Future Enhancements

- Multi-language support for regional farmers
- Mobile-friendly UI
- Integration with live weather APIs for automatic climate input
- Fertilizer and irrigation recommendations alongside crop suggestions

## License

This project was built for educational purposes as part of the SmartBridge AI/ML Virtual Internship 2026.
