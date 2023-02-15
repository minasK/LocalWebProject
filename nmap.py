import nmap
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_min = 0
port_max = 65535
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")