import numpy as np
import pandas as pd
import httpx
import csv
import json
import datetime
import os


# Functions

# automatic indent code: gg=G (src: https://youtu.be/r76uQkMNhSA)

# .exists work for dir y files
#if(not os.path.isdir('lala')):
#    os.mkdir('lala')
def direct(directorio):
    """
    Creation of directories where we store json data
    """
    path = 'dat/json/' + directorio
    try:
        os.makedirs(path)
    except: 
        pass


def jsondata(it, fecha, ubicacion):
    """
    Json query
    in:
        it: turn indicator
        fecha: date
        ubicacion: location
    out:
        json_data
    """
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
    				'Value': f"{it}",
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
    				'Value': f"{fecha}",
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
    				'Value': f"{ubicacion}",
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
    				'Value': f"{ubicacion}",
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
    return json_data


def to_json(res, name):
    """
    Generate and write data
    in:
        res: json data
        name: json file name
    """
    with open(name+".json", "w") as f:
        f.write(res)





# ==========================

# data location
# -------------
urlH = 'https://app.powerbi.com/view?r=eyJrIjoiMjUyMWVjNzctNDc4Ny00MzQyLWI0NjktNDYxNzU5ZDE1MDM5IiwidCI6ImU4YjUzOTJiLWM1NmQtNGM4Ni1iNjU4LWJjYmFhNzM1ZDFjZCIsImMiOjR9'

head = httpx.options(urlH)

url = 'https://wabi-south-central-us-api.analysis.windows.net/public/reports/querydata'

# headear
# -------

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



# Variables
# ---------

# We use it for iteration

year = datetime.date.today().year
#anios = ['2019', '2020', '2021', '2022', '2023', '2024']
anios = np.arange(2019, year+1).tolist()
#anios = str(anios)
meses = np.arange(1,13).tolist() 

# dict 
its = {0: "'MADRUGADA'", 
       1: "'MAÑANA'", 
       2: "'SIESTA'", 
       3: "'TARDE'", 
       4: "'NOCHE'"
       }


# directories store json files
# active cameras
location_dir = [
        'contVeh_MaipuOlmosN_EGRESO2',
        'contVeh_ChacabucoIllia_NORTE',
        'contVeh_MaipuOlmosE_EGRESO',
        'contVeh_GuzmanSarmiento_NW',
        'contVeh_PuenteSarmiento_INGRESO',
        'contVeh_GuzmanSarmiento_SE',
               ]

# no active cameras
location_dirNA = [
	'contVeh_CPCMonseñorS_Ingreso',
	'contVeh_CPCMonseñorN_Egreso',
	'contVeh_OctavioPintoSagradaFamilia_INGRESO',
	'contVeh_CaraffaOctavioPinto_INGRESO',
	'contVeh_CPCColonW_INGRESO',
	'contVeh_CPCColonE_EGRESO',
	'contVeh_Nuevocentro_EGRESO',
	'contVeh_SabattiniPucara_EGRESO',
	'contVeh_SabattiniPucara_INGRESO',
	'contVeh_SabattiniSgtoCabral_INGRESO',
	'contVeh_SabattiniSgtoCabral_EGRESO',
	'contVeh_CPCVillaLibertador_EGRESO',
	'contVeh_CPCVillaLibertador_INGRESO',
	'contVeh_CPCRuta20W_INGRESO',
	'contVeh_CPCRuta20W_EGRESO',
	'contVeh_CPCRuta20W_GiroIzqIngresoBarrioN',
	'contVeh_CPCRuta20E_INGRESO',
	'contVeh_CPCRuta20E_EGRESO',
]


# Camera locations
# active cameras
ubicaciones = ["'contVeh_MaipuOlmosN_EGRESO2'",
               "'contVeh_ChacabucoIllia_NORTE'",
               "'contVeh_MaipuOlmosE_EGRESO'",
               "'contVeh_GuzmanSarmiento_NW'",
               "'contVeh_PuenteSarmiento_INGRESO'",
               "'contVeh_GuzmanSarmiento_SE'",
               ]

# no active camera
ubicacionesNA = [
	"'contVeh_CPCMonseñorS_Ingreso'",
	"'contVeh_CPCMonseñorN_Egreso'",
	"'contVeh_OctavioPintoSagradaFamilia_INGRESO'",
	"'contVeh_CaraffaOctavioPinto_INGRESO'",
	"'contVeh_CPCColonW_INGRESO'",
	"'contVeh_CPCColonE_EGRESO'",
	"'contVeh_Nuevocentro_EGRESO'",
	"'contVeh_SabattiniPucara_EGRESO'",
	"'contVeh_SabattiniPucara_INGRESO'",
	"'contVeh_SabattiniSgtoCabral_INGRESO'",
	"'contVeh_SabattiniSgtoCabral_EGRESO'",
	"'contVeh_CPCVillaLibertador_EGRESO'",
	"'contVeh_CPCVillaLibertador_INGRESO'",
	"'contVeh_CPCRuta20W_INGRESO'",
	"'contVeh_CPCRuta20W_EGRESO'",
	"'contVeh_CPCRuta20W_GiroIzqIngresoBarrioN'",
	"'contVeh_CPCRuta20E_INGRESO'",
	"'contVeh_CPCRuta20E_EGRESO'",
]

"""
 References ubicaciones/ubicacionesNA
 
 with data and active cameras
 contVeh_MaipuOlmosN_EGRESO2:	Av. Olmos y Av. Maipú	Vehículos que circulan por Av. Maipú y Av. Olmos y se dirigen hacia Esquiú (egreso)
 contVeh_ChacabucoIllia_NORTE:	Bv. Chacabuco y Bv. Illía - NORTE	Vehículos que circulan por Bv. Chacabuco y Bv. Illía hacia puente Maipú.
 contVeh_MaipuOlmosE_EGRESO:	Av. Olmos esq. Av. Maipú	Vehículo que circulan por Av. Olmos y Maipú hacia el puente 24 de Septiembre.
 contVeh_GuzmanSarmiento_NW:	Bv. Guzmán y Av. Sarmiento	Vehículos que circulan por Bv. Guzmán y Sarmiento hacia el norte.
 contVeh_PuenteSarmiento_INGRESO:	Pte. Sarmiento y Bv. Guzmán	Vechículos que circulan por puente Sarmiento, hacia el centro.
 contVeh_GuzmanSarmiento_SE: 	Bv. Guzmán y Av. Sarmiento	Vehículos que circulan por Bv. Guzmán y Sarmiento hacia Terminal de Ómnibus

 with data and no active cameras
 contVeh_CPCMonseñorS_Ingreso:	CPC Monseñor P. Cabrera - INGRESO	Vehículos que circulan por el CPC Monseñor P. Cabrera y se dirigen hacia nudo vial Cardeñoza (ingreso).
 contVeh_CPCMonseñorN_Egreso:	: 	CPC Monseñor P. Cabrera - EGRESO	Vehículos que circulan por el CPC Monseñor P. Cabrera y se dirigen hacia el norte de la Ciudad (egreso).
 contVeh_OctavioPintoSagradaFamilia_INGRESO:	Bajada del Cerro	Vehículo que circulan por bajada del Cerro hacia puente Tablada.
 contVeh_CaraffaOctavioPinto_INGRESO:	Av. Caraffa y Av. Octavio Pinto	Vehículos que circulan por Octavio Pinto e ingresan por Av. Caraffa, hacia Castro Barros.
 contVeh_CPCColonW_INGRESO:	CPC Colón - OESTE	Vehículos que circulan por el CPC Colón y se dirigen hacia el este de la Ciudad (ingreso).
 contVeh_CPCColonE_EGRESO:	CPC Colón - ESTE	Vehículos que circulan por el CPC Colón y se dirigen hacia el oeste de la Ciudad (egreso).
 contVeh_Nuevocentro_EGRESO:	Nuevocentro Shopping	Vehículos que circulan por Av. Duarte Quirós (pasando por Nuevocentro Shopping) hacia CPC Colón.
 contVeh_SabattiniPucara_EGRESO:	Sabattini y bajada Pucará	Vehículos que circulan por Av. Sabattini hacia Sargento Cabral.
 contVeh_SabattiniPucara_INGRESO:	Sabattini y bajada Pucará	Vehículos que circulan por Av. Sabattini hacia Bv. Illía.
 contVeh_SabattiniSgtoCabral_INGRESO:	Av. Sabattini y Sargento Cabral - OESTE	Vehículos que circulan por Av. Sabattini y Sargento Cabral y se dirigen hacia Parque Sarmiento (ingreso).
 contVeh_SabattiniSgtoCabral_EGRESO:	Av. Sabattini y Sargento Cabral - ESTE	Vehículos que circulan por Av. Sabattini y Sargento Cabral y se dirigen hacia el Arco de Córdoba (egreso).
 contVeh_CPCVillaLibertador_EGRESO:	CPC Villa Libertador - EGRESO	Vehículos que circulan por el CPC Villa Libertador y se dirigen hacia el peaje (egreso).
 contVeh_CPCVillaLibertador_INGRESO:	CPC Villa Libertador - INGRESO	Vehículo que circulan por el CPC Villa Libertador y se dirigen hacia el centro de la Ciudad (ingreso).
 contVeh_CPCRuta20W_INGRESO:	CPC Ruta 20 - OESTE	Vehículos que circulan por el CPC Ruta 20 y se dirigen hacia el este de la Ciudad (ingreso).
 contVeh_CPCRuta20W_EGRESO:	CPC Ruta 20 - OESTE	Vehículos que circulan por el CPC Ruta 20 y se dirigen hacia el oeste de la Ciudad (egreso).
 contVeh_CPCRuta20W_GiroIzqIngresoBarrioN:	CPC Ruta 20 - OESTE	Vehículos que circulan por el CPC Ruta 20 hacia el oeste y giran a la izquierda para igreso al barrio por Aviador Richardson (hacia el norte de Av. Fza. Aérea).
 contVeh_CPCRuta20E_INGRESO:	CPC Ruta 20 - ESTE	Vehículos que circulan por el CPC Ruta 20 y se dirigen hacia el este de la Ciudad (ingreso).
 contVeh_CPCRuta20E_EGRESO:	CPC Ruta 20 - ESTE	Vehículos que circulan por el CPC Ruta 20 y se dirigen hacia el oeste de la Ciudad (egreso).
"""

# Loops here

print(os.stat('2023.04.json'))
it=its[1] 
ubicacion = ubicaciones[0]
fecha = "'"+str(anios[-1])+"/"+str(meses[3]).zfill(2)+"'"


#print('añslfjasfdj',str(anios[0]), type(str(anios[0])))
#print(type(anios[-1]), type(meses[3]), str(meses[3]),  str(anios[-1])+"."+str(meses[3])
#      )

print(it, ubicacion, fecha)

# response
# --------
r = httpx.post(url, 
              #params=params,
              headers=headers,
              json=jsondata(it, fecha, ubicacion),
              )

# src: https://datagy.io/python-requests-json/
if r.status_code == httpx.codes.OK:
    rj = r.json()
    print(type(r.json()))
    name_file = str(anios[-1])+"."+str(meses[3]).zfill(2)
    print(name_file)
    to_json(json.dumps(rj, indent=2, ensure_ascii=False), name_file)
    #to_json(json.dumps(rj, indent=2, ensure_ascii=False).encode('utf8'), name_file)
    #print(json.dumps(rj, indent=2)) # salida bonita
    #print(type(rj['results'][0]['result']['data']))
    #print(rj['results'][0]['result']['data']['dsr'])
    #print(r.text)
