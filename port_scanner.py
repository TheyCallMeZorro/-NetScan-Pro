import socket
import concurrent.futures




# Common ports

COMMON_PORTS = {

    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP Proxy"

}







def check_port(ip, port):


    try:


        sock = socket.socket(

            socket.AF_INET,

            socket.SOCK_STREAM

        )


        sock.settimeout(0.5)



        result = sock.connect_ex(

            (ip, port)

        )



        sock.close()



        if result == 0:


            return {

                "port": port,

                "service":
                COMMON_PORTS.get(
                    port,
                    "Unknown"
                ),

                "status":
                "Open"

            }




    except:

        pass



    return None







def scan_ports(ip):


    open_ports = []



    ports = list(

        COMMON_PORTS.keys()

    )





    with concurrent.futures.ThreadPoolExecutor(

        max_workers=50

    ) as executor:



        results = executor.map(

            lambda port:
            check_port(ip, port),

            ports

        )




        for result in results:


            if result:

                open_ports.append(result)




    return open_ports