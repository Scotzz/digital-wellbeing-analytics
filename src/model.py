import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

df = pd.read_csv('data/tiktok_instagram_global_100countries.csv')

features = ['tiktok_minutes_daily', 'instagram_minutes_daily', 'sleep_hours', 'ASI']
target = 'addiction_score'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print('Training model...')
model = RandomForestRegressor()
model.fit(X_train, y_train)


# Metrics
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"R2: {r2:.4f}")
print(f"MAE: {mae:.2f}")

# Important features
importance = pd.DataFrame({
    'feature': features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nimportance features:")
print(importance)

# Save model
joblib.dump(model, 'models/addiction_model.pkl')
print("\nModel saved in 'models/addiction_model.pkl'")