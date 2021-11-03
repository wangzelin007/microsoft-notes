[type](https://docs.python.org/3/library/typing.html)
Union type; Union[X, Y] is equivalent to X | Y and means either X or Y.
Optional[X] is equivalent to X | None (or Union[X, None]).
Dict(dict, MutableMapping[KT, VT])' -> KeyType, ValueType
```python
def __init__(
        self,
        *,
        name: Optional[str] = None,
        display_name: Optional[str] = None,
        display_description: Optional[str] = None,
        unit: Optional[str] = None,
        category: Optional[str] = None,
        aggregation_type: Optional[str] = None,
        supported_aggregation_types: Optional[List[str]] = None,
        supported_time_grain_types: Optional[List[str]] = None,
        fill_gap_with_zero: Optional[bool] = None,
        dimensions: Optional[List["MetricDimension"]] = None,
        source_mdm_namespace: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        runtime_version: Optional[Union[str, "RuntimeVersion"]] = "Java_8",
        cpu: Optional[int] = 1,
        **kwargs
    ):
    pass
```