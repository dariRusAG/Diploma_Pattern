import pandas as pd


def get_category(conn):
    return pd.read_sql('''
    SELECT category_name, category_id
    FROM category
    ORDER BY category_name
    ''', conn)


def get_formula(conn):
    return pd.read_sql('''
    SELECT formula_name, formula_value
    FROM formula
    ''', conn)


def get_line(conn):
    return pd.read_sql('''
    SELECT x_first_coord, y_first_coord, x_second_coord, y_second_coord, line_type, x_deviation, y_deviation, line_design
    FROM line
    ''', conn)

def get_measure(conn):
    return pd.read_sql('''
    SELECT measure_name, measure_full_name
    FROM measure
    ORDER BY measure_name
    ''', conn)


def get_category_id(conn, category_name):
    try:
        return pd.read_sql('''SELECT category_id
        FROM category
        WHERE category_name = :category_name
        ''', conn, params={"category_name": category_name}).values[0][0]
    except IndexError:
        return "error"


def get_formula_id(conn, formula_name, formula_value):
    try:
        return pd.read_sql('''SELECT formula_id
        FROM formula
        WHERE formula_name = :formula_name OR formula_value = :formula_value
        ''', conn, params={"formula_name": formula_name, "formula_value": formula_value}).values[0][0]
    except IndexError:
        return "error"

def add_formula(conn, formula_name, formula_value):
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO formula (formula_name, formula_value)
    VALUES (:formula_name, :formula_value)
     ''', {"formula_name": formula_name, "formula_value": formula_value})
    conn.commit()
    return cur.lastrowid


def add_category(conn, category):
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO category(category_name) 
    VALUES (:category)
     ''', {"category": category})
    conn.commit()
    return cur.lastrowid


def delete_category(conn, category_id):
    cur = conn.cursor()
    cur.execute(f'''
    DELETE FROM category
    WHERE category_id=:category_id;
     ''', {"category_id": category_id})
    conn.commit()
    return cur.lastrowid


def update_category(conn, category_id, category_name):
    cur = conn.cursor()
    cur.execute('''
    UPDATE category
    SET 
        category_name= :category_name
    WHERE category_id = :category_id
    ''', {"category_id": category_id, "category_name": category_name})
    return conn.commit()

