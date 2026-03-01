# Student Segmentation & Personalized Course Recommendation

## Objective
Segment learners based on engagement and spending behavior and provide personalized course recommendations.

## Dataset
- users.csv: User demographics
- courses.csv: Course metadata
- transactions.csv: Enrollment & payment data

## Methodology
1. Aggregated transaction data at user level
2. Engineered features:
   - total_courses
   - total_spent
3. Scaled numerical features
4. Applied K-Means clustering
5. Selected optimal clusters using Elbow Method
6. Built Streamlit dashboard for visualization

## Clusters
- Cluster 0: High spenders, multiple courses
- Cluster 1: Moderate learners
- Cluster 2: Beginners / inactive users

## Tools
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib, Seaborn

## How to Run
1. Open terminal in the project folder
2. Install required libraries
3. Run the Streamlit app

pip install streamlit scikit-learn pandas matplotlib seaborn
streamlit run app.py