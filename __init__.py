import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    n1 = int(req.params.get('n1'))
    n2 = int(req.params.get('n2'))
    n3 = int(req.params.get('n3'))
    if not n1 and not n2 and not n3:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            n1 = int(req_body.get('n1'))
            n2 = int(req_body.get('n2'))
            n3 = int(req_body.get('n3'))


    if n1 and n2 and n3:
        res = n1 + n2 + n3
        return func.HttpResponse(f"Result = {res}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass three numbers to get a result.",
             status_code=200
        )
