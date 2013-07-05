1.get the new db ddre/bdre (spiderdbx.py)    
2.decrease the db (using decrease.py get ddre-/bdre-)    
3.get the new doc (using get getnewdoc.py by comparing to the basedb final, get newdocdb)     
4.upload the new doc for mark (post.py  change the id)     
5.mark    
6.get the marked score to local db (get.py store to newdocdb)     
7.merge the newdocdb to basedb (merge.py  get final2)     
8.get the current MaxDCG (getMaxDcg reference the basedb)     
9.rewirte the ddre-/bdre- (getScore.py  write score into it refer basedb)     
10.caculate for dd/bb (caculate.py refer maxdcg&ddre-/bdre-  ->  bdRep/ddRep)     
11.view the report db in sqliteman or a django app in the web broser    
