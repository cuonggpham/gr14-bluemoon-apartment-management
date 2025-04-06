from fastapi import FastAPI
from app.api.v1 import auth, household, resident, fee, payment, stats

app = FastAPI(title="BlueMoon Apartment Manager", version="1.0")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
# app.include_router(household.router, prefix="/api/v1/household", tags=["Household"])
# app.include_router(resident.router, prefix="/api/v1/resident", tags=["Resident"])
# app.include_router(fee.router, prefix="/api/v1/fee", tags=["Fee"])
# app.include_router(payment.router, prefix="/api/v1/payment", tags=["Payment"])
# app.include_router(stats.router, prefix="/api/v1/stats", tags=["Stats"])