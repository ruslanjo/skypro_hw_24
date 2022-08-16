from typing import List
import os


class FileHandler:
    def __init__(self, data_directory):
        self.data_directory = data_directory

    def read_file(self, file_name: str):
        file_path = self._append_file_name_to_path(file_name)
        with open(file_path, 'r') as file:
            return file.readlines()

    def _append_file_name_to_path(self, file_name: str):
        return os.path.join(self.data_directory, file_name)


class LogQuery:
    def filter(self, logs_data: List[str], filter_condition: str) -> list:

        result = filter(lambda log: filter_condition in log, logs_data)
        return list(result)

    def map(self, logs_data: List[str], column_number: str) -> list:
        column_number = int(column_number)
        result = map(lambda log: log.split(' ')[column_number], logs_data)
        return list(result)

    def unique(self, logs_data: List[str]) -> list:
        unique_logs = set(logs_data)
        return list(unique_logs)

    def sort(self, logs_data: List[str], val) -> list:
        if val not in ['asc', 'desc']:
            raise ValueError('sort values must be either "asc" or "desc"')

        if val == 'desc':
            is_reversed = True
        else:
            is_reversed = False

        result = sorted(logs_data, reverse=is_reversed)

        return result

    def limit(self, logs_data: List[str], number_of_records: str):
        number_of_records = int(number_of_records)
        return logs_data[:number_of_records]

    def use_query_method(self, logs_data: List[str], command: str, value: str, available_commands: dict):
        # Получаем и применяем объект метода, который выполняет требуемую трансформацию данных
        query_method = available_commands.get(command)
        return query_method(logs_data, value)
