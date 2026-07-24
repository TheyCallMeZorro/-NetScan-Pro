import socket
import re




def validate_network(network):


    pattern = r"^\d{1,3}(\.\d{1,3}){3}/24$"



    if re.match(pattern, network):


        return True



    return False







def get_local_ip():


    try:


        hostname = socket.gethostname()


        ip = socket.gethostbyname(
            hostname
        )


        return ip



    except:


        return "Unknown"









def format_size(size):


    units = [

        "B",
        "KB",
        "MB",
        "GB"

    ]



    index = 0



    while size > 1024 and index < len(units)-1:


        size /= 1024


        index += 1





    return f"{size:.2f} {units[index]}"








def get_hostname(ip):


    try:


        return socket.gethostbyaddr(ip)[0]



    except:


        return "Unknown"