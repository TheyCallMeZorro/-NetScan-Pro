import socket
import subprocess
import concurrent.futures




def ping_device(ip):

    try:

        result = subprocess.run(

            ["ping", "-n", "1", "-w", "300", ip],

            stdout=subprocess.DEVNULL,

            stderr=subprocess.DEVNULL

        )


        if result.returncode == 0:

            try:

                hostname = socket.gethostbyaddr(ip)[0]

            except:

                hostname = "Unknown"



            return {

                "ip": ip,

                "hostname": hostname,

                "status": "Online"

            }



    except:

        pass



    return None






def scan_network(network):


    devices = []



    # Example:
    # 192.168.1.0/24

    base_ip = network.split("/")[0]


    parts = base_ip.split(".")


    prefix = ".".join(parts[:3])




    ips = [

        f"{prefix}.{i}"

        for i in range(1,255)

    ]





    with concurrent.futures.ThreadPoolExecutor(

        max_workers=50

    ) as executor:



        results = executor.map(

            ping_device,

            ips

        )




        for result in results:


            if result:

                devices.append(result)




    return devices