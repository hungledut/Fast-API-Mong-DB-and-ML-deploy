"Iris Routes"
from fastapi import APIRouter
from sklearn.datasets import load_iris
from app.ml.model_ml import iris_clf
from app.models.iris_model import Iris


iris_api_router = APIRouter()
iris = load_iris()


@iris_api_router.post('/predict')
async def predict(data : Iris):
    "iris predict"
    test_data = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
    ]]  
    class_idx = iris_clf.predict(test_data)[0]
    return { 'class' : iris['target_names'][class_idx]}
