import pandas as pd

myitemsdataset = {
  'cars': ["ricebags", "Dalbag", "salt"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(myitemsdataset)

print(myvar)
