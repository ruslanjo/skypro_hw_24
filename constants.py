from container import log_query

AVAILABLE_COMMANDS = {'filter': log_query.filter,
                      'map': log_query.map,
                      'unique': log_query.unique,
                      'sort': log_query.sort,
                      'limit': log_query.limit,
                      'regex': log_query.regex
                      }



COMMANDS_NUMBER = 2
