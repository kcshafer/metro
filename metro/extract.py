from metro.db.models import SObject
from metro.refs import TEMPORARILY_UNSUPPORTED, METADATA_OBJECTS
from metro.utils import is_installed_package_object

def extract_schema(engine):
    sobjects = []
    resp = engine.source_client.get_sobjects()
    unsupported_objects = TEMPORARILY_UNSUPPORTED + METADATA_OBJECTS
    
    print("***************** RETRIEVING SALESFORCE OBJECTS ****************")

    for r in resp:
        if r['queryable'] and r.get('name') not in unsupported_objects and not is_installed_package_object(r['name']):
            record_count = engine.source_client.count(r.get('name'))
            
            if record_count > 0:
                print('RETRIEVED ' + r.get('name'))
                s = SObject(name=r.get('name'), amount=record_count)
                engine.config_session.add(s)

    engine.config_session.commit()