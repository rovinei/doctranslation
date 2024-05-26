from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(response.data, dict):
            response.data['status'] = 'error'
        if response.status_code == 403:
            if 'detail' in response.data:
                response.data.pop('detail')
            response.data['auth'] = ['noPermission']

        elif response.status_code == 404:
            if 'detail' in response.data:
                response.data[str(response.data['detail'])] = ['notFound']
                response.data.pop('detail')

    return response
