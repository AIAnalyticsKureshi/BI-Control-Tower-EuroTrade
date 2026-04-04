SELECT
    d.quarter,
    d.year,
    r.transport_mode,
    COUNT(f.shipment_id)                    AS total_shipments,
    ROUND(SUM(f.co2_kg_emitted), 2)         AS total_co2_kg,
    ROUND(SUM(f.revenue_eur), 2)            AS total_revenue,
    ROUND(SUM(f.revenue_eur - f.cogs_eur - f.freight_cost_eur), 2) AS net_profit,
    ROUND(AVG(f.co2_kg_emitted), 2)         AS avg_co2_per_shipment,
    ROUND(SUM(f.co2_kg_emitted) /
        SUM(f.revenue_eur) * 1000, 4)       AS co2_per_1000eur
FROM FACT_SHIPMENTS f
JOIN DIM_DATE d  ON f.date_key  = d.date_key
JOIN DIM_ROUTE r ON f.route_key = r.route_key
GROUP BY d.quarter, d.year, r.transport_mode
ORDER BY d.quarter, total_co2_kg DESC;