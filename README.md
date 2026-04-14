<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=26&pause=1000&color=A78BFA&center=true&vCenter=true&width=850&lines=BI+Control+Tower+%E2%80%94+EuroTrade+GmbH;End-to-End+Logistics+BI+Ecosystem;SQL+%E2%80%A2+Python+%E2%80%A2+Power+BI+%E2%80%A2+Excel;Turning+Raw+Shipment+Data+Into+Executive+Decisions" alt="Typing SVG" />

<br/><br/>

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-0078d7?style=for-the-badge&logo=visual-studio-code&logoColor=white)

<br/>

[![Author](https://img.shields.io/badge/Author-Mohammad_M._Kureshi-a78bfa?style=flat&logo=github&logoColor=white)](https://github.com/AIAnalyticsKureshi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohammad-kureshi/)
[![Profile Views](https://komarev.com/ghpvc/?username=AIAnalyticsKureshi&color=a78bfa&style=flat)](https://github.com/AIAnalyticsKureshi)

</div>

---

## 🎯 The Business Problem

EuroTrade GmbH — a fictional global logistics company — had shipment data scattered across systems with no single source of truth. Leadership had zero visibility into delivery performance, route profitability, supplier reliability, or CO₂ compliance under CSRD regulations.

This project builds the **complete BI layer** to fix that. Not a tutorial. Not a course exercise. A full end-to-end system built from scratch to mirror real enterprise BI work.

---

## 🏗️ Architecture

```
Raw Business Data
      │
      ▼
┌─────────────────────────────┐
│   ETL Pipeline              │
│   Python · Pandas           │
│   500 records · 100% clean  │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│   SQLite Warehouse          │
│   Star Schema · 3NF         │
│   6 Tables · 524 Rows       │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│   Power BI Dashboard        │
│   3 Pages · DAX Measures    │
│   Interactive · Dark Theme  │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│   Excel Scenario Model      │
│   What-If · Carbon Tax      │
└─────────────────────────────┘
```

---

## 📊 Real Data — Key Numbers

| Icon | Metric | Value | Status |
|------|--------|-------|--------|
| 📦 | Total Shipments | 524 | ✅ Full year 2024 |
| 💶 | Total Revenue | €20.0M | ✅ Verified |
| 📈 | Net Profit | €5.95M | ✅ 29.74% margin |
| 🚛 | Freight Cost % | 8.66% | ⚠️ Near 9% threshold |
| ⏱️ | Avg Lead Time | 27.6 days | ⚠️ Road worst 30.1d |
| 🌿 | Total CO₂ | 2.76M kg | ✅ CSRD tracked |
| ⭐ | Best Mode | Rail | ✅ 7.81% · 24.7d · 5,295kg |
| 🔴 | Worst Mode | Air | ❌ 9.99% · 75% of total CO₂ |

---

## 🗄️ Data Model — Star Schema

```
                    ┌─────────────┐
                    │  DIM_DATE   │
                    │  date_key   │
                    │  month_name │
                    │  quarter    │
                    └──────┬──────┘
                           │
┌─────────────┐    ┌───────┴────────┐    ┌──────────────────┐
│ DIM_PRODUCT │    │ FACT_SHIPMENTS │    │   DIM_SUPPLIER   │
│ product_key ├────┤ 524 rows       ├────┤  TIER            │
│ category    │    │ revenue_eur    │    │  avg_lead_time   │
│ sub_category│    │ freight_cost   │    │  defect_rate_pct │
└─────────────┘    │ lead_time_days │    └──────────────────┘
                   │ co2_kg_emitted │
┌─────────────┐    └───────┬────────┘    ┌──────────────────┐
│DIM_CUSTOMER │            └─────────────┤   DIM_ROUTE      │
│ segment     │                          │  transport_mode  │
│ company_name│                          │  distance_km     │
│ city/country│                          │  emission_factor │
└─────────────┘                          │  co2_tier        │
                                         └──────────────────┘
```

---

## 🔨 Build Progress

| Week | Layer | Deliverable | Status |
|------|-------|-------------|--------|
| 1 | 🗄️ SQL | Star schema + 5 advanced queries · Window functions · RANK() · CTEs · CO₂ tracking | ✅ Done |
| 2 | 🐍 Python | ETL pipeline + Data quality scorecard · 500 records · 5 checks · 100% score | ✅ Done |
| 3 | 📊 Power BI | 3-page dashboard · DAX measures · Dark theme · Interactive sidebar views | 🔄 In Progress |
| 4 | 📋 Excel | Scenario planning model · What-if analysis · Carbon tax modelling | ⏳ Coming Next |

---

## 🖥️ Power BI Dashboard — 3 Pages

### ⚡ Page 1 — Executive Overview

**Main Dashboard:** 6 KPI cards · Revenue by Month · Segment donut · Profit trend line · Customer breakdown

**🔥 Sidebar View 2 — Operational Efficiency:**
Freight % by transport mode · Lead time by mode · CO₂ donut · Mode scatter plot · 3 dynamic alerts red/amber/green

**🔗 Sidebar View 3 — Supplier & Route Intelligence:**
Supplier scorecard with Gold/Silver/Bronze tiers · Revenue by country · Lead time by tier · Distance vs freight scatter

### 🚚 Page 2 — Logistics Performance
Delivery KPIs · Lead time analysis · Freight breakdown · Supplier reliability

### 👥 Page 3 — Customer & Product Analysis
Customer revenue · Product categories · Segment comparison · Account manager view

---

## 🧮 DAX Measures Built

```dax
-- Core Financial
Freight Cost Pct     = DIVIDE(SUM(freight_cost_eur), SUM(revenue_eur))
Net Profit           = SUM(revenue_eur) - SUM(cogs_eur) - SUM(freight_cost_eur)
Profit Margin %      = DIVIDE([Net Profit], SUM(revenue_eur))

-- Operational
Avg Lead Time        = AVERAGE(lead_time_days)
Rail CO2             = CALCULATE(SUM(co2_kg_emitted), transport_mode = "Rail")

-- Display Formatting
Lead Time Display    = FORMAT(AVERAGE(lead_time_days), "0.0") & " days"
Rail CO2 Display     = FORMAT([Rail CO2], "#,##0") & " kg"
Last Refresh         = "Last Refresh: " & FORMAT(NOW(), "YYYY-MM-DD")

-- Dynamic Alert Text
Freight Trend Text   = "Air highest at " & FORMAT(AirFreight*100,"0.00") & "%"
Lead Time Trend Text = "Road worst at " & FORMAT(RoadLT,"0.0") & " days"
Rail CO2 Trend Text  = "↓ vs Air " & FORMAT(AirCO2/1000000,"0.00") & "M kg total"

-- Alert Status (0=Green · 1=Amber · 2=Red)
Freight Alert Status = IF(Freight > 0.09, 2, IF(Freight > 0.08, 1, 0))
Lead Time Alert      = IF(AvgLT > 29, 2, IF(AvgLT > 27, 1, 0))
Rail CO2 Alert       = IF(RailCO2 < 6000, 0, IF(RailCO2 < 8000, 1, 2))
```

---

## 🔍 Key Business Findings

> ⚠️ **Finding 1 — Air Transport is the biggest risk**
> Air freight costs 9.99% of revenue — highest of all modes — and contributes 75% of total CO₂ at 2.08M kg. Shifting non-urgent volume from Air to Rail simultaneously reduces cost and emissions.

> ⭐ **Finding 2 — Rail is the strategic winner**
> Rail delivers lowest freight cost 7.81%, fastest lead time 24.7 days, and only 5,295 kg total CO₂. Increasing Rail share is the single highest-impact operational decision available to leadership.

> ⏱️ **Finding 3 — Road has worst delivery performance**
> Avg 30.1 days on Road is the highest of all modes. Three specific routes exceed the 32-day threshold and require immediate review.

> 💰 **Finding 4 — Margin healthy but under pressure**
> 29.74% margin is strong. Freight cost at 8.66% is approaching the 9% threshold. Air transport is the primary driver — reducing air usage directly protects margin.

---

## 📁 Repository Structure

```
BI-Control-Tower-EuroTrade/
│
├── 📁 01_SQL/
│   ├── create_schema.sql
│   ├── logistics_warehouse.db
│   └── queries/
│       ├── 01_revenue_analysis.sql
│       ├── 02_supplier_scorecard.sql
│       ├── 03_window_functions.sql
│       ├── 04_cte_analysis.sql
│       └── 05_co2_tracking.sql
│
├── 📁 02_Python/
│   ├── etl_pipeline.py
│   └── data_quality_scorecard.py
│
├── 📁 03_PowerBI/
│   └── BI-Control-Tower_EuroTrade.pbix
│
└── 📁 04_Excel/
    └── scenario_model.xlsx
```

---

## 🛠️ Tech Stack

<div align="center">

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-F2C811?style=flat&logo=powerbi&logoColor=black)
![Power Query](https://img.shields.io/badge/Power_Query-F2C811?style=flat&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoft-excel&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-0078d7?style=flat&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)

</div>

---

## 👤 About the Author

Built by **Mohammad M. Kureshi** — Business Intelligence Analyst based in Magdeburg, Germany. Actively seeking BI Analyst, Reporting Analyst, and Data Analyst roles across Germany.

Every layer of this project — from schema design to ETL pipeline to Power BI dashboard — was designed and built independently from scratch as proof of full-stack BI capability.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/Connect_on_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohammad-kureshi/)
[![Portfolio](https://img.shields.io/badge/Full_Portfolio-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AIAnalyticsKureshi)
[![Email](https://img.shields.io/badge/Send_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mohd.kureshi04@gmail.com)

</div>

---

<div align="center">
<sub>📍 Magdeburg, Germany · Open to relocation · 🏆 Microsoft PL-300 In Progress · May 2026 · 🗓️ Last updated: April 2026</sub>
</div>
