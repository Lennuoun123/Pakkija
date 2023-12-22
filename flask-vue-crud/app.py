from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import pandas as pd
import openpyxl
import itertools as it

df = pd.read_excel(io="3P_tunniplaan.xlsx", dtype='object')

komb = [
    '00000', '00001', '00010', '00011',
    '00100', '00101', '00110', '00111',
    '01000', '01001', '01010', '01011',
    '01100', '01101', '01110', '01111',
    '10000', '10001', '10010', '10011',
    '10100', '10101', '10110', '10111',
    '11000', '11001', '11010', '11011',
    '11100', '11101', '11110', '11111'
]

filtered_numbers = []

for binary_number in komb:
    if binary_number[0] == '1':
        filtered_numbers.append(binary_number)
#print(filtered_numbers)

esmaspaev = df[df['Cycle Day'].isin(filtered_numbers)]
#print(esmaspaev.head(50))

klassid = ["11R"]
esmaspaev_11R = esmaspaev[df['SectionID'].isin(klassid)]
print(esmaspaev_11R.head(50))

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify("hello")

if __name__ == '__main__':
    app.run()
