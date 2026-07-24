import sqlite3
from datetime import datetime




DATABASE = "netscan.db"






def connect_db():

    return sqlite3.connect(
        DATABASE
    )








def create_tables():


    conn = connect_db()

    cursor = conn.cursor()



    cursor.execute("""

    CREATE TABLE IF NOT EXISTS devices (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        ip TEXT,

        hostname TEXT,

        status TEXT,

        scan_time TEXT

    )

    """)



    cursor.execute("""

    CREATE TABLE IF NOT EXISTS ports (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        ip TEXT,

        port INTEGER,

        service TEXT,

        status TEXT,

        scan_time TEXT

    )

    """)



    conn.commit()

    conn.close()







def save_device(device):


    conn = connect_db()

    cursor = conn.cursor()



    cursor.execute(

        """

        INSERT INTO devices

        (ip, hostname, status, scan_time)

        VALUES (?, ?, ?, ?)

        """,

        (

            device["ip"],

            device["hostname"],

            device["status"],

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )

    )



    conn.commit()

    conn.close()







def save_port(ip, port_info):


    conn = connect_db()

    cursor = conn.cursor()



    cursor.execute(

        """

        INSERT INTO ports

        (ip, port, service, status, scan_time)

        VALUES (?, ?, ?, ?, ?)

        """,

        (

            ip,

            port_info["port"],

            port_info["service"],

            port_info["status"],

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )

    )



    conn.commit()

    conn.close()