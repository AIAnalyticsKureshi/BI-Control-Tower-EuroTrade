# ============================================================
# Script 2: data_quality_scorecard.py
# BI Control Tower — EuroTrade GmbH
# Author: Mohammad M. Kureshi
# ============================================================

import sqlite3
import pandas as pd
from datetime import datetime

DB_PATH = r"D:\Project for CV Mohammad\BI-Control-Tower_EuroTrade\logistics_warehouse.db"

def run_scorecard():
    conn = sqlite3.connect(DB_PATH)
    results = []
    print("\n" + "="*55)
    print("  BI CONTROL TOWER — DATA QUALITY SCORECARD")
    print(f"  EuroTrade GmbH | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*55)

    # CHECK 1: Row Counts
    tables = ["DIM_DATE","DIM_CUSTOMER","DIM_SUPPLIER","DIM_PRODUCT","DIM_ROUTE","FACT_SHIPMENTS"]
    print("\n[CHECK 1] Row Counts")
    all_ok = True
    for t in tables:
        count = pd.read_sql(f"SELECT COUNT(*) as cnt FROM {t}", conn).iloc[0,0]
        status = "✅" if count > 0 else "❌"
        if count == 0: all_ok = False
        print(f"  {status} {t}: {count} rows")
    results.append(("Row Counts", all_ok))

    # CHECK 2: NULL Values
    print("\n[CHECK 2] NULL Values in FACT_SHIPMENTS")
    key_cols = ["shipment_id","date_key","product_key","customer_key",
                "supplier_key","route_key","revenue_eur","freight_cost_eur","weight_kg"]
    df = pd.read_sql("SELECT * FROM FACT_SHIPMENTS", conn)
    all_ok = True
    for col in key_cols:
        nulls = df[col].isnull().sum()
        status = "✅" if nulls == 0 else "❌"
        if nulls > 0: all_ok = False
        print(f"  {status} {col}: {nulls} nulls")
    results.append(("NULL Values", all_ok))

    # CHECK 3: Referential Integrity
    print("\n[CHECK 3] Referential Integrity")
    checks = [
        ("customer_key", "DIM_CUSTOMER", "customer_key"),
        ("supplier_key", "DIM_SUPPLIER", "supplier_key"),
        ("product_key",  "DIM_PRODUCT",  "product_key"),
        ("route_key",    "DIM_ROUTE",    "route_key"),
        ("date_key",     "DIM_DATE",     "date_key"),
    ]
    all_ok = True
    for fk, dim, pk in checks:
        query = f"""
            SELECT COUNT(*) as cnt FROM FACT_SHIPMENTS f
            LEFT JOIN {dim} d ON f.{fk} = d.{pk}
            WHERE d.{pk} IS NULL
        """
        orphans = pd.read_sql(query, conn).iloc[0,0]
        status = "✅" if orphans == 0 else "❌"
        if orphans > 0: all_ok = False
        print(f"  {status} {fk} → {dim}: {orphans} orphans")
    results.append(("Referential Integrity", all_ok))

    # CHECK 4: Lead Time Logic
    print("\n[CHECK 4] Lead Time Logic")
    df2 = pd.read_sql("SELECT lead_time_days FROM FACT_SHIPMENTS", conn)
    bad_lead = (df2["lead_time_days"] <= 0).sum()
    status = "✅" if bad_lead == 0 else "❌"
    print(f"  {status} Invalid lead_time_days (zero or negative): {bad_lead} records")
    results.append(("Lead Time Logic", bad_lead == 0))

    # CHECK 5: Value Ranges
    print("\n[CHECK 5] Value Ranges")
    df3 = pd.read_sql("SELECT weight_kg, freight_cost_eur, revenue_eur FROM FACT_SHIPMENTS", conn)
    neg_weight  = (df3["weight_kg"] <= 0).sum()
    neg_cost    = (df3["freight_cost_eur"] <= 0).sum()
    neg_revenue = (df3["revenue_eur"] <= 0).sum()
    all_ok = neg_weight == 0 and neg_cost == 0 and neg_revenue == 0
    print(f"  {'✅' if neg_weight==0 else '❌'} Negative/Zero weight_kg: {neg_weight} records")
    print(f"  {'✅' if neg_cost==0 else '❌'} Negative/Zero freight_cost_eur: {neg_cost} records")
    print(f"  {'✅' if neg_revenue==0 else '❌'} Negative/Zero revenue_eur: {neg_revenue} records")
    results.append(("Value Ranges", all_ok))

    # FINAL SCORE
    passed = sum(1 for _, ok in results if ok)
    total  = len(results)
    score  = round((passed / total) * 100)
    print("\n" + "="*55)
    print(f"  CHECKS PASSED: {passed}/{total}")
    print(f"  OVERALL SCORE: {score}%  |  STATUS: {'EXCELLENT ✅' if score==100 else 'NEEDS ATTENTION ⚠️'}")
    print("="*55 + "\n")
    conn.close()

if __name__ == "__main__":
    run_scorecard()