"""Initialize Flask app."""
from flask import Flask


def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)


    with app.app_context():
        # Import parts of our core Flask app
        import routes
        

        # Import Dash application
        from dashboard import init_dashboard
        app = init_dashboard(app)
        #from dashb import init_callbacks
        
        return app