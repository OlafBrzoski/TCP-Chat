# Multithreaded TCP Chat Application

  A real-time chat application demonstrating Client-Server architecture. The project utilizes Python's low-level socket library for network communication and threading to handle multiple concurrent client connections without blocking the server.

## 🛠️ Technologies Used
 * Language: Python 3.x
 
 * Networking: socket (TCP/IP protocol)
 
 * Concurrency: threading

## ⚙️ Configuration & Setup
 Important: The default code is configured for a specific LAN IP (192.168.100.2). To run this locally on your machine, you must update the IP address settings.
 
 Clone the repository:
 
 Bash
 
 git clone https://github.com/OlafBrzoski/TCP-Chat.git
 cd TCP-Chat
 Update IP Address: Open Server.py and Client.py in your code editor. Change the IP address to '127.0.0.1' (localhost) for local testing.
 
 In Server.py:
 
 Python
 
 Change host = '192.168.100.2' to:
 host = '127.0.0.1' 
 In Client.py:
 
 Python
 
  Change client.connect(('192.168.100.2', 9999)) to:
 client.connect(('127.0.0.1', 9999))

## 💻 How to Run
 * Start the Server: Open a terminal window and run:
 
 Bash
 
 python Server.py
 Output: Server is listening...
 
 * Start the Client(s): Open a new terminal window (you can open multiple terminals to simulate multiple users) and run:
 
 Bash
 
 python Client.py
 
 * Usage:
 
   * Enter a nickname when prompted.
 
   * Type messages to broadcast them to all connected users.
 
   *  Enter your nickname when prompted.
 
   *  Start typing messages!
