import db_conn

def comparison(response, weather):
    resp_list = []
    if response[1] == 'year' or response[2] == 'month' or response[3] == 'day':
        if response[4] == 'year' or response[5] == 'month' or response[6] == 'day':
            return weather
        for i in weather:
            str_date = i[-1].split('-')
            if int(response[4]) < int(str_date[0]):
                resp_list.append(i)
            elif int(response[4]) == int(str_date[0]) and int(response[5]) < int(str_date[1]) :
                resp_list.append(i)
            elif int(response[4]) == int(str_date[0]) and int(response[5]) == int(str_date[1]) and int(response[6]) < int(str_date[2]):
                resp_list.append(i)
        return resp_list

    elif response[4] == 'year' or response[5] == 'month' or response[6] == 'day':
        for i in weather:
            str_date = i[-1].split('-')
            if int(response[1]) > int(str_date[0]):
                resp_list.append(i)
            elif int(response[1]) == int(str_date[0]) and int(response[2]) > int(str_date[1]) :
                resp_list.append(i)
            elif int(response[1]) == int(str_date[0]) and int(response[2]) == int(str_date[1]) and int(response[3]) > int(str_date[2]):
                resp_list.append(i)
        return resp_list

    for i in weather:
        str_date = i[-1].split('-')
        if int(response[1]) > int(str_date[0]) and int(response[4]) < int(str_date[0]):
            resp_list.append(i)
        elif int(response[1]) == int(str_date[0]) and int(response[2]) > int(str_date[1]) and int(response[4]) == int(str_date[0]) and int(response[5]) < int(str_date[1]) :
            resp_list.append(i)
        elif int(response[1]) == int(str_date[0]) and int(response[2]) == int(str_date[1]) and int(response[3]) > int(str_date[2]) and\
            int(response[4]) == int(str_date[0]) and int(response[5]) == int(str_date[1]) and int(response[6]) < int(str_date[2]):
            resp_list.append(i)
    return resp_list

def filter_by(response):
    if response[0] == "All":
        weather = db_conn.select_all()
        return comparison(response, weather)

    weather = db_conn.filter(response)
    return comparison(response, weather)
