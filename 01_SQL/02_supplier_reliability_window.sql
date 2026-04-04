WITH supplier_monthly AS (
    SELECT
        s.supplier_name,
        s.reliability_tier,
        s.avg_lead_time_days            AS contracted_lead_time,
        d.month_name,
        d.quarter,
        d.year,
        COUNT(f.shipment_id)            AS shipments_count,
        ROUND(AVG(f.lead_time_days), 1) AS actual_avg_lead_time,
        ROUND(AVG(f.co2_kg_emitted), 1) AS avg_co2_per_shipment,
        ROUND(SUM(f.revenue_eur), 2)    AS total_revenue,
        ROUND(SUM(f.freight_cost_eur), 2) AS total_freight_cost,
        ROUND(AVG(f.lead_time_days) - s.avg_lead_time_days, 1) AS lead_time_variance
    FROM FACT_SHIPMENTS f
    JOIN DIM_SUPPLIER s ON f.supplier_key = s.supplier_key
    JOIN DIM_DATE d     ON f.date_key     = d.date_key
    GROUP BY s.supplier_name, s.reliability_tier,
             s.avg_lead_time_days, d.month_name, d.quarter, d.year
)
SELECT
    supplier_name,
    reliability_tier,
    contracted_lead_time,
    month_name,
    quarter,
    actual_avg_lead_time,
    lead_time_variance,
    avg_co2_per_shipment,
    total_revenue,
    RANK() OVER (
        PARTITION BY quarter
        ORDER BY lead_time_variance ASC
    ) AS reliability_rank_in_quarter,
    ROUND(AVG(actual_avg_lead_time) OVER (
        PARTITION BY supplier_name
        ORDER BY quarter
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 1) AS rolling_3month_avg_lead_time
FROM supplier_monthly
ORDER BY quarter, reliability_rank_in_quarter;