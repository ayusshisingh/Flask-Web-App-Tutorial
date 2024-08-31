import sys
print(sys.path)  # Add this line to see where Python is looking for modules

from website import create_app

app = create_app()
if __name__ == '__main__': 
	app.run(debug=True)
