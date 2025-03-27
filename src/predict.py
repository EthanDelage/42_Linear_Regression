from estimate_price import estimate_price
from model_manager import ModelManager

import sys

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print_usage()
    model = load_model(args[0])
    while True:
        try:
            mileage = int(input("Enter mileage: "))
            price = estimate_price(mileage, model['intercept'], model['coef'])
            print("Predicted price: " + str(price))
            break
        except ValueError:
            print("Please enter a number")

def load_model(model_path: str) -> any:
    model_manager = ModelManager(model_path=model_path)
    try:
        return model_manager.load_model()
    except FileNotFoundError as e:
        model = ModelManager.format_model(0, 0)
        print(f"Error: {e}")
        print(f"Info: Using default model ({model})")
        return model

def print_usage():
    print("Usage: python predict.py <model_path>")
    print("\nArguments:")
    print("  <model_path>   Path to the trained model file (e.g., models/model.pkl)")
    print("\nExample:")
    print("  python predict.py models/model.pkl")
    sys.exit(1)
if __name__ == "__main__":
    main()