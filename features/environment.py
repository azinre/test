from app import app
from behave import before, after

# Set up Flask app before the tests
def before_all(context):
    context.client = app.test_client()

# Clean up after the tests
def after_all(context):
    pass