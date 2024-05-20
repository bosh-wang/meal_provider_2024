import yaml
import sys


def load_config():
    """
    Load config yaml file
    """

    with open("/workspaces/meal_provider_2024/backend/config.yaml") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg
config = load_config()