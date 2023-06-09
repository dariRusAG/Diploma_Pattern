from app import app
from flask import render_template, request, session
from functions.data_check import is_correct_params, is_correct_login_password
from models.scheme_model import get_info_param
from utils import get_db_connection
from models.user_profile_model import *


@app.route('/user_profile', methods=['GET', 'POST'])
def user_profile():
    conn = get_db_connection()
    error_param = [[],[]]
    param_name = []

    df_param = get_param(conn, session['user_id'])

    for i in range(len(df_param)):
        param_name.append(df_param.loc[i, "param_name"])

    # Если нажата кнопка "Сохранить изменения"
    if request.values.get('save'):
        new_data_user = request.form.getlist('data_user')
        if not new_data_user:
            new_data_user = get_data_user(conn, session['user_id']).values[0]
        if is_correct_login_password(conn, new_data_user[0], new_data_user[1], session['user_id']) != "True":
            error_param[1].append(is_correct_login_password(conn, new_data_user[0], new_data_user[1], session['user_id']))
        else:
            update_data_user(conn, session['user_id'], new_data_user)

        def update(elem_, new_param_user_):
            update_param_user(conn, session['user_id'], elem_, new_param_user_)
            error_param[0].append('upd')

        new_param_user = request.form.getlist('param_user')
        if len(new_param_user) == 10:
            error_param.append('осн')
            new_param_name = param_name[0:10]
        else:
            error_param.append('доп')
            new_param_name=param_name[10:]

        for elem in range(len(new_param_user)):
            if is_correct_params(conn, new_param_user[elem], new_param_name[elem]) != "True":
                error_param[0].append(new_param_user[elem])
                error_param[1].append(is_correct_params(conn, new_param_user[elem], new_param_name[elem]))
            else:
                update(int(get_param_id(conn, str(new_param_name[elem]))), new_param_user[elem])

    df_data_user = get_data_user(conn, session['user_id'])
    df_param_user = get_param_user(conn, session['user_id'])
    df_info_param = get_info_param(conn)

    html = render_template(
        'user_profile.html',

        user=session['user_id'],
        info_param=df_info_param,
        data_user=df_data_user,
        param_user=df_param_user,
        error_param=error_param,

        # Функции
        len=len
    )

    return html