import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.7,es-AR;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'ActivityId': '59de48fe-ed88-4f74-8470-2030ce885677',
    'RequestId': '20c2c1e7-c1fe-3760-0457-a6ecf57486f3',
    'X-PowerBI-ResourceKey': '285bdc89-ddc9-4831-ab93-e43d5bf3d1a9',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://app.powerbi.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://app.powerbi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
}

params = {
    'synchronous': 'true',
}

json_data = {
    'version': '1.0.0',
    'queries': [
        {
            'Query': {
                'Commands': [
                    {
                        'SemanticQueryDataShapeCommand': {
                            'Query': {
                                'Version': 2,
                                'From': [
                                    {
                                        'Name': 'e',
                                        'Entity': 'EstadoTrafico',
                                        'Type': 0,
                                    },
                                    {
                                        'Name': 't',
                                        'Entity': 'Turnos',
                                        'Type': 0,
                                    },
                                    {
                                        'Name': 'p',
                                        'Entity': 'Periodos',
                                        'Type': 0,
                                    },
                                    {
                                        'Name': 'm',
                                        'Entity': 'Metricas',
                                        'Type': 0,
                                    },
                                    {
                                        'Name': 'c',
                                        'Entity': 'Camaras',
                                        'Type': 0,
                                    },
                                ],
                                'Select': [
                                    {
                                        'Column': {
                                            'Expression': {
                                                'SourceRef': {
                                                    'Source': 'e',
                                                },
                                            },
                                            'Property': 'fecha',
                                        },
                                        'Name': 'EstadoTrafico.fecha',
                                    },
                                    {
                                        'Column': {
                                            'Expression': {
                                                'SourceRef': {
                                                    'Source': 'e',
                                                },
                                            },
                                            'Property': 'cant',
                                        },
                                        'Name': 'Sum(EstadoTrafico.cant)',
                                    },
                                    {
                                        'Column': {
                                            'Expression': {
                                                'SourceRef': {
                                                    'Source': 't',
                                                },
                                            },
                                            'Property': 'nombre',
                                        },
                                        'Name': 'Turnos.nombre',
                                    },
                                    {
                                        'Column': {
                                            'Expression': {
                                                'SourceRef': {
                                                    'Source': 'e',
                                                },
                                            },
                                            'Property': 'activo',
                                        },
                                        'Name': 'EstadoTrafico.activo',
                                        'NativeReferenceName': 'activo',
                                    },
                                    {
                                        'Column': {
                                            'Expression': {
                                                'SourceRef': {
                                                    'Source': 'e',
                                                },
                                            },
                                            'Property': 'mark',
                                        },
                                        'Name': 'EstadoTrafico.mark',
                                        'NativeReferenceName': 'mark',
                                    },
                                    {
                                        'Column': {
                                            'Expression': {
                                                'SourceRef': {
                                                    'Source': 'e',
                                                },
                                            },
                                            'Property': 'diaSemana',
                                        },
                                        'Name': 'EstadoTrafico.diaSemana',
                                        'NativeReferenceName': 'diaSemana',
                                    },
                                    {
                                        'Column': {
                                            'Expression': {
                                                'SourceRef': {
                                                    'Source': 'e',
                                                },
                                            },
                                            'Property': 'periodo',
                                        },
                                        'Name': 'EstadoTrafico.periodo',
                                        'NativeReferenceName': 'periodo',
                                    },
                                    {
                                        'Column': {
                                            'Expression': {
                                                'SourceRef': {
                                                    'Source': 'e',
                                                },
                                            },
                                            'Property': 'intervaloSegmento',
                                        },
                                        'Name': 'EstadoTrafico.intervaloSegmento',
                                        'NativeReferenceName': 'intervaloSegmento',
                                    },
                                ],
                                'Where': [
                                    {
                                        'Condition': {
                                            'In': {
                                                'Expressions': [
                                                    {
                                                        'Column': {
                                                            'Expression': {
                                                                'SourceRef': {
                                                                    'Source': 't',
                                                                },
                                                            },
                                                            'Property': 'nombre',
                                                        },
                                                    },
                                                ],
                                                'Values': [
                                                    [
                                                        {
                                                            'Literal': {
                                                                'Value': "'MADRUGADA'",
                                                            },
                                                        },
                                                    ],
                                                ],
                                            },
                                        },
                                    },
                                    {
                                        'Condition': {
                                            'In': {
                                                'Expressions': [
                                                    {
                                                        'Column': {
                                                            'Expression': {
                                                                'SourceRef': {
                                                                    'Source': 'p',
                                                                },
                                                            },
                                                            'Property': 'periodo',
                                                        },
                                                    },
                                                ],
                                                'Values': [
                                                    [
                                                        {
                                                            'Literal': {
                                                                'Value': "'2024/03'",
                                                            },
                                                        },
                                                    ],
                                                ],
                                            },
                                        },
                                    },
                                    {
                                        'Condition': {
                                            'In': {
                                                'Expressions': [
                                                    {
                                                        'Column': {
                                                            'Expression': {
                                                                'SourceRef': {
                                                                    'Source': 'm',
                                                                },
                                                            },
                                                            'Property': 'nombreMetrica',
                                                        },
                                                    },
                                                ],
                                                'Values': [
                                                    [
                                                        {
                                                            'Literal': {
                                                                'Value': "'contVeh_ChacabucoIllia_NORTE'",
                                                            },
                                                        },
                                                    ],
                                                ],
                                            },
                                        },
                                    },
                                    {
                                        'Condition': {
                                            'In': {
                                                'Expressions': [
                                                    {
                                                        'Column': {
                                                            'Expression': {
                                                                'SourceRef': {
                                                                    'Source': 'c',
                                                                },
                                                            },
                                                            'Property': 'activo',
                                                        },
                                                    },
                                                ],
                                                'Values': [
                                                    [
                                                        {
                                                            'Literal': {
                                                                'Value': 'true',
                                                            },
                                                        },
                                                    ],
                                                ],
                                            },
                                        },
                                    },
                                    {
                                        'Condition': {
                                            'In': {
                                                'Expressions': [
                                                    {
                                                        'Column': {
                                                            'Expression': {
                                                                'SourceRef': {
                                                                    'Source': 'm',
                                                                },
                                                            },
                                                            'Property': 'activo',
                                                        },
                                                    },
                                                ],
                                                'Values': [
                                                    [
                                                        {
                                                            'Literal': {
                                                                'Value': 'true',
                                                            },
                                                        },
                                                    ],
                                                ],
                                            },
                                        },
                                    },
                                    {
                                        'Condition': {
                                            'In': {
                                                'Expressions': [
                                                    {
                                                        'Column': {
                                                            'Expression': {
                                                                'SourceRef': {
                                                                    'Source': 'c',
                                                                },
                                                            },
                                                            'Property': 'analyticsCapable',
                                                        },
                                                    },
                                                ],
                                                'Values': [
                                                    [
                                                        {
                                                            'Literal': {
                                                                'Value': 'true',
                                                            },
                                                        },
                                                    ],
                                                ],
                                            },
                                        },
                                    },
                                    {
                                        'Condition': {
                                            'Between': {
                                                'Expression': {
                                                    'Column': {
                                                        'Expression': {
                                                            'SourceRef': {
                                                                'Source': 'e',
                                                            },
                                                        },
                                                        'Property': 'fechaDesde',
                                                    },
                                                },
                                                'LowerBound': {
                                                    'DateSpan': {
                                                        'Expression': {
                                                            'DateAdd': {
                                                                'Expression': {
                                                                    'DateAdd': {
                                                                        'Expression': {
                                                                            'DateAdd': {
                                                                                'Expression': {
                                                                                    'Now': {},
                                                                                },
                                                                                'Amount': -1,
                                                                                'TimeUnit': 0,
                                                                            },
                                                                        },
                                                                        'Amount': 1,
                                                                        'TimeUnit': 0,
                                                                    },
                                                                },
                                                                'Amount': -50,
                                                                'TimeUnit': 3,
                                                            },
                                                        },
                                                        'TimeUnit': 0,
                                                    },
                                                },
                                                'UpperBound': {
                                                    'DateSpan': {
                                                        'Expression': {
                                                            'DateAdd': {
                                                                'Expression': {
                                                                    'Now': {},
                                                                },
                                                                'Amount': -1,
                                                                'TimeUnit': 0,
                                                            },
                                                        },
                                                        'TimeUnit': 0,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    {
                                        'Condition': {
                                            'In': {
                                                'Expressions': [
                                                    {
                                                        'Column': {
                                                            'Expression': {
                                                                'SourceRef': {
                                                                    'Source': 'm',
                                                                },
                                                            },
                                                            'Property': 'nombreMetrica',
                                                        },
                                                    },
                                                ],
                                                'Values': [
                                                    [
                                                        {
                                                            'Literal': {
                                                                'Value': "'contVeh_ChacabucoIllia_NORTE'",
                                                            },
                                                        },
                                                    ],
                                                ],
                                            },
                                        },
                                    },
                                ],
                                'OrderBy': [
                                    {
                                        'Direction': 1,
                                        'Expression': {
                                            'Column': {
                                                'Expression': {
                                                    'SourceRef': {
                                                        'Source': 'e',
                                                    },
                                                },
                                                'Property': 'intervaloSegmento',
                                            },
                                        },
                                    },
                                ],
                                'GroupBy': [
                                    {
                                        'SourceRef': {
                                            'Source': 'e',
                                        },
                                        'Name': 'EstadoTrafico',
                                    },
                                ],
                            },
                            'Binding': {
                                'Primary': {
                                    'Groupings': [
                                        {
                                            'Projections': [
                                                0,
                                                1,
                                                2,
                                                3,
                                                4,
                                                5,
                                                6,
                                                7,
                                            ],
                                            'GroupBy': [
                                                0,
                                            ],
                                        },
                                    ],
                                },
                                'DataReduction': {
                                    'Primary': {
                                        'Top': {
                                            'Count': 1000,
                                        },
                                    },
                                },
                                'Version': 1,
                            },
                            'ExecutionMetricsKind': 1,
                        },
                    },
                ],
            },
            'QueryId': '',
            'ApplicationContext': {
                'DatasetId': '1439b6ab-51b8-43f4-ba8d-9706f373e65c',
                'Sources': [
                    {
                        'ReportId': 'cf615ef0-e612-49b7-84eb-fbd80b7073f8',
                        'VisualId': '26282cb27cb1cdc65c30',
                    },
                ],
            },
        },
    ],
    'cancelQueries': [],
    'modelId': 2445474,
}

response = requests.post(
    'https://wabi-south-central-us-api.analysis.windows.net/public/reports/querydata',
    params=params,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"e","Entity":"EstadoTrafico","Type":0},{"Name":"t","Entity":"Turnos","Type":0},{"Name":"p","Entity":"Periodos","Type":0},{"Name":"m","Entity":"Metricas","Type":0},{"Name":"c","Entity":"Camaras","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"e"}},"Property":"fecha"},"Name":"EstadoTrafico.fecha"},{"Column":{"Expression":{"SourceRef":{"Source":"e"}},"Property":"cant"},"Name":"Sum(EstadoTrafico.cant)"},{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"nombre"},"Name":"Turnos.nombre"},{"Column":{"Expression":{"SourceRef":{"Source":"e"}},"Property":"activo"},"Name":"EstadoTrafico.activo","NativeReferenceName":"activo"},{"Column":{"Expression":{"SourceRef":{"Source":"e"}},"Property":"mark"},"Name":"EstadoTrafico.mark","NativeReferenceName":"mark"},{"Column":{"Expression":{"SourceRef":{"Source":"e"}},"Property":"diaSemana"},"Name":"EstadoTrafico.diaSemana","NativeReferenceName":"diaSemana"},{"Column":{"Expression":{"SourceRef":{"Source":"e"}},"Property":"periodo"},"Name":"EstadoTrafico.periodo","NativeReferenceName":"periodo"},{"Column":{"Expression":{"SourceRef":{"Source":"e"}},"Property":"intervaloSegmento"},"Name":"EstadoTrafico.intervaloSegmento","NativeReferenceName":"intervaloSegmento"}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"nombre"}}],"Values":[[{"Literal":{"Value":"\'MADRUGADA\'"}}]]}}},{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"p"}},"Property":"periodo"}}],"Values":[[{"Literal":{"Value":"\'2024/03\'"}}]]}}},{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"m"}},"Property":"nombreMetrica"}}],"Values":[[{"Literal":{"Value":"\'contVeh_ChacabucoIllia_NORTE\'"}}]]}}},{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"activo"}}],"Values":[[{"Literal":{"Value":"true"}}]]}}},{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"m"}},"Property":"activo"}}],"Values":[[{"Literal":{"Value":"true"}}]]}}},{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"analyticsCapable"}}],"Values":[[{"Literal":{"Value":"true"}}]]}}},{"Condition":{"Between":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"e"}},"Property":"fechaDesde"}},"LowerBound":{"DateSpan":{"Expression":{"DateAdd":{"Expression":{"DateAdd":{"Expression":{"DateAdd":{"Expression":{"Now":{}},"Amount":-1,"TimeUnit":0}},"Amount":1,"TimeUnit":0}},"Amount":-50,"TimeUnit":3}},"TimeUnit":0}},"UpperBound":{"DateSpan":{"Expression":{"DateAdd":{"Expression":{"Now":{}},"Amount":-1,"TimeUnit":0}},"TimeUnit":0}}}}},{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"m"}},"Property":"nombreMetrica"}}],"Values":[[{"Literal":{"Value":"\'contVeh_ChacabucoIllia_NORTE\'"}}]]}}}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"e"}},"Property":"intervaloSegmento"}}}],"GroupBy":[{"SourceRef":{"Source":"e"},"Name":"EstadoTrafico"}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1,2,3,4,5,6,7],"GroupBy":[0]}]},"DataReduction":{"Primary":{"Top":{"Count":1000}}},"Version":1},"ExecutionMetricsKind":1}}]},"QueryId":"","ApplicationContext":{"DatasetId":"1439b6ab-51b8-43f4-ba8d-9706f373e65c","Sources":[{"ReportId":"cf615ef0-e612-49b7-84eb-fbd80b7073f8","VisualId":"26282cb27cb1cdc65c30"}]}}],"cancelQueries":[],"modelId":2445474}'
#response = requests.post(
#    'https://wabi-south-central-us-api.analysis.windows.net/public/reports/querydata',
#    params=params,
#    headers=headers,
#    data=data,
#)
