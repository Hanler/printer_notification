from re import findall
from subprocess import check_output

def get_temp():
    """
    Get the temperature, execute the value and return it
    """
    temp = check_output(["vcgencmd", "measure_temp"]).decode()  # temperature query
    temp = float(findall('\d+\.\d+', temp)[0]) # execute the temp val from string by regex
    return temp
