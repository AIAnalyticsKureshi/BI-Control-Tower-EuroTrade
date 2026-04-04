SELECT
    s.supplier_name,
    s.country,
    s.reliability_tier,
    s.avg_lead_time_days                    AS contracted_days,
    COUNT(f.shipment_id)                    AS total_shipments,
    ROUND(AVG(f.lead_time_days), 1)         AS actual_avg_days,
    ROUND(AVG(f.lead_time_days) - s.avg_lead_time_days, 1) AS variance_days,
    ROUND(AVG(s.defect_rate_pct), 2)        AS defect_rate,
    ROUND(SUM(f.revenue_eur), 2)            AS total_revenue,
    ROUND(SUM(f.revenue_eur - f.cogs_eur - f.freight_cost_eur), 2) AS net_profit,
    ROUND(AVG(f.co2_kg_emitted), 1)         AS avg_co2_per_shipment,
    CASE
        WHEN ROUND(AVG(f.lead_time_days) - s.avg_lead_time_days, 1) <= 2
             AND s.reliability_tier = 'A'
             AND AVG(s.defect_rate_pct) < 1.0 THEN 'EXCELLENT'
        WHEN ROUND(AVG(f.lead_time_days) - s.avg_lead_time_days, 1) <= 4
             AND s.reliability_tier IN ('A','B')
             AND AVG(s.defect_rate_pct) < 2.0 THEN 'ACCEPTABLE'
        WHEN ROUND(AVG(f.lead_time_days) - s.avg_lead_time_days, 1) <= 6
             AND AVG(s.defect_rate_pct) < 3.0 THEN 'MONITOR'
        ELSE 'CRITICAL'
    END AS performance_status
FROM FACT_SHIPMENTS f
JOIN DIM_SUPPLIER s ON f.supplier_key = s.supplier_key
GROUP BY s.supplier_name, s.country,
         s.reliability_tier, s.avg_lead_time_days
ORDER BY variance_days ASC;