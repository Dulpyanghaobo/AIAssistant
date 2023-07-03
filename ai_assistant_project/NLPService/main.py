from fastapi import FastAPI

app = FastAPI()

@app.get("/nlp/quickAccess")
def get_quick_access():
    return {"message": "This is the quick access feature."}

@app.get("/nlp/tipsOrTutorials")
def get_tips_or_tutorials():
    return {"message": "This is the tips or tutorials feature."}

@app.get("/nlp/recommendations")
def get_recommendations():
    return {"message": "This is the recommendations feature."}

@app.get("/nlp/updates")
def get_updates():
    return {"message": "This is the updates feature."}
