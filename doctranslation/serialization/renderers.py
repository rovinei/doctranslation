from djangorestframework_camel_case.render import CamelCaseJSONRenderer


class StatusRenderer(CamelCaseJSONRenderer):
    media_type = 'application/json'
    format = '.json'

    def render(self, data, media_type=None, renderer_context=None):
        status = 'ok'
        formatted_data = {}

        content = data
        if isinstance(data, dict):
            status = data.get('status', 'ok')
            if status == 'error' or status == 'ok':
                content = {d: data[d] for d in data if d != 'status'}

        if status == 'error':
            formatted_data['status'] = 'error'
            formatted_data['errors'] = content
        else:
            formatted_data['status'] = 'ok'
            formatted_data['result'] = content

        return super().render(formatted_data, media_type, renderer_context)
