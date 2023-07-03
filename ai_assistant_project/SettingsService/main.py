from fastapi import FastAPI

app = FastAPI()

@app.get("/quickAccess")
def get_quick_access():
    return {"message": "This is the quick access feature."}

@app.get("/tipsOrTutorials")
def get_tips_or_tutorials():
    return {"message": "This is the tips or tutorials feature."}

@app.get("/recommendations")
def get_recommendations():
    return {"message": "This is the recommendations feature."}

@app.get("/updates")
def get_updates():
    return {"message": "This is the updates feature."}
