# Solution

We get to control one of the sensors, so let's see what sort of outputs we have with different inputs:

```
python .\submission_helper.py 10  
Better buckle up. Class isn't canceled. The sensor values were [ 2 10 16  9] with a predicted wind speed of 12.99 knots.
python .\submission_helper.py 20
Better buckle up. Class isn't canceled. The sensor values were [46 20 18 14] with a predicted wind speed of 10.35 knots.
python .\submission_helper.py 30
Better buckle up. Class isn't canceled. The sensor values were [20 30  5  6] with a predicted wind speed of 6.88 knots.
python .\submission_helper.py 5 
Better buckle up. Class isn't canceled. The sensor values were [33  5 16 10] with a predicted wind speed of 18.79 knots.
python .\submission_helper.py 4
Better buckle up. Class isn't canceled. The sensor values were [53  4  4  5] with a predicted wind speed of 18.48 knots.
python .\submission_helper.py 2
Better buckle up. Class isn't canceled. The sensor values were [51  2 12 13] with a predicted wind speed of 25.46 knots.
python .\submission_helper.py 0
Better buckle up. Class isn't canceled. The sensor values were [45  0  0 14] with a predicted wind speed of 11.94 knots.
python .\submission_helper.py -5
```

Looks like increasing temperature doesn't help but decreasing actually increases wind speed!