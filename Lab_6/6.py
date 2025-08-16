from flask import Flask
ungdung = Flask(__name__)
@ungdung.route('/')

@ungdung.route('/monhoc')
def learn():
    chuoi = "Day la trang mon hoc Python"
    return chuoi

@ungdung.route('/monhoc/<tenmon>')
def subjects(tenmon):
    chuoi = "Day la trang mon hoc Python"
    monhoc = str(tenmon).upper()
    if monhoc == "":
        chuoi += "!"
    else:
        chuoi += " " + monhoc
    return chuoi    

if __name__ == "__main__":
    ungdung.run(port=5050)
