# For refrence https://www.kdnuggets.com/2021/06/5-tasks-automate-python.html

#Requirements

#pip install requests

#Command to run the file

#python scirpt_to_check_quick_weather_with_reports.py[put file name here] "Your City" [your city name here]


#python weather.py "Your City"

import sysimport requestsresp = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')
print(resp.text)
