"Iris Model"
from pydantic import BaseModel

class Iris(BaseModel):
    "Iris"
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
