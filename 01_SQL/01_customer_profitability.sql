SELECT
    c.company_name,
    c.customer_segment,
    COUNT(f.shipment_id)                    AS total_shipments,
    ROUND(SUM(f.revenue_eur), 2)            AS total_revenue_eur,
    ROUND(SUM(f.freight_cost_eur), 2)       AS total_freight_cost,
    ROUND(SUM(f.revenue_eur - f.cogs_eur - f.freight_cost_eur), 2) AS total_net_profit,
    ROUND(AVG((f.revenue_eur - f.cogs_eur - f.freight_cost_eur)
        / f.revenue_eur * 100), 2)          AS avg_net_margin_pct,
    ROUND(SUM(f.co2_kg_emitted), 2)         AS total_co2_kg
FROM FACT_SHIPMENTS f
JOIN DIM_CUSTOMER c ON f.customer_key = c.customer_key
GROUP BY c.company_name, c.customer_segment
ORDER BY total_net_profit DESC;