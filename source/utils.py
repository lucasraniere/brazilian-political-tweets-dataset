from dateutil import parser

def convert_date(date_str):
    try:
        parsed_date = parser.parse(date_str)
        return parsed_date.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return 'Invalid date format'
