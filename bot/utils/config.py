import os
import yaml
import logging

logger = logging.getLogger(__name__)

def load_config():
    """Load configuration from config.yml"""
    default_config = {
        'groq': {
            'model': 'mixtral-8x7b-32768',
            'temperature': 0.7,
        },
        'attendance': {
            'max_records': 1000,
            'max_duration': '8h'
        }
    }
    
    try:
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                return {**default_config, **config}
        return default_config
    except Exception as e:
        logger.error(f"Error loading config: {e}")
        return default_config
