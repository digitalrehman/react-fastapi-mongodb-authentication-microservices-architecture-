def convert_objectid(document):
    document["_id"] = str(document["_id"])
    return document
