data=[
           {"dept": "IT", "roll":1, "sal": 50000},
          {"dept": "IT", "roll":2, "sal": 60000},
          {"dept": "HR", "roll":1, "sal": 40000},
           {"dept": "HR", "roll":2, "sal": 20000}
        ]
stats={}
for entry in data:
        d=entry["dept"]
        s=entry["sal"]
        if d not in stats:
                stats[d]={"min":s, "max":s}
        else:
                stats[d]["min"]=min(stats[d]["min"],s)
                stats[d]["max"]=max(stats[d]["max"],s)

print(stats)                 
                
