import sqlite3
import pandas as pd
import load_excel


conn = sqlite3.connect('Project_data.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

# create tables
conn.execute('CREATE TABLE continent (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
conn.execute('CREATE TABLE country( id INTEGER PRIMARY KEY AUTOINCREMENT, continent_id INTEGER, name TEXT, population INTEGER, '
             'population_density INTEGER, land_area INTEGER, energy_consumption INTEGER, FOREIGN KEY(continent_id) '
             'REFERENCES continent(id) )')
conn.execute('CREATE TABLE livestock( id INTEGER PRIMARY KEY AUTOINCREMENT, country_id INTEGER, cattle INTEGER, sheep INTEGER, '
             'goat INTEGER, pig INTEGER, eguines INTEGER, buffallo INTEGER, camel INTEGER, FOREIGN KEY(country_id) REFERENCES'
             ' country(id))')

file = pd.ExcelFile('Open-source-data.xls')
continents = file.sheet_names
for continent in continents:
    name = continent
    cur.execute('INSERT INTO continent VALUES(NULL, ?)', [name])
    conn.commit()

sheets = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for sheet in sheets:
    countries = load_excel.which_sheet(sheet, 1)
    populations = load_excel.which_sheet(sheet, 2)
    population_densities = load_excel.which_sheet(sheet, 3)
    land_areas = load_excel.which_sheet(sheet, 4)
    energy_consumptions = load_excel.which_sheet(sheet, 12)
    indexes = load_excel.index_array(sheet, 1)
    for index in indexes:
        continent_id = sheet
        name = countries[index]
        population = 1
        population_density = 1
        land_area = 1
        energy_consumption = 1
        cur.execute('INSERT INTO country VALUES(NULL, ?, ?, ?, ?, ?, ?)', (continent_id, name, population, population_density, land_area, energy_consumption))
        conn.commit()
id_country = 0
for sheet in sheets:
    cattles = load_excel.which_sheet(sheet, 5)
    sheeps = load_excel.which_sheet(sheet, 6)
    goats = load_excel.which_sheet(sheet, 7)
    pigs = load_excel.which_sheet(sheet, 8)
    eguiness = load_excel.which_sheet(sheet, 9)
    buffallos = load_excel.which_sheet(sheet, 10)
    camels = load_excel.which_sheet(sheet, 11)
    countries = load_excel.which_sheet(sheet, 1)
    index = 0
    for livestock in countries:
        id_country = id_country + 1
        country_id = id_country
        cattle = 1
        sheep = 1
        goat = 1
        pig = 1
        eguines = 1
        buffallo = 1
        camel = 1
        index = index + 1
        cur.execute('INSERT INTO livestock VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)', (country_id, cattle, sheep, goat, pig, eguines,
                                                                                   buffallo, camel))
        conn.commit()


conn.close()