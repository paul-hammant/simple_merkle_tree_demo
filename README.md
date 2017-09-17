CSV Date from https://raw.githubusercontent.com/tonmcg/County_Level_Election_Results_12-16/master/2016_US_County_Level_Presidential_Results.csv via wget.

After that, I ran:

```
python2 create_merkle_tree.py
```

That created directories and JSON documents for each voting district.

After that, I ran:

```
python2 update_merke_tree_hashes.py
```

That one just runs in a loop.  Sure that's not exactly friendly to the host machine, but this is only a proof of concept.