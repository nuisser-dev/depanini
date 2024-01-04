import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

def get_best(ch):
    file_path = 'fake_development_data.csv'
    data = pd.read_csv(file_path)


    label_encoder = LabelEncoder()
    data['title_cv_encoded'] = label_encoder.fit_transform(data['title_cv'])

   
    features = ['title_cv_encoded', 'experience']
    target_label = ch  

    
    if target_label in data['title_cv'].unique():
        
        data['target'] = (data['title_cv'] == target_label).astype(int)

        
        X = data[features]
        y = data['target']

        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        
        clf = DecisionTreeClassifier(random_state=42)
        clf.fit(X_train, y_train)

        
        predictions = clf.predict(X_test)

        
        if 1 in predictions:
            
            software_eng_indices = [i for i, pred in enumerate(predictions) if pred == 1]

            
            best_ids = data.iloc[y_test.index[software_eng_indices]]['id'].tolist()
    
           
       
    else:
       return 0
    return best_ids
