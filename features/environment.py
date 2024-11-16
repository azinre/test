import sys
sys.path.insert(0, '/Users/Azin/test')
from app import app



# Set up Flask app before the tests
def before_all(context):
    context.client = app.test_client()

# Clean up after the tests
def after_all(context):
    pass

