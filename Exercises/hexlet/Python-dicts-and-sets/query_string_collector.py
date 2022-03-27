def build_query_string(parameters):
    result = []
    for k, v in sorted(parameters.items()):
        result.append(f'{k}={v}')
    return '&'.join(result)


print(build_query_string({'per': 10, 'page': 1}))
