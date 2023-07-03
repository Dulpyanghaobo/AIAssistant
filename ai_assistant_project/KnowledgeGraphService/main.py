from fastapi import FastAPI

app = FastAPI()

@app.get("/knowleage_graph/quickAccess")
def get_quick_access():
    return {"message": "This is the quick access feature."}

@app.get("/knowleage_graphknowleage_graph/tipsOrTutorials")
def get_tips_or_tutorials():
    return {"message": "This is the tips or tutorials feature."}

@app.get("/knowleage_graph/recommendations")
def get_recommendations():
    return {"message": "This is the recommendations feature."}

@app.get("/knowleage_graph/updates")
def get_updates():
    return {"message": "This is the updates feature."}
