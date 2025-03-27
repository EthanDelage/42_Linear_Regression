import pickle
import os
from typing import Union


class ModelManager:
    def __init__(self, model_path="models/model.pkl"):
        self.model_path = model_path

    def save_model(self, model: any):
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        with open(self.model_path, "wb") as f:
            pickle.dump(model, f)
        print("Model saved as {self.model_path}!")

    def load_model(self) -> Union[any, None]:
        if not(os.path.exists(self.model_path)):
            raise FileNotFoundError(f"Model file {self.model_path} does not exist!")
        with open(self.model_path, "rb") as f:
            model = pickle.load(f)
        try:
            self.require_attribute_(model, "coef")
            self.require_attribute_(model, "intercept")
        except AttributeError as e:
            print(e)
            return None
        return model

    @staticmethod
    def format_model(coefficient: int, intercept: int) -> any:
        return {"coef": coefficient, "intercept": intercept}

    @staticmethod
    def require_attribute_(model: any, attribute: str):
        if attribute not in model:
            raise AttributeError(f"Model does not contain a '{attribute}' attribute!")
