"""
Refactrings: 

1. Introduce explanatory variable (aka, extract variable) for repeated expression.
2. Extract a method, or use the Python API. Hint: Python has a 'statistics' module.
3. Replace nested condition (if ... elif ...) with guard clauses

DON'T
- introduce named constants for threshold values, like UNHEALTHY = 150
- make the code more complex by introducing a bunch of local variables


"""
def air_quality(data) -> str:
    """Return an air quality rating based on observed data.

    :param data: list of air quality index (AQI) readings from a location
    :returns: String description of air quality
    """
    # check extreme cases
    if not data:
        return "no data"
    elif max(data) <= 10:
        return "very good"
    elif max(data) > 200:
        return "dangerously unhealthy"

    # otherwise, quality is based on average reading
    if sum(data)/len(data) <= 50:
        return "good"
    elif sum(data)/len(data) <= 100:
        return "moderate"
    elif sum(data)/len(data) <= 150:
        return "poor"
    else:
        return "unhealthy"
