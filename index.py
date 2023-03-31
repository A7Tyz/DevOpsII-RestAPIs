from flask import Flask, request, jsonify

app = Flask(__name__)

Items = [
    {"name": "Keybord", "category:" : "1" , "price:" : "20.5" , "instock:" : "200"},
    
]
def _find_next_id(name):
    data = [x for x in Items if  x['name']==name]
    return data

@app.route('/Items', methods=["GET"])
def get_items():
    return jsonify(Items)

@app.route('/Items/<name>', methods=["GET"])
def get_items_id(name):
    data = _find_next_id(name)
    return jsonify(data)


@app.route('/Items' , methods=["POST"])
def post_items():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')
    

    new_data = {
        "name" : name,
        "category" : category,
        "price" : price,
        "instock" : instock
    }

    if (_find_next_id(name)) :
        return {"error" : "Bad Request"}, name
    else : 
        Items.append(new_data)
        return jsonify(Items)

@app.route('/Items/<name>', methods = ['DELETE'])
def delete_items(name):

    data = _find_next_id(name)
    if not data:
        return {"error": "Items not found"}, 404
    else:
        Items.remove(data[0]) 
        return "Items deleted succuessfully" ,200

@app.route('/Items/<name>', methods=["PUT"])
def update_items(name):
    global Items
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    for Items in Items:
        if name == Items["name"]:
            Items["category"] = int(category)
            Items["price"] = int(price)
            Items["instock"] = int(instock)
            return jsonify(Items)

    else:
        return "Error", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)