import customtkinter as ctk
from tkinter import ttk
import threading


from scanner import scan_network
from port_scanner import scan_ports
from database import create_tables, save_device, save_port




class NetScanGUI(ctk.CTk):


    def __init__(self):

        super().__init__()


        self.title("NetScan Pro - Network Scanner")

        self.geometry("1100x700")


        ctk.set_appearance_mode("dark")

        ctk.set_default_color_theme("blue")



        create_tables()



        self.create_header()

        self.create_network_section()

        self.create_device_table()

        self.create_port_section()

        self.create_port_table()

        self.create_status()





    # ---------------- HEADER ----------------


    def create_header(self):


        title = ctk.CTkLabel(

            self,

            text="🌐 NetScan Pro",

            font=("Arial",32,"bold")

        )


        title.pack(pady=15)







    # ---------------- NETWORK SCAN ----------------


    def create_network_section(self):


        frame = ctk.CTkFrame(self)

        frame.pack(

            fill="x",

            padx=20,

            pady=10

        )



        self.network_entry = ctk.CTkEntry(

            frame,

            width=300,

            placeholder_text="192.168.1.0/24"

        )


        self.network_entry.pack(

            side="left",

            padx=10,

            pady=10

        )




        self.scan_btn = ctk.CTkButton(

            frame,

            text="Scan Network",

            command=self.start_network_scan

        )


        self.scan_btn.pack(

            side="left",

            padx=10

        )







    def create_device_table(self):


        columns=(

            "IP",

            "Hostname",

            "Status"

        )


        self.device_table = ttk.Treeview(

            self,

            columns=columns,

            show="headings",

            height=8

        )



        for col in columns:


            self.device_table.heading(

                col,

                text=col

            )


            self.device_table.column(

                col,

                width=250

            )



        self.device_table.pack(

            padx=20,

            pady=10,

            fill="x"

        )









    def start_network_scan(self):


        network = self.network_entry.get()



        if not network:

            return



        threading.Thread(

            target=self.network_scan,

            args=(network,),

            daemon=True

        ).start()






    def network_scan(self,network):


        devices = scan_network(network)



        self.after(

            0,

            lambda:self.show_devices(devices)

        )







    def show_devices(self,devices):


        for row in self.device_table.get_children():

            self.device_table.delete(row)




        for device in devices:


            self.device_table.insert(

                "",

                "end",

                values=(

                    device["ip"],

                    device["hostname"],

                    device["status"]

                )

            )


            save_device(device)



        self.status.configure(

            text=f"{len(devices)} devices found"

        )









    # ---------------- PORT SCANNER ----------------


    def create_port_section(self):


        frame = ctk.CTkFrame(self)

        frame.pack(

            fill="x",

            padx=20,

            pady=10

        )




        self.ip_entry = ctk.CTkEntry(

            frame,

            width=300,

            placeholder_text="Target IP"

        )


        self.ip_entry.pack(

            side="left",

            padx=10,

            pady=10

        )





        self.port_btn = ctk.CTkButton(

            frame,

            text="Scan Ports",

            command=self.start_port_scan

        )


        self.port_btn.pack(

            side="left",

            padx=10

        )









    def create_port_table(self):


        columns=(

            "Port",

            "Service",

            "Status"

        )



        self.port_table = ttk.Treeview(

            self,

            columns=columns,

            show="headings",

            height=6

        )



        for col in columns:


            self.port_table.heading(

                col,

                text=col

            )


            self.port_table.column(

                col,

                width=250

            )



        self.port_table.pack(

            padx=20,

            pady=10,

            fill="x"

        )








    def start_port_scan(self):


        ip = self.ip_entry.get()



        if not ip:

            return



        threading.Thread(

            target=self.port_scan,

            args=(ip,),

            daemon=True

        ).start()







    def port_scan(self,ip):


        ports = scan_ports(ip)



        self.after(

            0,

            lambda:self.show_ports(ip,ports)

        )









    def show_ports(self,ip,ports):


        for row in self.port_table.get_children():

            self.port_table.delete(row)





        for port in ports:


            self.port_table.insert(

                "",

                "end",

                values=(

                    port["port"],

                    port["service"],

                    port["status"]

                )

            )


            save_port(

                ip,

                port

            )



        self.status.configure(

            text=f"{len(ports)} open ports found"

        )









    def create_status(self):


        self.status = ctk.CTkLabel(

            self,

            text="Ready"

        )


        self.status.pack(

            pady=10

        )