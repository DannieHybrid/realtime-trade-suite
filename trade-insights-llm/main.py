from fastapi import FastAPI
from llm_insights.views import router as insights_router

app = FastAPI()

# Mount the insights router
app.include_router(insights_router, prefix="/insights")
