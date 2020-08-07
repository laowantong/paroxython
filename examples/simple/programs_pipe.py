[
    {
        "operation": "impart",
        "data": [
            "01_hello_world.py",
            "02_input_name.py",
            "abstr/procedure",
            "appli/function",
            "flow",
        ],
    },
    {
        "operation": "exclude",
        "data": [
            "03_friends.py",
        ],
    },
    {
        "operation": "exclude",
        "data": [
            "type/number/floating_point/literal",
            ("type/sequence/tuple", "is not", "var/assignment/parallel"),
        ],
    },
    {
        "operation": "include",
        "data": [
            "var/assignment",
        ],
    },
    {
        "operation": "hide",
        "data": [
            "appli/function/builtin/print",
            r".*test.*\.py",
        ],
    },
]
