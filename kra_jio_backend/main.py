# This is a sample Python script.
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run
from fastapi import FastAPI

from src.routes.all_routes import router
app = FastAPI(
    title='KRA Backend',
    # root_path="/kra-jewellers"
)
app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=5555, reload=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
