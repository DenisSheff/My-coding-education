from user_interface import temperature_value_view
from user_interface import wind_value_view
from user_interface import pressure_value_view


def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '     <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_value_view(device))
    html += '     <p {}>Wind_speed: {} m/s</p>\n' \
        .format(style, wind_value_view(device))
    html += '     <p {}>Pressure: {} mmHg</p>\n' \
        .format(style, pressure_value_view(device))
    html += '    </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html


def new_create(data, device = 1):
    t, p, w = data
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '     <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '     <p {}>Wind_speed: {} m/s</p>\n' \
        .format(style, w)
    html += '     <p {}>Pressure: {} mmHg</p>\n' \
        .format(style, p)
    html += '    </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data
