from flask import Flask
import logging
import os
from config import config_by_name

# Read environment (default is 'dev')
env = os.getenv("FLASK_ENV", "dev")

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(config_by_name[env])

# Setup logging
logging.basicConfig(level=app.config['LOG_LEVEL'])
logger = logging.getLogger(__name__)

@app.route('/test')
def test_logging():
    logger.debug("DEBUG: This is a debug message.")
    logger.info("INFO: This is an info message.")
    logger.warning("WARNING: This is a warning message.")
    logger.error("ERROR: This is an error message.")
    return "Logging test completed. Check terminal."

if __name__ == "__main__":
    app.run(debug=True)
