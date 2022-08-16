from flask import Flask, request, jsonify
from flask_restx import Resource, Api, Namespace
from werkzeug.exceptions import BadRequest

from container import file_handler, log_query
from constants import COMMANDS_NUMBER, AVAILABLE_COMMANDS

app = Flask(__name__)
api = Api(app)

query_ns = Namespace('/perform_query')


@query_ns.route('/')
class Query(Resource):
    def post(self):
        req_data = request.json

        logs_file_name = req_data.get('file_name')

        try:
            logs_data = file_handler.read_file(logs_file_name)
        except FileNotFoundError:
            raise BadRequest('logs file not found')

        # Команда для обработки данных приходит в виде словаря с ключами cmd1, value1, cmd2, value2 и т.п
        # В цикле увеличиваем значение, чтобы динамически получить все команды для обработки
        for i in range(1, COMMANDS_NUMBER + 1):
            command = req_data.get('cmd' + str(i))
            command_value = req_data.get('value' + str(i))

            if command not in AVAILABLE_COMMANDS:
                raise BadRequest('server did not identify command')

            try:
                logs_data = log_query.use_query_method(logs_data, command, command_value, AVAILABLE_COMMANDS)
            except ValueError as e:
                raise BadRequest(str(e))

        return jsonify(logs_data)


if __name__ == '__main__':
    api.add_namespace(query_ns)
    app.run(debug=True, port=2024)
