#!/usr/bin/env python3

import wolframalpha as wra

app_id = "42Y669-3A4V8JE46Y"

client = wra.Client(app_id)

res = client.query('C47H70O3 + C4H6O2')

'''print(next(res.results).text)

for pod in res.pods:
  print(pod.results.text)'''

for pod in res.pods:
  if (pod.title == "Sample reactions"):
    print('H20 + HCl')
    for sub in pod.subpods:
      print(sub.plaintext)
