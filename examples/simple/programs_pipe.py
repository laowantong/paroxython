[
    {
        "operation": "impart",
        "data": [
            "01_hello_world.py",
            "02_input_name.py",
            "def/procedure",
            "call/function",
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
            ("type/sequence/tuple", "is not", "var/assignment/explicit/parallel"),
        ],
    },
    {
        "operation": "include",
        "data": [
            "var/assignment/explicit",
        ],
    },
    {
        "operation": "hide",
        "data": [
            "call/function/builtin/print",
            r".*test.*\.py",
        ],
    },
]
