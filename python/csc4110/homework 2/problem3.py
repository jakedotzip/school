log = "341johnbutters,445jakesmith,331stevmorrisy,341wrapopossum,445leavehilarious,331leavelice,341macaronibountiful,445diveaction,331mercurialdingdong,341languidfluther,445yelloutgoing,331aroundgaff,341virtualvisitor,445roachbarber,331journallug"
new_log = []

user = log.split(',')
for i in user:
  new_log.append(i[3:])
print(new_log)