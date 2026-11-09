```python
from scipy.stats import chisquare

# Observed frequencies
observed = [18, 22, 27, 33]

# Expected frequencies
expected = [25, 25, 25, 25]

# Calculate chi-square statistic
chi_square, p_value = chisquare(
    f_obs=observed,
    f_exp=expected
)

print("Observed Frequencies:", observed)
print("Expected Frequencies:", expected)
print("Chi-Square Value:", round(chi_square, 2))
print("P-Value:", round(p_value, 4))

# Interpret the result
if p_value < 0.05:
    print("Reject the null hypothesis.")
    print("The difference is statistically significant.")
else:
    print("Fail to reject the null hypothesis.")
    print("The difference is not statistically significant.")
```
