import sqlite3

con = sqlite3.connect("DB.sqlite")

con.executescript('''
CREATE TABLE IF NOT EXISTS category (
 category_id INTEGER PRIMARY KEY AUTOINCREMENT,
 category_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS pattern (
 pattern_id INTEGER PRIMARY KEY AUTOINCREMENT,
 pattern_name VARCHAR(70),
 complexity INTEGER,
 picture VARCHAR(70),
 category_id INTEGER,
 FOREIGN KEY (category_id) REFERENCES category (category_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS detail (
 detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
 detail_name VARCHAR(50),
 detail_size VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS pattern_detail (
 pattern_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
 pattern_id INTEGER,
 detail_id INTEGER,
 FOREIGN KEY (pattern_id) REFERENCES pattern (pattern_id) ON DELETE CASCADE,
 FOREIGN KEY (detail_id) REFERENCES detail (detail_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS measure (
 measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
 measure_name VARCHAR(10),
 measure_full_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS detail_measure (
 detail_measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
 detail_id INTEGER,
 measure_id INTEGER,
 FOREIGN KEY (detail_id) REFERENCES detail (detail_id) ON DELETE CASCADE,
 FOREIGN KEY (measure_id) REFERENCES measure (measure_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS formula (
 formula_id INTEGER PRIMARY KEY AUTOINCREMENT,
 formula_name VARCHAR(50),
 formula_value VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS detail_formula (
 detail_formula_id INTEGER PRIMARY KEY AUTOINCREMENT,
 detail_id INTEGER,
 formula_id INTEGER,
 FOREIGN KEY (detail_id) REFERENCES detail (detail_id) ON DELETE CASCADE,
 FOREIGN KEY (formula_id) REFERENCES formula (formula_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS line (
 line_id INTEGER PRIMARY KEY AUTOINCREMENT,
 detail_id INTEGER,
 x_first_coord varchar(70), y_first_coord varchar(70),
 x_second_coord varchar(70), y_second_coord varchar(70),
 x_deviation varchar(70), y_deviation varchar(70),
 FOREIGN KEY (detail_id) REFERENCES detail (detail_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS users (
 users_id INTEGER PRIMARY KEY AUTOINCREMENT,
 users_login VARCHAR(30),
 users_password VARCHAR(30),
 users_role VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS favorite (
 favorite_id INTEGER PRIMARY KEY AUTOINCREMENT,
 users_id INTEGER,
 pattern_id INTEGER,
 FOREIGN KEY (users_id) REFERENCES users (users_id) ON DELETE CASCADE,
 FOREIGN KEY (pattern_id) REFERENCES pattern (pattern_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS param (
 param_id INTEGER PRIMARY KEY AUTOINCREMENT,
 param_name VARCHAR(10),
 param_full_name VARCHAR(50),
 param_value_w VARCHAR(70),
 param_value_m VARCHAR(70),
 info_param VARCHAR(250),
 info_picture VARCHAR(70),
 min_value INTEGER,
 max_value INTEGER
);

CREATE TABLE IF NOT EXISTS user_param (
 user_param_id INTEGER PRIMARY KEY AUTOINCREMENT,
 user_param_value INTEGER,
 users_id INTEGER,
 param_id INTEGER,
 FOREIGN KEY (users_id) REFERENCES users (users_id) ON DELETE CASCADE,
 FOREIGN KEY (param_id) REFERENCES param (param_id) ON DELETE CASCADE
);
''')


con.executescript('''
INSERT INTO category (category_name)
VALUES
('Брюки'),
('Платья'),
('Рубашки'),
('Футболки'),
('Шорты'),
('Юбки');

INSERT INTO pattern (pattern_name, category_id, complexity, picture)
VALUES
('Футболка поло', 4, 2, '/static/image/picture_pattern/Футболка%20поло.jpg'),
('Лонгслив', 4, 1, '/static/image/picture_pattern/Лонгслив.jpg'),
('Классическая футболка', 4, 1, '/static/image/picture_pattern/Классическая%20футболка.jpg'),
('Классическая рубашка', 3, 3, '/static/image/picture_pattern/Классическая%20рубашка.jpg'),
('Юбка-карандаш', 6, 1, '/static/image/picture_pattern/Юбка-карандаш.jpg'),
('Юбка-солнце', 6, 1, '/static/image/picture_pattern/Юбка-солнце.jpg'),
('Классические брюки', 1, 2, '/static/image/picture_pattern/Классические%20брюки.jpg'),
('Брюки бананы', 1, 3, '/static/image/picture_pattern/Брюки%20бананы.jpg'),
('Брюки скинни', 1, 3, '/static/image/picture_pattern/Брюки%20скинни.jpg'),
('Брюки карго', 1, 4, '/static/image/picture_pattern/Брюки%20карго.jpg'),
('Платье-футляр', 2, 5, '/static/image/picture_pattern/Платье-футляр.jpg'),
('Платье сафари', 2, 5, '/static/image/picture_pattern/Платье%20сафари.jpg');

INSERT INTO pattern_detail (pattern_id, detail_id)
VALUES
(5, 1), (5, 2),
(2, 3), (2, 4),
(1, 3), (1, 5), (1, 6),
(12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13);

INSERT INTO detail (detail_name, detail_size)
VALUES
('Передняя половина', '60'),
('Задняя половина', '60'),
('Основа верха', '72'),
('Длинный рукав', '62'),
('Короткий рукав', '33'),
('Воротник', ''),
('Перед', ''),
('Спинка', ''),
('Заднее полотнище юбки', '66'),
('Переднее полотнище юбки', '66'),
('Карман', ''),
('Шлевка', ''),
('Манжета', '');

INSERT INTO measure (measure_name, measure_full_name)
VALUES
('ОГ', 'Обхват груди'),
('ОТ', 'Обхват талии'),
('ОБ', 'Обхват бедер'),
('ОШ', 'Обхват шеи'),
('ОПл', 'Обхват плеча'),
('ОЗ', 'Обхват запястья'),
('ВБ', 'Высота бедер'),
('ДИ', 'Длина изделия'),
('ДТС', 'Длина до талии спинки'),
('ДПл', 'Длина плеча'),

('ОБед', 'Обхват бедра'),
('ОК', 'Обхват колена'),
('ОИ', 'Обхват икры'),
('ОЩ', 'Обхват щиколотки'),
('ОПСт', 'Обхват подъема стопы'),
('ОГол', 'Обхват головы'),
('ВТ', 'Высота линии талии'),
('ВК', 'Высота коленной точки'),
('ВПл', 'Высота плечевой точки'),
('ВЯ', 'Высота подъягодичной складки'),
('ВПлК', 'Высота плеча косая сзади'),
('ШГ', 'Ширина груди'),
('ШПл', 'Ширина плечевого ската'),
('ШС', 'Ширина спины'),
('ЦГ', 'Центр груди'),
('ДРЗ', 'Длина руки до запястья'),
('ДТБ', 'Длина от талии до бедер'),
('ДС', 'Расстояние от линии талии до плоскости сидения'),
('ДН', 'Длина ноги по внутренней поверхности'),
('ДТС2', 'Расстояние от линии талии сзади до точки основания шеи'),
('ДТПТС', 'Дуга верхней части туловища через точку основания шеи'),
('ВЛТБ', 'Расстояние от линии талии до пола сбоку'),
('ВЛТП', 'Расстояние от линии талии до пола спереди'),
('Р', 'Рост');

INSERT INTO detail_measure (detail_id, measure_id)
VALUES
(1, 2), (1, 3), (1, 7), (1, 8),
(2, 2), (2, 3), (2, 7), (2, 8),
(3, 1), (3, 2), (3, 4), (3, 5), (3, 8), (3, 9), (3, 10),
(4, 1), (4, 5), (4, 6), (4, 8),
(5, 1), (5, 5), (5, 8),
(6, 1), (6, 4),
(7, 1), (7, 2), (7, 4), (7, 9),
(8, 1), (8, 2), (8, 4), (8, 9),
(9, 2), (9, 8),
(10, 2), (10, 8),
(13, 1), (13, 2), (13, 4);
''')


con.executescript('''
INSERT INTO formula (formula_name, formula_value)
VALUES
('Длина', 'ДИ + 1'),
('Середина', 'ДИ - ВБ + 1'),
('Ширина', '0.25 * ОБ + 1.5'),
('Боковая_вытачка', '0.25 * (ОБ - ОТ)'),
('Вытачка_переда', 'ДИ - 0.5 * ВБ + 1'),
('Подъем_талии', 'ДИ + 1.5 + 1'),
('Ширина_верха', 'ОГ * 0.25 - 0.05 + 1'),
('Линия_талии', '0.25 * ОТ + 1.5'),
('Боковой_шов', 'ДИ - ДТС + 2'),
('Горловина', 'ОШ / 6 + 2'),
('Плечо', 'ДПл'),
('Угол_проймы', '0.5 * (0.33 * ОПл + 0.5)'),
('Глубина_проймы', '0.1 * ОГ + 10.5'),
('Высота_оката', '0.5 * ОПл + 1.5'),
('Низ_рукава', '0.5 * ОЗ + 2'),
('Линия_оката', 'ДИ - 0.75 * (0.1 * ОГ + 10.5) + 3'),
('Половина_длины_горловины', '0.1 * 0.25 * ОГ + 3.14 * 0.5 * (ОШ / 6 + 1.5) + 1'),
('Длина_короткого_рукава', 'ДИ * 0.5 + 1'),
('Линия_оката_короткого_рукава', 'ДИ * 0.5 - 0.75 * (0.1 * ОГ + 10.5) + 1.5'),
('Длина_до_талии', 'ДТС + 1'),
('Отступ_воротника', '4 * Корень(Степень(0.1 * ОГ + 10.5, 2) - 8 * 0.1 * ОГ + 10.5) / (0.1 * ОГ + 10.5 - 4)'),
('Пробник', '-1 * ((-14 * ДИ - 5256 + 31 * ОТ - ДИ * ОТ) / (4 * ДИ + 12))'),
('Коэффициент_диагонали_юбки', '(Корень(Степень(1 - ДИ - 4, 2) + Степень(44 - 0.25 * ОТ - 4.5, 2)) - ДИ + 4) - (Корень(Степень(1 - ДИ - 4, 2) + Степень(44 - 0.25 * ОТ - 4.5, 2)) - ДИ + 4) / Корень(Степень(1 - ДИ - 4, 2) + Степень(44 - 0.25 * ОТ - 4.5, 2))'),
('Пробник_2', '-1 * ((-14 * ДИ - 2570 + 14 * ОТ - ДИ * ОТ) / (4 * ДИ + 12))');

INSERT INTO detail_formula (detail_id, formula_id)
VALUES
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
(3, 1), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13),
(4, 1), (4, 14), (4, 15), (4, 16),
(5, 14), (5, 16), (5, 18), (5, 19),
(6, 17),
(7, 8), (7, 10), (7, 13), (7, 20), (7, 21),
(8, 8), (8, 10), (8, 13), (8, 20),
(9, 1), (9, 8), (9, 23),
(10, 1), (10, 8), (10, 22), (10, 23), (10, 24),
(13, 8), (13, 10), (13, 13);
''')


con.executescript('''
INSERT INTO line (
    detail_id,
    x_first_coord, y_first_coord, 
    x_second_coord, y_second_coord,
    x_deviation, y_deviation)
VALUES
(1, '1', 'Длина', '1', '1', '', ''),
(1, '1', '1', 'Ширина', '1', '', ''),
(1, 'Ширина', '1', 'Ширина', 'Середина', '', ''),
(1, '(Ширина - 1) * 0.5 - Боковая_вытачка * 0.6 * 0.5', 'Длина', 'Ширина * 0.5', 'Длина - 2 * Боковая_вытачка', '', ''),
(1, '(Ширина - 1) * 0.5 + Боковая_вытачка * 0.6 * 0.5', 'Длина + 0.1', 'Ширина * 0.5', 'Длина - 2 * Боковая_вытачка', '', ''),
(1, 'Ширина', 'Середина', 'Ширина - 0.5 * Боковая_вытачка', 'Подъем_талии', '1.1', '1.1'),
(1, '1', 'Длина', 'Ширина - 0.5 * Боковая_вытачка', 'Подъем_талии', '1.3', '0.98'),

(2, 'Ширина', '1', '1', '1', '', ''),
(2, 'Ширина', 'Длина', 'Ширина', '1', '', ''),
(2, '1', '1', '1', 'Середина', '', ''),
(2, '(Ширина - 1) * 0.5 - Боковая_вытачка * 0.4 * 0.5', 'Длина + 0.2', '(Ширина - 1) * 0.5 - 0.5', 'Вытачка_переда', '', ''),
(2, '(Ширина - 1) * 0.5 + Боковая_вытачка * 0.4 * 0.5', 'Длина', '(Ширина - 1) * 0.5 - 0.5',  'Вытачка_переда', '', ''),
(2, '1', 'Середина', '0.5 * Боковая_вытачка + 1', 'Подъем_талии', '0.3', '1.1'),
(2, 'Ширина', 'Длина', '0.5 * Боковая_вытачка + 1', 'Подъем_талии', '0.7', '0.98'),

(3, '1', '1', 'Ширина_верха', '1', '', ''),
(3, '1', 'Длина', '1', '1', '', ''),
(3, 'Горловина', 'Длина + 2', 'Горловина + Корень(Степень(Плечо, 2) - 9) - 1', 'Длина - 1', '', ''),
(3, '1', 'Длина', 'Горловина', 'Длина + 2', '1.4', '0.98'),
(3, 'Горловина', 'Длина + 2', '1', 'Длина + 1 - (Горловина - 2.5)', '1.66', '0.95'),
(3, 'Горловина + Корень(Степень(Плечо, 2) - 9) - 1', 'Длина - 1', 'Ширина_верха', 'Длина - Глубина_проймы', '0.75, 0.77', '0.92, 0.89'),
(3, 'Ширина_верха', 'Длина - Глубина_проймы', 'Ширина_верха', '1', '0.84, 0.8, 0.86, 1.01', '0.9, 0.8, 0.8, 0.9'),

(4, 'Высота_оката', 'Длина', 'Высота_оката', '1', '', ''),
(4, 'Высота_оката - Низ_рукава', '1', 'Высота_оката', '1', '', ''),
(4, '1', 'Линия_оката', 'Высота_оката - Низ_рукава', '1', '1.5', '1.4'),
(4, 'Высота_оката', 'Длина', '1', 'Линия_оката', '1, 1', '1.08, 0.94'),

(5, 'Высота_оката + 1.5', 'Длина_короткого_рукава + 0.5', '1', 'Линия_оката_короткого_рукава', '0.75, 0.5, 1.4', '1.25, 1.15, 0.6'),
(5, 'Высота_оката + 1.5', 'Длина_короткого_рукава + 0.5', 'Высота_оката * 2 + 0.5 + 1', 'Линия_оката_короткого_рукава', '1.1, 1.11, 0.9', '1.2, 1.1, 0.6'),
(5, '1', '1', 'Высота_оката * 2 + 0.5 + 1', '1', '1', '2'),
(5, '1', 'Линия_оката_короткого_рукава', '1', '1', '', ''),
(5, 'Высота_оката * 2 + 0.5 + 1', 'Линия_оката_короткого_рукава', 'Высота_оката * 2 + 0.5 + 1', '1', '', ''),

(6, '1', '1', '1', '4', '', ''),
(6, '1', '4', 'Половина_длины_горловины * 0.5 + 1', '4', '', ''),
(6, '1', '1', 'Половина_длины_горловины * 0.5 + 1', '1', '', ''),
(6, 'Половина_длины_горловины * 0.5 + 1', '4', 'Половина_длины_горловины - 0.5', '4.5', '1, 1', '0.95, 0.98'),
(6, 'Половина_длины_горловины * 0.5 + 1', '1', 'Половина_длины_горловины + 1.5', '1.5', '1, 1', '0.85, 0.95'),
(6, 'Половина_длины_горловины - 0.5', '4.5', 'Половина_длины_горловины + 1.5', '1.5', '1.04, 1.08, 1.05, 1.025', '1.2, 1.24, 1.05, 1'),
(6, '1', '11', '1', '6', '', ''),
(6, '1', '6', 'Половина_длины_горловины - 0.5', '4.5', '1, 1, 1.05, 1.05', '1.03, 1.1, 1.2, 1.14'),
(6, '1', '11', 'Половина_длины_горловины + 0.5', '13', '1, 1, 1, 1', '0.97, 0.92, 0.95, 0.97'),
(6, 'Половина_длины_горловины + 0.5', '13', 'Половина_длины_горловины - 0.5', '4.5', '', ''),

(7, '1', 'Длина_до_талии - 8 - 16 / (Глубина_проймы - 4)', '1 + Отступ_воротника', 'Длина_до_талии - 8', '1', '0.99'),
(7, '1 + Отступ_воротника', 'Длина_до_талии - 8', 'Отступ_воротника + Горловина + 0.5', 'Длина_до_талии + 5', '1.18, 1.12, 1.05', '0.95, 0.93, 0.98'),
(7, 'Отступ_воротника + Горловина + 0.5', 'Длина_до_талии + 5', 'Отступ_воротника + Горловина + 28.5', 'Длина_до_талии - 1', '', ''),
(7, 'Отступ_воротника + Горловина + 28.5', 'Длина_до_талии - 1', 'Отступ_воротника + 0.75 * (Горловина + 27.5) + 0.25 * (Линия_талии + 0.5) + 1', 'Длина_до_талии - Глубина_проймы - 4', '', ''),
(7, 'Отступ_воротника + 0.75 * (Горловина + 27.5) + 0.25 * (Линия_талии + 0.5) + 1', 'Длина_до_талии - Глубина_проймы - 4', 'Отступ_воротника + Линия_талии + 1.5', 'Длина_до_талии - Глубина_проймы - 5 - (Длина_до_талии - Глубина_проймы - 6) * 5 / 8', '0.82', '1.41'),
(7, 'Отступ_воротника + Линия_талии + 1.5', '1', 'Отступ_воротника + Линия_талии + 1.5', 'Длина_до_талии - Глубина_проймы - 5 - (Длина_до_талии - Глубина_проймы - 6) * 5 / 8', '', ''),

(7, 'Отступ_воротника + Линия_талии + 1.5', '1', 'Отступ_воротника - 0.5', '1', '', ''),
(7, 'Отступ_воротника - 0.5', '1', 'Отступ_воротника - 0.5', 'Длина_до_талии - Глубина_проймы - 3', '', ''),
(7, 'Отступ_воротника - 0.5', 'Длина_до_талии - Глубина_проймы - 3', '1', 'Длина_до_талии - 8 - 16 / (Глубина_проймы - 4)', '', ''),

(7, 'Отступ_воротника + 1.2', '1.5', 'Отступ_воротника + 0.8', '1.5', '', ''),
(7, 'Отступ_воротника + 1', '1.5', 'Отступ_воротника + 1', '3.5', '', ''),
(7, 'Отступ_воротника + 1.2', '3.5', 'Отступ_воротника + 0.8', '3.5', '', ''),
(7, 'Отступ_воротника + 1.2', 'Длина_до_талии - (Глубина_проймы + 5) - 0.5', 'Отступ_воротника + 0.8', 'Длина_до_талии - (Глубина_проймы + 5) - 0.5', '', ''),
(7, 'Отступ_воротника + 1', 'Длина_до_талии - (Глубина_проймы + 5) - 0.5', 'Отступ_воротника + 1', 'Длина_до_талии - (Глубина_проймы + 5) - 2.5', '', ''),
(7, 'Отступ_воротника + 1.2', 'Длина_до_талии - (Глубина_проймы + 5) - 2.5', 'Отступ_воротника + 0.8', 'Длина_до_талии - (Глубина_проймы + 5) - 2.5', '', ''),
(7, 'Отступ_воротника + 1.2', '0.5 * (Длина_до_талии - Глубина_проймы) - 1', 'Отступ_воротника + 0.8', '0.5 * (Длина_до_талии - Глубина_проймы) - 1', '', ''),
(7, 'Отступ_воротника + 1', '0.5 * (Длина_до_талии - Глубина_проймы) - 1', 'Отступ_воротника + 1', '0.5 * (Длина_до_талии - Глубина_проймы) - 3', '', ''),
(7, 'Отступ_воротника + 1.2', '0.5 * (Длина_до_талии - Глубина_проймы) - 3', 'Отступ_воротника + 0.8', '0.5 * (Длина_до_талии - Глубина_проймы) - 3', '', ''),
(7, 'Отступ_воротника + 2.5', '1', 'Отступ_воротника + Горловина + (1 + 57 * (3 / Корень(784 + 25))) / (2 + 2 * (3 / Корень(784 + 25)))', 'Длина_до_талии + (5 - 3 / Корень(784 + 25)) / (1 + 3 / Корень(784 + 25))', '0.9, 0.81, 0.74, 0.56, 0.74, 0.89, 0.9, 0.93, 0.97', '1, 1, 1, 1.07, 1, 1, 1, 1, 1'),

(8, '1', 'Длина_до_талии', 'Горловина + 0.5', 'Длина_до_талии + 3', '1.8', '0.968'),
(8, 'Горловина + 0.5', 'Длина_до_талии + 3', 'Горловина + 0.5 + 28', 'Длина_до_талии - 1', '', ''),
(8, 'Горловина + 0.5 + 28', 'Длина_до_талии - 1', '0.75 * (Горловина + 27.5) + 0.25 * (Линия_талии + 0.5) + 1', 'Длина_до_талии - (Глубина_проймы + 5)', '', ''),
(8, '0.75 * (Горловина + 27.5) + 0.25 * (Линия_талии + 0.5) + 1', 'Длина_до_талии - (Глубина_проймы + 5)', 'Линия_талии + 1.5', 'Длина_до_талии - Глубина_проймы - 5 - (Длина_до_талии - Глубина_проймы - 6) * 5 / 8', '0.8', '1.4'), 
(8, 'Линия_талии + 1.5', 'Длина_до_талии - Глубина_проймы - 5 - (Длина_до_талии - Глубина_проймы - 6) * 5 / 8', 'Линия_талии + 1.5', '1', '', ''),

(8, '1', '1', 'Линия_талии + 1.5', '1', '', ''),
(8, '1', 'Длина_до_талии', '1', '1', '', ''),

(9, '1', 'Длина', 'Линия_талии + 3.5', 'Длина + 3', '1, 1, 1', '0.988, 0.98, 0.975'),
(9, 'Линия_талии + 3.5', 'Длина + 3', '(Линия_талии + 3 + Коэффициент_диагонали_юбки * 44) / (1 + Коэффициент_диагонали_юбки)', '(Длина + 3 + Коэффициент_диагонали_юбки) / (1 + Коэффициент_диагонали_юбки)', '', ''),
(9, '1', '1', '(Линия_талии + 3 + Коэффициент_диагонали_юбки * 44) / (1 + Коэффициент_диагонали_юбки)', '(Длина + 3 + Коэффициент_диагонали_юбки) / (1 + Коэффициент_диагонали_юбки)', '1, 1, 1', '0.55, 0.5, 0.45'),
(9, '1', 'Длина', '1', '1', '', ''),
(9, '(Линия_талии + 4.5) * 0.5', '(Длина + Длина + 0.7) * 0.5', '(Линия_талии + 4.5) * 0.5 + 1', '(Длина + Длина + 0.9) * 0.5 - 11', '', ''),
(9, '(Линия_талии + 4.5) * 0.5 - 1', '(Длина + Длина + 0.5) * 0.5', '(Линия_талии + 4.5) * 0.5 + 1', '(Длина + Длина + 0.9) * 0.5 - 11', '', ''),
(9, '(Линия_талии + 4.5) * 0.5 + 1', '(Длина + Длина + 0.9) * 0.5', '(Линия_талии + 4.5) * 0.5 + 1', '(Длина + Длина + 0.9) * 0.5 - 11', '', ''),

(10, '2.5', 'Длина', 'Линия_талии + 3', 'Длина + 3', '1, 1, 1', '0.988, 0.98, 0.975'),
(10, '2.5', 'Длина', '2.5', '1', '', ''),
(10, '2.5', '1', '(Линия_талии + 3 + Коэффициент_диагонали_юбки * 44) / (1 + Коэффициент_диагонали_юбки)', '(Длина + 3 + Коэффициент_диагонали_юбки) / (1 + Коэффициент_диагонали_юбки)', '1, 1, 1', '0.55, 0.5, 0.45'),
(10, 'Линия_талии + 3', 'Длина + 3', '(Линия_талии + 3 + Коэффициент_диагонали_юбки * 44) / (1 + Коэффициент_диагонали_юбки)', '(Длина + 3 + Коэффициент_диагонали_юбки) / (1 + Коэффициент_диагонали_юбки)', '', ''),

(10, '1', 'Длина', '4', 'Длина', '', ''),
(10, '4', 'Длина', '4', 'Длина - 19', '', ''),
(10, '1', 'Длина - 19', '4', 'Длина - 19', '', ''),
(10, '1', 'Длина', '1', 'Длина - 19', '', ''),

(10, 'Пробник - 22 - 1.2', 'Длина - 30', 'Пробник + 1.2', 'Длина - 30', '', ''),
(10, 'Пробник - 22 - 1.2', 'Длина  - 6', 'Пробник - 22 - 1.2', 'Длина - 30', '', ''),
(10, 'Пробник - 22 - 1.2', 'Длина  - 6', 'Пробник - 22 + 4.5 - 1.2', 'Длина  - 6', '', ''),
(10, 'Пробник - 22 + 4.5 - 1.2', 'Длина  - 6', 'Пробник_2 + 1.2', 'Длина - 13', '', ''),

(10, '2.5 - 0.2', 'Длина - 16', '2.5 + 0.2', 'Длина - 16', '', ''),
(10, '2.5 - 0.2', 'Длина - 14', '2.5 + 0.2', 'Длина - 14', '', ''),
(10, '2.5 - 0.2', 'Длина - 8', '2.5 + 0.2', 'Длина - 8', '', ''),
(10, '2.5 - 0.2', 'Длина - 6', '2.5 + 0.2', 'Длина - 6', '', ''),

(11, '1', '1', '1', '13.5', '', ''),
(11, '1', '13.5', '13.5', '13.5', '', ''),
(11, '13.5', '13.5', '13.5', '1', '', ''),
(11, '13.5', '1', '1', '1', '', ''),
(11, '5.25', '15.5', '9.25', '15.5', '', ''),
(11, '9.25', '15.5', '9.25', '11.5', '', ''),
(11, '9.25', '11.5', '7.25', '9.5', '', ''),
(11, '7.25', '9.5', '5.25', '11.5', '', ''),
(11, '5.25', '11.5', '5.25', '15.5', '', ''),
(11, '7.25', '13.5', '7.25', '11.5', '', ''),
(11, '7.05', '11.5', '7.45', '11.5', '', ''),

(12, '1', '3', '1', '16.5', '', ''),
(12, '1', '16.5', '5.5', '16.5', '', ''),
(12, '5.5', '16.5', '5.5', '3', '', ''),
(12, '5.5', '3', '3.25', '1', '', ''),
(12, '3.25', '1', '1', '3', '', ''),
(12, '3.25', '3', '3.25', '5', '', ''),
(12, '3.05', '3', '3.45', '3', '', ''),
(12, '3.05', '5', '3.45', '5', '', ''),

(13, '1', '1', '7', '1', '', ''),
(13, '7', '1', '7', 'Корень(Степень(0.25 * (Горловина - Линия_талии) + 5, 2) + Степень(Глубина_проймы + 5, 2)) + 1', '', ''),
(13, '1', 'Корень(Степень(0.25 * (Горловина - Линия_талии) + 5, 2) + Степень(Глубина_проймы + 5, 2)) + 1', '7', 'Корень(Степень(0.25 * (Горловина - Линия_талии) + 5, 2) + Степень(Глубина_проймы + 5, 2)) + 1', '', ''),
(13, '1', '1', '1', 'Корень(Степень(0.25 * (Горловина - Линия_талии) + 5, 2) + Степень(Глубина_проймы + 5, 2)) + 1', '', ''),
(13, '4', 'Корень(Степень(0.25 * (Горловина - Линия_талии) + 5, 2) + Степень(Глубина_проймы + 5, 2)) + 1', '4', '1', '', '');
''')


con.executescript('''
INSERT INTO users (users_login, users_password, users_role)
VALUES
('nakao.pd','1234567','admin'),
('srf_adlr','qwerty','admin'),
('test','testtest','user');

INSERT INTO param (param_name, param_full_name, param_value_w, param_value_m, info_param, info_picture, min_value, max_value)
VALUES
('ОГ', 'Обхват груди', '84, 88, 92, 96, 100, 104', '88, 92, 96, 100, 104, 108', 
'Сантиметровая лента проходит через выступающие точки грудных желез, через задние углы подмышечных впадин и через выступающие точки лопаток, замыкается на середине спины и удерживается. Сзади сантиметровая лента должна быть приподнята', 
'/static/image/picture_parameters/Обхват%20груди.gif', 76, 116),

('ОТ', 'Обхват талии', '65.5, 67.3, 71.3, 75.5, 80, 84.1', '76, 79, 82, 84, 91, 98', 
'Естественную линию талии фиксируют шнуром, она должна быть расположена на теле строго горизонтально', 
'/static/image/picture_parameters/Обхват%20талии.gif', 57, 100),

('ОБ', 'Обхват бедер', '96.3, 96.5, 99.8, 103.2, 106.7, 110.2', '93.8, 96, 98.3, 101.7, 104, 109.5', 
'Сантиметровая лента проходит горизонтально по наиболее выступающим точкам ягодиц, замыкается и удерживается спереди', 
'/static/image/picture_parameters/Обхват%20бедер.gif', 79, 113),

('ОШ', 'Обхват шеи', '35.5, 35.9, 36.6, 37.3, 38, 38.8', '39.2, 39.8, 40.5, 41.2, 42.1, 43.2', 
'Сантиметровая лента должна проходить по основанию шеи и замыкаться сбоку', 
'/static/image/picture_parameters/Обхват%20шеи.gif', 32, 45),

('ОПл', 'Обхват плеча', '26.8, 27.6, 29.1, 30.5, 31.8, 33', '28.3, 29.3, 30.2, 32.3, 33.8, 34.7', 
'Эта мерка снимается горизонтально на уровне задних углов подмышечных впадин. Сантиметровая лента накладывается очень плотно', 
'/static/image/picture_parameters/Обхват%20плеча.gif', 24, 36),

('ОЗ', 'Обхват запястья', '16, 16.1, 16.4, 16.7, 17.0, 17.2', '17.7, 18, 18.3, 18.6, 19, 19.3', 
'Измеряется на уровне запястья – основание кисти руки', 
'/static/image/picture_parameters/Обхват%20запястья.gif', 14, 20),

('ВБ', 'Высота бедер', '20.8, 21, 21.2, 21.4, 21.5, 21.7', '19.2, 19.6, 20, 20.4, 20.7, 21', 
'Измеряется от 7-го шейного позвонка до уровня наиболее выступающих точек ягодиц', 
'/static/image/picture_parameters/Высота%20бедер.gif', 18, 23),

('ДТС', 'Длина до талии спинки', '41.2, 41.3, 41.4, 41.4, 41.5, 41.6', '45.8, 46, 46.3, 46.4, 46.5, 47', 
'Измеряется от 7-го шейного позвонка так, чтобы она свисала вдоль позвоночника. Другой рукой прижать ее на уровне линии талии к горизонтально наложенной ленте для талии и считывать мерку у нижнего края ленты для талии', 
'/static/image/picture_parameters/Длина%20до%20талии%20спинки.gif', 37, 49),

('ДТП', 'Длина до талии переда', '43, 43.8, 44.4, 44.9, 45.4, 46', '46.4, 47, 47.5, 48, 48.5, 49.3', 
'Измеряется от 7-го шейного позвонка, вдоль основания шеи сзади сантиметровая лента проходит до наиболее выступающей точке груди, откуда свисает вертикально вниз до ленты для талии, к которой ее следует прижать', 
'/static/image/picture_parameters/Длина%20до%20талии%20переда.gif', 38, 50),

('ДПл', 'Длина плеча', '13.5, 13.5, 13.6, 13.6, 13.7, 13.8', '14.4, 14.6, 14.8, 15, 15.2, 15.4', 
'Измеряют от высшей точки проектируемого плечевого шва (у основания шеи) до конечной точки проектируемого плечевого шва', 
'/static/image/picture_parameters/Длина%20плеча.gif', 11, 17),

('ДИ', 'Длина изделия', '', '', 
'Измеряется от 7-го шейного позвонка до выбранной длины модели', 
'/static/image/picture_parameters/Длина%20изделия.gif', 10, 110),

('ОБед', 'Обхват бедра', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ОК', 'Обхват колена', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ОИ', 'Обхват икры', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ОЩ', 'Обхват щиколотки', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ОПСт', 'Обхват подъема стопы', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ОГол', 'Обхват головы', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ВТ', 'Высота линии талии', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ВК', 'Высота коленной точки', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ВПл', 'Высота плечевой точки', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ВЯ', 'Высота подъягодичной складки', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ВПлК', 'Высота плеча косая сзади', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ШГ', 'Ширина груди', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ШПл', 'Ширина плечевого ската', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ШС', 'Ширина спины', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ЦГ', 'Центр груди', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ДРЗ', 'Длина руки до уровня обхвата запястья', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ДТБ', 'Длина от талии до бедер', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ДС', 'Расстояние от линии талии до плоскости сидения', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ДН', 'Длина ноги по внутренней поверхности', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ДТС2', 'Расстояние от линии талии сзади до точки основания шеи', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ДТПТС', 'Дуга верхней части туловища через точку основания шеи', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ВЛТБ', 'Расстояние от линии талии до пола сбоку', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('ВЛТП', 'Расстояние от линии талии до пола спереди', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100),
('Р', 'Рост', '0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0', '', '', 0, 100);

INSERT INTO favorite (users_id, pattern_id)
VALUES
(3, 1), (3, 4), (3, 6), (3, 7), (3, 11);

INSERT INTO user_param (users_id, param_id, user_param_value)
VALUES
(3, 1, 108), 
(3, 2, 80), 
(3, 3, 105), 
(3, 4, 37), 
(3, 5, 30), 
(3, 6, 16), 
(3, 7, 21), 
(3, 8, 42), 
(3, 9, 44), 
(3, 10, 13),

(3, 12, 100), 
(3, 13, 80), 
(3, 14, 99), 
(3, 15, 37), 
(3, 16, 30), 
(3, 17, 16), 
(3, 18, 21), 
(3, 19, 42), 
(3, 20, 13),
(3, 21, 10), 
(3, 22, 11), 
(3, 23, 12), 
(3, 24, 13), 
(3, 25, 14), 
(3, 26, 15), 
(3, 27, 16), 
(3, 28, 17), 
(3, 29, 18), 
(3, 30, 19),
(3, 31, 20),
(3, 32, 37), 
(3, 33, 30), 
(3, 34, 16), 
(3, 35, 165);            
''')

# сохраняем информацию в базе данных
con.commit()
