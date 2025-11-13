from fastapi import FastAPI
from api.endpoints import router

app = FastAPI()
app.include_router(router)

# from apscheduler.schedulers.background import BackgroundScheduler

# def retrain_all_models():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
#     
#     #... 

# scheduler = BackgroundScheduler()
# scheduler.add_job(retrain_all_models, 'interval', days=1)  # chaque jour
# scheduler.start()

