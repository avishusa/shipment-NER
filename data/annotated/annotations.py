"""
Annotated training examples for the shipment NER model.

Format per example:
    (text, [(entity_text, label), ...])

No hardcoded offsets. Offsets are computed automatically
at export time by the data exporter.
"""

ANNOTATED_EXAMPLES = [

    # --- CHAT examples ---
    (
        "Customer: Hi, can you tell me the status of shipment SHP-1042?\n"
        "Agent: Sure! SHP-1042 departed Chicago this morning.\n"
        "Customer: When will it arrive in Houston?\n"
        "Agent: ETA is March 28. There was a slight delay due to weather hold.",
        [
            ("SHP-1042",     "SHIPMENT_ID"),
            ("Chicago",      "ORIGIN"),
            ("Houston",      "DESTINATION"),
            ("March 28",     "ETA"),
            ("weather hold", "DELAY_REASON"),
        ]
    ),

    (
        "Customer: What is the waybill number for my order?\n"
        "Agent: Your waybill is WB-8821 and the equipment ID is BNSF-442201.",
        [
            ("WB-8821",    "WAYBILL_ID"),
            ("BNSF-442201","EQUIPMENT_ID"),
        ]
    ),

    (
        "Customer: Is the grain shipment on track?\n"
        "Agent: Yes, 3 carloads of grain are in transit from Memphis to Dallas.\n"
        "Agent: Total weight is 42 tons. Status is in transit.",
        [
            ("3 carloads", "CARLOADS"),
            ("grain",      "COMMODITY"),
            ("Memphis",    "ORIGIN"),
            ("Dallas",     "DESTINATION"),
            ("42 tons",    "WEIGHT"),
            ("in transit", "STATUS"),
        ]
    ),

    # --- EMAIL examples ---
    (
        "Waybill WB-8821 has been assigned to your shipment SHP-2091.\n"
        "Equipment BNSF-442201 is loaded with grain (42 tons, 3 carloads).\n"
        "The shipment departed Kansas City and is en route to Dallas.\n"
        "Estimated arrival is March 22. No delays at this time.",
        [
            ("WB-8821",     "WAYBILL_ID"),
            ("SHP-2091",    "SHIPMENT_ID"),
            ("BNSF-442201", "EQUIPMENT_ID"),
            ("grain",       "COMMODITY"),
            ("42 tons",     "WEIGHT"),
            ("3 carloads",  "CARLOADS"),
            ("Kansas City", "ORIGIN"),
            ("Dallas",      "DESTINATION"),
            ("March 22",    "ETA"),
        ]
    ),

    (
        "Dear Team, shipment SHP-3301 is currently on hold.\n"
        "The delay is caused by a mechanical issue at the Chicago yard.\n"
        "New estimated arrival in Houston is April 3.",
        [
            ("SHP-3301",         "SHIPMENT_ID"),
            ("on hold",          "STATUS"),
            ("mechanical issue", "DELAY_REASON"),
            ("Chicago",          "ORIGIN"),
            ("Houston",          "DESTINATION"),
            ("April 3",          "ETA"),
        ]
    ),

    (
        "This message confirms delivery of auto parts weighing 18000 lbs.\n"
        "Shipment SHP-7712 arrived at Atlanta on schedule.\n"
        "Equipment TTGX-998871 carried 2 carloads from Nashville.",
        [
            ("auto parts",   "COMMODITY"),
            ("18000 lbs",    "WEIGHT"),
            ("SHP-7712",     "SHIPMENT_ID"),
            ("Atlanta",      "DESTINATION"),
            ("on schedule",  "STATUS"),
            ("TTGX-998871",  "EQUIPMENT_ID"),
            ("2 carloads",   "CARLOADS"),
            ("Nashville",    "ORIGIN"),
        ]
    ),

    # --- VOICE examples ---
    (
        "Speaker 1: Can you pull up the details on waybill WB-9910?\n"
        "Speaker 2: Yes, waybill WB-9910 covers shipment SHP-3301, "
        "carrying auto parts out of Memphis.\n"
        "Speaker 1: What is the destination?\n"
        "Speaker 2: It is heading to Atlanta. About 18000 lbs, 2 carloads.",
        [
            ("WB-9910",    "WAYBILL_ID"),
            ("SHP-3301",   "SHIPMENT_ID"),
            ("auto parts", "COMMODITY"),
            ("Memphis",    "ORIGIN"),
            ("Atlanta",    "DESTINATION"),
            ("18000 lbs",  "WEIGHT"),
            ("2 carloads", "CARLOADS"),
        ]
    ),

    (
        "Speaker 1: What is the current status of SHP-5501?\n"
        "Speaker 2: SHP-5501 is delayed. "
        "There is a track obstruction near Kansas City.\n"
        "Speaker 1: When do we expect it in Chicago?\n"
        "Speaker 2: New ETA is end of week.",
        [
            ("SHP-5501",           "SHIPMENT_ID"),
            ("delayed",            "STATUS"),
            ("track obstruction",  "DELAY_REASON"),
            ("Kansas City",        "ORIGIN"),
            ("Chicago",            "DESTINATION"),
            ("end of week",        "ETA"),
        ]
    ),

    (
        "Speaker 1: Confirm the commodity and weight for equipment TTGX-112233.\n"
        "Speaker 2: Equipment TTGX-112233 is carrying chemicals, roughly 30 tons.\n"
        "Speaker 2: It departed from Houston bound for Kansas City. "
        "Status is in transit.",
        [
            ("TTGX-112233", "EQUIPMENT_ID"),
            ("chemicals",   "COMMODITY"),
            ("30 tons",     "WEIGHT"),
            ("Houston",     "ORIGIN"),
            ("Kansas City", "DESTINATION"),
            ("in transit",  "STATUS"),
        ]
    ),
]