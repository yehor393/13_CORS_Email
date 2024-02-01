# import urllib
from fastapi import FastAPI
from api.todo_items import router as todo_router
from api.users import router as user_router
from models import todo
from dependencies.database import engine

#from fastapi_sso.sso.google import GoogleSSO

todo.BaseModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router, prefix="/todo")
app.include_router(user_router, prefix="/users")

GSSO_CLIENT_SECRET = "YOUR SECRET"
GSSO_CLIENT_ID = "YOUR CLIENT ID"

REDIRECT_URI = "http://localhost:8000/google/callback"


@app.get("/")
async def health_check():
    print()
    return {"OK": True}

#
# def get_google_sso() -> GoogleSSO:
#     return GoogleSSO(GSSO_CLIENT_ID, GSSO_CLIENT_SECRET, redirect_uri=REDIRECT_URI)
#
#
# @app.get("/auth/google")
# async def login_with_google():
#     google_auth_url = f"https://accounts.google.com/o/oauth2/auth?client_id={urllib.parse.quote(GSSO_CLIENT_ID)}&redirect_uri={urllib.parse.quote(REDIRECT_URI)}&scope=openid%20profile%20email&response_type=code"
#     return {"message": "Redirecting to Google for authentication...", "auth_url": google_auth_url}
#
#
# @app.get("/google/callback")
# async def complete_google_login(request: Request, google_sso: GoogleSSO = Depends(get_google_sso),
#                                 db: SessionLocal = Depends(get_db)):
#     google_user = await google_sso.verify_and_process(request)
#
#     user_service = UserServices(db)
#     user = user_service.get_by_username(google_user.email)
#     access_token = create_access_token(username=user.username, role=user.role)
#     return {"access_token": access_token, "token_type": "bearer"}
