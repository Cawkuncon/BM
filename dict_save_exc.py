import datetime
import pandas


def savetoexcel(dict_price, buffer_name='buffer.xlsx', file_name='ParsPrices.xlsx'):
    """функция для сохранения результатов поиска в excel"""
    prices_to_excel = pandas.DataFrame(dict_price)  # считываем данные
    # (словарь, ключи словаря - название колонок, значения - списки с содержимым строк)
    prices_to_excel.to_excel(f'./{buffer_name}', index=False)  # сохраняем найденные данные
    data = pandas.read_excel(f'./{file_name}')  # загружаем данные, уже сохраненные в конечный файл
    data_pr = pandas.read_excel(f'./{buffer_name}')  # загружаем данные найденные в текущий запуск программы
    data_over = pandas.concat([data, data_pr])  # объединяем данные, ранее сохраненные и данные полученные
    # при текущем исполнении программы
    with pandas.ExcelWriter(f'{file_name}', engine='xlsxwriter') as writer:  # открываем файл для записи
        time = datetime.datetime.now().strftime(
            "%Y %m %d %H.%M.%S")  # в качестве имени листа будет дата запуска прогр.
        data_over.to_excel(writer, sheet_name=f'{time}', index=False,
                           freeze_panes=(1, 0))  # сохраняем все данные в конечный файл
        worksheet = writer.sheets[f'{time}']  # указываем лист для форматирования ячеек
        worksheet.set_column('A:A', 50)  # задает диапазону колонок их ширину
        worksheet.set_column('B:F', 10)
        worksheet.set_column('G:L', 7)
        worksheet.set_column('M:O', 10)
        worksheet.set_column('P:R', 30)