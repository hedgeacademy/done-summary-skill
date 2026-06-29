# Done Summary Example: Data Analysis

## Goal

Analyze a dataset and identify why a key metric changed.

## Who Did What

- User provided the dataset and business question.
- AI agent inspected schema, cleaned obvious data quality issues, calculated trend breaks, and summarized likely drivers.

## Why This Approach

The metric change could have come from volume, mix, data gaps, or calculation logic. Breaking the metric into components made the explanation more reliable.

## Final Result

The analysis identified the main driver, supporting segments, and a short list of caveats.

## Verification

- Row counts and date ranges were checked.
- Aggregations were compared against the raw data.
- Outliers and missing values were inspected.

## Pitfalls

One source table had missing records for the final period. The summary separated confirmed movement from incomplete-period noise.

## Risks And Open Items

The analysis should be rerun after the final period is complete.

## Next Step

Confirm whether the incomplete period should be excluded from the official report.

## Reusable Knowledge

Data analysis summaries should record grain, filters, denominators, missing data, and whether the latest period is complete.
