'''
from flask import Flask, request, make_response
'''

from flask import Flask,request,json
app = Flask(__name__)

@app.route("/")
def hello2():
    return "Hello2 again, Universal!"

@app.route('/testme')
def home():
    return 'success'

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@app.route('/simulate',methods=['POST'])
def recommend():
    df_result=get_recommendation(request)
    return(jsonify(df_result.to_json(orient='records')))
#     return recommendation(request)
if __name__=='__main__':
    app.run(debug=True)


