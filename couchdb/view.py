#!/usr/bin/env python

from cloudant import couchdb
from coudant.document import Document
import sys

#username, password, database
assert len(sys.argv) == 4 
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

host = "http://localhost:5984"

#view document
_doc = {
  "_id":"_design/gene_target",
  "views":{
    "counts":{
      "map":"function(doc) { emit(doc.primary_target,1); }",
      "reduce":"function(k,v) {return sum(v);}",
    }
  }
}

with couchdb(username,password,url=host) as client:
  db=client[database]
  view = Document(db,"_design/gene_target")
  if view.exists():
     print "Exists"
  else:
    try:
      view = db.create_document(_doc)
    except:
      print "Error"
  result = db.get_view_result("_design/most_severe_consequences","counts",group=True)
  for item in result:
    print res
      