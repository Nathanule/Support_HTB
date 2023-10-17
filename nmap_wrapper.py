#!/usr/bin/python3

import nmap
import matplotlib.pyplot as plt
from tabulate import tabulate

class Scanner():
    def __init__(self, target_ip, flags):
        self.target_ip = target_ip
        self.flags = flags
        self.nmap = nmap.PortScanner()
        
    def scan(self):
        self.nmap.scan(hosts=self.target_ip, arguments=self.flags)

    def format_scan_results(self):
        table_data = []
        for host in self.nmap.all_hosts():
            for proto in self.nmap[host].all_protocols():
                ports = self.nmap[host][proto].keys()
                for port in ports:
                    service = self.nmap[host][proto][port]['name']
                    state = self.nmap[host][proto][port]['state']
                    version = self.nmap[host][proto][port].get('product', 'N/A')
                    table_data.append([host, port, proto, service, version, state])
        
        tables_headers = ['Host', 'Port', 'Protocol', 'Service', 'Version', 'State']
        table = tabulate(table_data, headers=tables_headers, tablefmt='grid')
        print(table)
        return table
    
    def save_file(self, filename):
        table = self.format_scan_results()
        with open(filename, 'w') as file:
            file.write(table)
    
    def gen_image(self, filename):
        table = self.format_scan_results()
        #split the table into lines and format it
        table_lines = table.split('\n')
        table_text = '\n'.join(table_lines[2:-1]) # exclluse headers and empty lines

        # create a figure and axis
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))
        ax.axis('off')
        ax.text(0, 0.5, table_text, va='center', fontsize=12)

        #Save the figure as an image
        plt.savefig(filename, bbox_inches='tight')
        plt.close()


if __name__ == "__main__":
    target_ip = str(input("Please enter a IP address: "))
    flags = str(input("Please enter nmap flags: "))
    port_scanner = Scanner(target_ip, flags)
    port_scanner.scan()
    result_table = port_scanner.format_scan_results()
    print(result_table)

    # saving the table to a txt file
    result_filname = 'nmap_results'
    port_scanner.save_file(result_filname)
    print(f"Saving results to {result_filname}")

    # Generate and save the table as an image
    image_filename = 'nmap_results.png'
    port_scanner.gen_image(image_filename)
    print(f"results saved to image {image_filename}")
