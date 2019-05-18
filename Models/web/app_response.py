from flask import Flask,jsonify,request
from werkzeug.wrappers import Response
app=Flask(__name__)

class JSONResponse(Response):
    @classmethod
    def force_type(cls,rv,environ=None):
        if isinstance(rv,dict):
            rv=jsonify(rv)
        return super(JSONResponse,cls).force_type(rv,environ)
app.response_class=JSONResponse

@app.route("/")
def hello_world():
    return "message:hello world"

@app.route("/custom_headers")
def headers():
    print(request.headers.get("User-Agent"))
    return {'header':[1,2,3]},201,[("X-Request-Id",'100')]

if __name__=="__main__":
    app.run(host="0.0.0.0",port=9000,debug=True)
