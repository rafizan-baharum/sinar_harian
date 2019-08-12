from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph

## specify the connection like
connection = "postgres://sinar_harian:sinar_harian@127.0.0.1/sinar_harian"

##Generate graph of connected database
graph = create_schema_graph(metadata=MetaData(connection),
                 show_datatypes=False,
                 show_indexes=False,
                 rankdir='LR',
                 concentrate=False)

##Generate png image
graph.write_png('dbschema.png')