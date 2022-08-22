from typing import Callable, Optional
import os
import re


class FileHandler:
    def __init__(self, data_directory: str) -> None:
        self.data_directory = data_directory

    def read_file(self, file_name: str) -> list[str]:
        file_path: str = self._append_file_name_to_path(file_name)
        with open(file_path, 'r') as file:
            return file.readlines()

    def _append_file_name_to_path(self, file_name: str) -> str:
        return os.path.join(self.data_directory, file_name)


class LogQuery:
    def filter(self, logs_data: list[str], filter_condition: str) -> list[str]:

        result = filter(lambda log: filter_condition in log, logs_data)
        return list(result)

    def map(self, logs_data: list[str], column_number: str) -> list[str]:
        column_number_int = int(column_number)
        result = map(lambda log: log.split(' ')[column_number_int], logs_data)
        return list(result)

    def unique(self, logs_data: list[str]) -> list[str]:
        unique_logs: set = set(logs_data)
        return list(unique_logs)

    def sort(self, logs_data: list[str], val: str) -> list[str]:
        if val not in ['asc', 'desc']:
            raise ValueError('sort values must be either "asc" or "desc"')

        if val == 'desc':
            is_reversed = True
        else:
            is_reversed = False

        result: list = sorted(logs_data, reverse=is_reversed)

        return result

    def limit(self, logs_data: list[str], number_of_records: str):
        number_of_records_int = int(number_of_records)
        return logs_data[:number_of_records_int]

    def regex(self, logs_data: list[str], regex: str) -> list[str]:
        res = []

        for log in logs_data:
            res.extend(re.findall(regex, log))

        return res

    def use_query_method(self, logs_data: list[str], command: str, value: str, available_commands: dict):
        # Получаем и применяем объект метода, который выполняет требуемую трансформацию данных
        query_method: Optional[Callable] = available_commands.get(command)

        if query_method:
            return query_method(logs_data, value)
