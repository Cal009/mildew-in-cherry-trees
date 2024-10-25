import streamlit as st
from app_pages.multi_page import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary
from app_pages.page_cells_visualizer import page_cells_visualizer
from app_pages.page_cells_detector import page_cells_detector
from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name="Cherry Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary)
app.add_page("Cells Visualiser", page_cells_visualizer)
app.add_page("Cherry Detection", page_cells_detector)
app.add_page("ML Performance", page_ml_performance_metrics)

app.run()  # Run the app