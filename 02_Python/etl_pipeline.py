import pandas as pd
import sqlite3
import random
from datetime import datetime, timedelta

print("=" * 60)
print("EuroTrade GmbH — ETL Pipeline")
print("Generating 500 professional shipment records...")
print("=" * 60)

DB_PATH = r"D:\Project for CV Mohammad\BI-Control-Tower_EuroTrade\logistics_warehouse.db"

customers = [
    (1, "Bosch GmbH", "Enterprise"),
    (2, "Siemens AG", "Enterprise"),
    (3, "Rhenus Logistics", "Mittelstand"),
    (4, "DB Schenker", "Enterprise"),
    (5, "Hapag-Lloyd AG", "Enterprise"),
    (6, "Trumpf GmbH", "Mittelstand"),
    (7, "Herrenknecht AG", "Mittelstand"),
    (8, "Voith GmbH", "Mittelstand")
]

suppliers = [
    (1, "Yangtze Manufacturing Co.", "A", 18),
    (2, "Vietnam Industrial Supply", "B", 24),
    (3, "Mumbai Trade Partners", "A", 21),
    (4, "Bangkok Components Ltd.", "B", 28),
    (5, "Jakarta Export House", "C", 35),
    (6, "Taipei Precision Parts", "A", 16),
    (7, "Seoul Electronics Hub", "A", 14),
    (8, "Karachi Textile Mills", "C", 42)
]

routes = [
    (1, "Shanghai", "Sea", 20800, 0.000015, "Low"),
    (2, "Ho Chi Minh City", "Sea", 18200, 0.000015, "Low"),
    (3, "Mumbai", "Air", 6200, 0.0005, "High"),
    (4, "Bangkok", "Sea", 19400, 0.000015, "Low"),
    (5, "Jakarta", "Sea", 21600, 0.000018, "Low"),
    (6, "Taipei", "Air", 9200, 0.0005, "High"),
    (7, "Seoul", "Sea", 21000, 0.000015, "Low"),
    (8, "Warsaw", "Road", 580, 0.0001, "Medium"),
    (9, "Rotterdam", "Rail", 870, 0.000028, "Low"),
    (10, "Karachi", "Sea", 17800, 0.000018, "Medium")
]

products = [
    (1, "Industrial Control Unit", "Electronics", 12.5),
    (2, "Precision Ball Bearings", "Machinery", 4.2),
    (3, "Hydraulic Pump Assembly", "Machinery", 28.75),
    (4, "Copper Wire Harness", "Electronics", 3.8),
    (5, "Carbon Fiber Panels", "Materials", 6.1),
    (6, "LED Display Module", "Electronics", 1.95),
    (7, "Steel Structural Frame", "Materials", 185.0),
    (8, "Textile Machine Parts", "Machinery", 9.3)
]

print("Reference data loaded successfully.")

def generate_shipments(num_records=500):
    shipments = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(num_records):
        customer = random.choice(customers)
        supplier = random.choice(suppliers)
        route = random.choice(routes)
        product = random.choice(products)
        
        shipment_date = start_date + timedelta(days=random.randint(0, 364))
        date_key = int(shipment_date.strftime("%Y%m01"))
        
        if product[3] > 50:
            quantity = random.randint(10, 100)
        elif product[3] > 10:
            quantity = random.randint(50, 500)
        else:
            quantity = random.randint(100, 2000)
        weight_kg = round(quantity * product[3], 2)
        unit_price = round(random.uniform(15, 85), 2)
        revenue = round(quantity * unit_price, 2)
        cogs = round(revenue * random.uniform(0.55, 0.68), 2)
        freight_cost = round(weight_kg * 0.45 + random.uniform(400, 2000), 2)
        freight_cost = min(freight_cost, revenue * 0.35)
        net_profit = round(revenue - cogs - freight_cost, 2)
        net_margin = round(net_profit / revenue * 100, 2)
        co2 = round(weight_kg * route[3] * route[4], 2)
        
        actual_lead_time = supplier[3] + random.randint(-3, 10)
        actual_lead_time = max(actual_lead_time, 7)
        shipment_id = 25 + i
        
        shipments.append({
            "shipment_id": shipment_id,
            "date_key": date_key,
            "product_key": product[0],
            "customer_key": customer[0],
            "supplier_key": supplier[0],
            "route_key": route[0],
            "revenue_eur": revenue,
            "cogs_eur": cogs,
            "freight_cost_eur": freight_cost,
            "quantity_units": quantity,
            "weight_kg": weight_kg,
            "lead_time_days": actual_lead_time,
            "co2_kg_emitted": co2
        })
    
    return pd.DataFrame(shipments)

df = generate_shipments(500)
print(f"Generated {len(df)} shipment records.")
print(f"Total Revenue: EUR {df['revenue_eur'].sum():,.2f}")
print(f"Total Net Profit: EUR {(df['revenue_eur'] - df['cogs_eur'] - df['freight_cost_eur']).sum():,.2f}")
print(f"Total CO2 Emitted: {df['co2_kg_emitted'].sum():,.1f} kg")
print(f"Average Lead Time: {df['lead_time_days'].mean():.1f} days")

def validate_data(df):
    print("\n" + "=" * 60)
    print("DATA QUALITY VALIDATION REPORT")
    print("=" * 60)
    
    anomalies = []
    
    negative_freight = df[df['freight_cost_eur'] < 0]
    if len(negative_freight) > 0:
        anomalies.append(f"CRITICAL: {len(negative_freight)} negative freight costs")

    negative_revenue = df[df['revenue_eur'] < 0]
    if len(negative_revenue) > 0:
        anomalies.append(f"CRITICAL: {len(negative_revenue)} negative revenue values")
    
    impossible_lead = df[df['lead_time_days'] < 3]
    if len(impossible_lead) > 0:
        anomalies.append(f"WARNING: {len(impossible_lead)} impossibly short lead times")
    
    zero_co2 = df[df['co2_kg_emitted'] <= 0]
    if len(zero_co2) > 0:
        anomalies.append(f"WARNING: {len(zero_co2)} zero or negative CO2 values")
    
    high_freight = df[df['freight_cost_eur'] > df['revenue_eur'] * 0.5]
    if len(high_freight) > 0:
        anomalies.append(f"WARNING: {len(high_freight)} shipments where freight exceeds 50% of revenue")
    
    if len(anomalies) == 0:
        print("ALL CHECKS PASSED. Data quality is excellent.")
    else:
        for a in anomalies:
            print(a)
    
    print(f"\nTotal Records: {len(df)}")
    print(f"Valid Records: {len(df) - len(anomalies)}")
    print(f"Data Quality Score: {round((len(df) - len(anomalies)) / len(df) * 100, 2)}%")
    return df

def load_to_database(df):
    print("\n" + "=" * 60)
    print("LOADING DATA TO DATABASE")
    print("=" * 60)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('FACT_SHIPMENTS', conn, if_exists='append', index=False)
    conn.close()
    print(f"Successfully loaded {len(df)} records into FACT_SHIPMENTS.")
    print("ETL Pipeline completed successfully.")

df = validate_data(df)
load_to_database(df)
