select_all_female_bears_return_name_and_age =
SELECT age, anme FROM bears WHARE gender = 'female'


select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT names bear_order,FROM  bears ORDER BY name ASC;
    Write your SQL query here
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELCT names, ages FROM bears OREDER BY ages ASC WHERE alive = '1' 
    Write your SQL query here
"""

select_oldest_bear_and_returns_name_and_age = """
SELECT names, ages, FROM bears WHERE oldest_bear = 'Sergeant Brown'
    Write your SQL query here
"""
select_youngest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
WHERE alive = 1 -- Assuming 1 represents alive in your schema
ORDER BY age ASC
LIMIT 1;

    Write your SQL query here
""

    