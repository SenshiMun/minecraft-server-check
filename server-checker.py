from mcstatus import JavaServer
import tkinter as tk
import socket

def status_check():
    try:
        server = JavaServer.lookup(ip.get())
        status = server.status()
        print("The server is ONLINE with {0} players and replied in {1} ms Latency".format(status.players.online, status.latency))
        label.config(text="Status: ONLINE | Players: "+str(status.players.online)+" | Latency: "+str(status.latency))
    except:
        try:
            socket.inet_aton(ip.get())
            label.config(text="The Server is OFFLINE")
        except:
            label.config(text="An Error Has Occured, Please Check the IP and try again.")

window = tk.Tk()

window.title('Server Status Check')
window.resizable(False, False)

ip = tk.Entry(width="50",)
label = tk.Label(text="Status: | Players:  | Latency:")
enter = tk.Button(text="Enter", command=status_check)


ip.pack()
enter.pack()
label.pack()





window.mainloop()




