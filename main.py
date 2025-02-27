from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
def read_root():
    version="0.3"
    namespace = os.getenv('POD_NAMESPACE', default = 'ns-red')
    return {"Message": "with LOVE from OCI Devops team ","Version":version,"Namespace":namespace}
