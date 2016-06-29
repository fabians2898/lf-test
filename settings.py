import os

SETTINGS = dict(
         template_path = os.path.join(os.path.dirname(__file__), 'templates'),
         static_path = os.path.join(os.path.dirname(__file__), 'static'),
         debug = True,                  
)

PORT = int(os.environ.get("PORT", 8889))