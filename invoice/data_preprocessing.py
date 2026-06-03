import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def load_invoice_data():
    conn = sqlite3.connect("C:/Users/Aadarsh/Desktop/Vendor Invoice Intelligent System/data/inventory.db")
    
    query = """
    WITH purchase_agg AS (
        SELECT
        p.pONumber,
        COUNT(DISTINCT p.Brand) AS total_brands,
        SUM(p.Quantity) AS total_item_quantity,
        SUM(p.Dollars) AS total_items_dollars,
        AVG(julianday(p.ReceivingDate) - )
    )
    """
    