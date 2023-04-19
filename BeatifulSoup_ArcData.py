import requests
from bs4 import BeautifulSoup

def get_content_from_url(url):
    try:
        print("Getting Content...")
        response = requests.get(url)
        # Comprobar que la respuesta es correcta
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
        return None
    except Exception as err:
        print(f'Error: {err}')
        return None
    else:
        return response.content

def get_tables_from_content(content):
    try:
        soup = BeautifulSoup(content, 'html.parser')
        tables = {}
        table1 = soup.select_one('a[name="AWE1WP01"] ~ table')
        table2 = soup.select_one('a[name="AWE1WP02"] ~ table')
        
        tables["Weld_Schedule_Data_AWE1WP01"] = table1
        tables["Weld_Schedule_Data_AWE1WP02"] = table2

        return tables
    except Exception as err:
        print('Error:', err)
        return None

def convert_table_to_object(table):
    try:
        headers = [header.text.strip() for header in table.find_all('tr')[0].find_all('b')]

        data = []
        for row in table.find_all('tr')[1:]:
            values = [value.text.strip() for value in row.find_all('td')]
            data.append(dict(zip(headers, values)))
        
        return data

    except Exception as e:
        print('Error:', e)
        return None

def main():
    print("Starting...")
    URL = 'http://192.168.115.50/FRS/awdata.stm'
    content = get_content_from_url(URL)
    
    if content is None:
        print('Error getting content')
    else:
        content_tables = get_tables_from_content(content)
        if not content_tables:
            print("No tables found")
        
        data_objects = {}
        for key, value in content_tables.items():
            dataObj = convert_table_to_object(value)
            if dataObj:
                data_objects[key] = dataObj

        print(data_objects)


if (__name__ == "__main__"):
    main()
