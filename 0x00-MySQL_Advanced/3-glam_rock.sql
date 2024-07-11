-- List all Glam rock bands ranked by their longevity
SELECT 
    band_name,
    TIMESTAMPDIFF(YEAR, formed, 2022) AS lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY 
    lifespan DESC;