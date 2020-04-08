import logging

import azure.functions as func
import psycopg2

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    if name:
        try:
            conn = psycopg2.connect(
                database = "penTest",
                user = "postgres", 
                password = "postgres",
                host = "host.docker.internal",
                port = "5432")
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE name = '%s' " % name)
                result = cursor.fetchall()
            conn.commit()
            conn.close()
            if result:
                return func.HttpResponse(f"{result}", mimetype='application/json')
            else:
                return func.HttpResponse("no data",mimetype='application/json')
        except Exception as e:
            print(f"error: {e}")
            return func.HttpResponse(f"{e}", status_code=500,mimetype='application/json')

       
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200,mimetype='application/json'
        )
