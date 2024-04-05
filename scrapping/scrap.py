import httpx
import csv


# location
urlH = 'https://app.powerbi.com/view?r=eyJrIjoiMjUyMWVjNzctNDc4Ny00MzQyLWI0NjktNDYxNzU5ZDE1MDM5IiwidCI6ImU4YjUzOTJiLWM1NmQtNGM4Ni1iNjU4LWJjYmFhNzM1ZDFjZCIsImMiOjR9'

head = httpx.options(urlH)

url = 'https://wabi-south-central-us-api.analysis.windows.net/public/reports/querydata'

# headear

#headers = {
#    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
#    'Accept': 'application/json, text/plain, */*',
#    'Accept-Language': 'en-US,en;q=0.7,es-AR;q=0.3',
#    # 'Accept-Encoding': 'gzip, deflate, br',
#    #'ActivityId': '59de48fe-ed88-4f74-8470-2030ce885677',
#    #'RequestId': '20c2c1e7-c1fe-3760-0457-a6ecf57486f3',
#    'X-PowerBI-ResourceKey': '285bdc89-ddc9-4831-ab93-e43d5bf3d1a9',
#    'Content-Type': 'application/json;charset=UTF-8',
#    'Origin': 'https://app.powerbi.com',
#    'DNT': '1',
#    'Connection': 'keep-alive',
#    'Referer': 'https://app.powerbi.com/',
#    'Sec-Fetch-Dest': 'empty',
#    'Sec-Fetch-Mode': 'cors',
#    'Sec-Fetch-Site': 'cross-site',
#    'Sec-GPC': '1',
#}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.7,es-AR;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://app.powerbi.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'X-PowerBI-ResourceKey': '2521ec77-4787-4342-b469-461759d15039',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://app.powerbi.com/',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

#print('head: ', head, '\nsalida: ', headers)

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
                                                                'Value': "'contVeh_MaipuOlmosN_EGRESO2'",
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
                                                                'Value': "'contVeh_MaipuOlmosN_EGRESO2'",
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
                'DatasetId': 'beefe97a-a0ed-4ea2-bc00-5b94ee700c95',
                'Sources': [
                    {
                        'ReportId': '90780177-2a38-419a-9c34-3bc250cb771d',
                    },
                ],
            },
        },
    ],
    'cancelQueries': [],
    'modelId': 2445526,
}

#def to_json(res):
#    with open("results.json", "w") as f:



# response
r = httpx.post(url, 
              #params=params,
              headers=headers,
              json=json_data,
              )



print(r.status_code)
print(r.headers['content-type'])

if r.status_code == httpx.codes.OK:
    print(r.json())
    #print(r.text)
