import json
from flask import Flask, render_template, abort

app = Flask(__name__)             
app.config['DEBUG'] = True

@app.route('/')                  
def index():                 
    return render_template('index.html')

@app.route('/<color>/')  
def get_RGB_color(color):
    """gets the rgb code from the list of colors/file according to color in url"""
    with open("colors.txt") as file_:
        for line in file_:
            line_dict = json.loads(line)   
            for k, v in line_dict.items():
                if line_dict["name"] == color[0].upper() + color[1:].lower():
                    rgb = line_dict["rgb"]
                    return rgb
    return "Sorry. That color is not in list."


if __name__ == "__main__":
    app.run()
    