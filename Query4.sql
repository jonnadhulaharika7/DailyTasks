-- write a query to provide the date for nth occurence of sunday in fure from given date
-- datepart
-- sunday-1
-- monday-2
-- friday-6
-- saturday-7

DO $$
DECLARE
    today_date DATE := DATE '2022-01-03';
    n INT := 3;
BEGIN
    RAISE NOTICE 'Result: %',
        today_date
        + ((6 - EXTRACT(DOW FROM today_date)::INT + 7) % 7)
        + ((n - 1) * 7);
END $$;
