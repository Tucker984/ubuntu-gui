import http.server
import socketserver
import tkinter
#config
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    window = tkinter.Tk()
window.title("Button GUI")
button_widget = tkinter.Button(window,text="Welcome to DataCamp's Tutorial on Tkinter")
button_widget.pack()
tkinter.mainloop()
