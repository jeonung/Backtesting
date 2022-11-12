import pandas as pd

def read_data(name):
    """2016 ~ 2021년 데이터를 세로로 붙이는 함수"""
    kospi_2016 = pd.read_table(f"./data/{name}_kospi_2016.txt", sep="\t", names=['Stock', 'date', name])
    kosdaq_2016 = pd.read_table(f"./data/{name}_kosdaq_2016.txt", sep="\t", names=['Stock', 'date', name])
    data = pd.concat([kospi_2016, kosdaq_2016])

    for year in range(2017, 2022):
        for market in ['kospi', 'kosdaq']:
            file_name = [name, '_', market, '_', str(year), '.txt']
            file_name = "".join(file_name)
            tmp = pd.read_table("./data/" + file_name, sep="\t", names=['Stock', 'date', name])
            data = pd.concat([data, tmp])
    
    return data