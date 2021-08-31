
def web_page():
  #if led.value() == 1:
  #  gpio_state="OFF"
  #else:
  #gpio_state="ON"
  
  html = """<html>
	<head> 
		<title>
			ESP Web Server
		</title> 
	
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="icon" href="data:,">
		<style>
			html{
				font-family: Helvetica; 
				display:inline-block; 
				margin: 0px auto; 
				text-align: center;
				}
			h1{
				color: #0F3376; 
				padding: 2vh;
				}
			p{
			font-size: 1.5rem;
			}
			.button{
				display: inline-block; 
				background-color: #e7bd3b; 
				border: none; 
				border-radius: 4px; 
				color: white;
				padding: 16px 40px; 
				text-decoration: none; 
				font-size: 30px; 
				margin: 2px; 
				cursor: pointer;
				}
			.button2{
				background-color: #4286f4;
				}
		</style>
	</head>
	
	<body> 
		<h1>ESP Web Server</h1> 
		
		<p>
			<a href="/?movement=toward"><button class="button">TOWARD</button></a>
		</p>
		<p>
			<a href="/?movement=stop"><button class="button button2">STOP</button></a>
		</p>
		<p>
			<a href="/?movement=backward"><button class="button">BACKWARD</button></a>
		</p>
	</body>
</html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  
  mov_to = request.find('/?movement=toward')
  mov_stop = request.find('/?movement=stop')
  mov_back = request.find('/?movement=backward')
  
  if mov_to == 6:
    print('MOVEMENT TOWARD')
    Mot_R_direction.value(1)
    Mot_L_direction.value(1)
    Mot_R_speed.duty(800)
    Mot_L_speed.duty(800)    
  if mov_stop == 6:
    print('MOVEMENT STOP')
    Mot_R_speed.duty(0)
    Mot_L_speed.duty(0)
  if mov_back == 6:
    
    print('MOVEMENT BACKWARD')
    Mot_R_direction.value(0)
    Mot_L_direction.value(0)
    Mot_R_speed.duty(800)
    Mot_L_speed.duty(800) 
    
  response = web_page()
  #conn.sendall(response)
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

