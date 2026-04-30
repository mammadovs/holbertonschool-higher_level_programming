-- Вычисляет среднюю температуру (в Фаренгейтах) для каждого города
-- Результат сортируется по температуре в порядке убывания
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
