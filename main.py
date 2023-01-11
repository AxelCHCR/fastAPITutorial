from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from happytransformer import HappyTextClassification 
app = FastAPI()
@app.get("/")
def index():
    return {"message": "Working"}
@app.post("/AI")
def getScore(string: str = Body()):
    happy_tc = HappyTextClassification(model_type = "DISTILBERT", model_name = "distilbert-base-uncased-finetuned-sst-2-english", num_labels=2)
    result = happy_tc.classify_text(string)
    return {"Test Score: ": result}
