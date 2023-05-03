import pandas as pd


# Вывод данных выкройки для построения
def get_scheme_pattern(conn, index):
    return pd.read_sql(f'''
    SELECT
        pattern_id AS ID,
        pattern_name AS Название, 
        category_name AS Категория,
        picture AS Изображение  
    FROM pattern
    JOIN category USING (category_id)
    WHERE pattern_id == {index}
    ''', conn)


# Вывод всех мерок выкройки
def get_measure_detail(conn, index):
    return pd.read_sql(f'''
    WITH get_all_measure(detail_id, measure_name, measure_full_name)
    AS (
        SELECT 
            detail_id, 
            group_concat(measure_name, ', ') AS measure_name,
            group_concat(measure_full_name, ', ') AS measure_full_name
        FROM detail_measure 
        JOIN measure USING (measure_id)
        GROUP BY detail_id
    )
    SELECT 
        detail_name AS Название_детали,
        measure_name AS Обозначение,
        measure_full_name AS Полное_название
    FROM pattern_detail 
    JOIN get_all_measure USING (detail_id) 
    JOIN detail USING (detail_id) 
    WHERE pattern_id == {index}
    ''', conn)


# Вывод параметров пользователя для построения
def get_param_user(conn, user_id):
    return pd.read_sql(f'''
    SELECT 
        param_name AS Обозначение, 
        user_param.[param_value] AS Значение
    FROM param
    JOIN user_param USING (param_id)
    WHERE users_id = {user_id}
    ''', conn)