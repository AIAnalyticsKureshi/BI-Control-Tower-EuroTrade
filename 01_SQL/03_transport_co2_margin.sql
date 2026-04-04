SELECT
    r.transport_mode,
    r.co2_tier,
    COUNT(f.shipment_id)                    AS total_shipments,
    ROUND(SUM(f.revenue_eur), 2)            AS total_revenue,
    ROUND(SUM(f.freight_cost_eur), 2)       AS total_freight_cost,
    ROUND(SUM(f.co2_kg_emitted), 2)         AS total_co2_kg,
    ROUND(AVG(f.lead_time_days), 1)         AS avg_lead_time,
    ROUND(SUM(f.revenue_eur - f.cogs_eur - f.freight_cost_eur), 2) AS total_net_profit,
    ROUND(AVG((f.revenue_eur - f.cogs_eur - f.freight_cost_eur)
        / f.revenue_eur * 100), 2)          AS avg_net_margin_pct,
    ROUND(SUM(f.co2_kg_emitted) /
        SUM(f.revenue_eur) * 1000, 4)       AS co2_per_1000eur_revenue
FROM FACT_SHIPMENTS f
JOIN DIM_ROUTE r ON f.route_key = r.route_key
GROUP BY r.transport_mode, r.co2_tier
ORDER BY avg_net_margin_pct DESC;