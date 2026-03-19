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
            ("WB-8821",     "WAYBILL_ID"),
            ("BNSF-442201", "EQUIPMENT_ID"),
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
            ("auto parts",  "COMMODITY"),
            ("18000 lbs",   "WEIGHT"),
            ("SHP-7712",    "SHIPMENT_ID"),
            ("Atlanta",     "DESTINATION"),
            ("on schedule", "STATUS"),
            ("TTGX-998871", "EQUIPMENT_ID"),
            ("2 carloads",  "CARLOADS"),
            ("Nashville",   "ORIGIN"),
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
            ("SHP-5501",          "SHIPMENT_ID"),
            ("delayed",           "STATUS"),
            ("track obstruction", "DELAY_REASON"),
            ("Kansas City",       "ORIGIN"),
            ("Chicago",           "DESTINATION"),
            ("end of week",       "ETA"),
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

    # --- Additional CHAT examples ---
    (
        "Customer: Can you check on shipment SHP-8801?\n"
        "Agent: SHP-8801 is currently delayed at the Dallas yard.\n"
        "Agent: The delay is due to a track obstruction. New ETA is April 10.",
        [
            ("SHP-8801",          "SHIPMENT_ID"),
            ("delayed",           "STATUS"),
            ("Dallas",            "ORIGIN"),
            ("track obstruction", "DELAY_REASON"),
            ("April 10",          "ETA"),
        ]
    ),

    (
        "Agent: Shipment SHP-4421 has been delivered to Kansas City.\n"
        "Agent: Equipment RAIL-556677 carried 5 carloads of chemicals.\n"
        "Customer: Great, what was the total weight?\n"
        "Agent: Total weight was 75 tons.",
        [
            ("SHP-4421",    "SHIPMENT_ID"),
            ("Kansas City", "DESTINATION"),
            ("RAIL-556677", "EQUIPMENT_ID"),
            ("5 carloads",  "CARLOADS"),
            ("chemicals",   "COMMODITY"),
            ("75 tons",     "WEIGHT"),
        ]
    ),

    (
        "Customer: What is waybill WB-3310 carrying?\n"
        "Agent: WB-3310 is assigned to auto parts from Nashville to Atlanta.\n"
        "Agent: Status is in transit. ETA is March 31.",
        [
            ("WB-3310",    "WAYBILL_ID"),
            ("auto parts", "COMMODITY"),
            ("Nashville",  "ORIGIN"),
            ("Atlanta",    "DESTINATION"),
            ("in transit", "STATUS"),
            ("March 31",   "ETA"),
        ]
    ),

    (
        "Customer: Is there any delay on SHP-6612?\n"
        "Agent: Yes, SHP-6612 has a weather hold near Memphis.\n"
        "Agent: Equipment BNSF-119922 is standing by. New ETA is April 5.",
        [
            ("SHP-6612",     "SHIPMENT_ID"),
            ("weather hold", "DELAY_REASON"),
            ("Memphis",      "ORIGIN"),
            ("BNSF-119922",  "EQUIPMENT_ID"),
            ("April 5",      "ETA"),
        ]
    ),

    (
        "Agent: Confirmed. Shipment SHP-7733 departed Houston this morning.\n"
        "Agent: Carrying grain, 6 carloads, total 90 tons.\n"
        "Agent: Destination is Kansas City. Status is in transit.",
        [
            ("SHP-7733",    "SHIPMENT_ID"),
            ("Houston",     "ORIGIN"),
            ("grain",       "COMMODITY"),
            ("6 carloads",  "CARLOADS"),
            ("90 tons",     "WEIGHT"),
            ("Kansas City", "DESTINATION"),
            ("in transit",  "STATUS"),
        ]
    ),

    # --- Additional EMAIL examples ---
    (
        "Please be advised that shipment SHP-9901 is currently on hold.\n"
        "Equipment TTGX-445566 has a mechanical issue at the Nashville yard.\n"
        "We expect to resume transit to Chicago by April 7.",
        [
            ("SHP-9901",         "SHIPMENT_ID"),
            ("on hold",          "STATUS"),
            ("TTGX-445566",      "EQUIPMENT_ID"),
            ("mechanical issue", "DELAY_REASON"),
            ("Nashville",        "ORIGIN"),
            ("Chicago",          "DESTINATION"),
            ("April 7",          "ETA"),
        ]
    ),

    (
        "Waybill WB-5521 has been issued for shipment SHP-1133.\n"
        "Commodity: steel coils. Weight: 55 tons, 4 carloads.\n"
        "Origin is Pittsburgh. Destination is Dallas. ETA March 29.",
        [
            ("WB-5521",     "WAYBILL_ID"),
            ("SHP-1133",    "SHIPMENT_ID"),
            ("steel coils", "COMMODITY"),
            ("55 tons",     "WEIGHT"),
            ("4 carloads",  "CARLOADS"),
            ("Pittsburgh",  "ORIGIN"),
            ("Dallas",      "DESTINATION"),
            ("March 29",    "ETA"),
        ]
    ),

    (
        "Shipment SHP-2244 has been delivered successfully to Atlanta.\n"
        "Equipment RAIL-887766 carried lumber weighing 38 tons.\n"
        "Departed from Memphis on March 14. No delays reported.",
        [
            ("SHP-2244",    "SHIPMENT_ID"),
            ("Atlanta",     "DESTINATION"),
            ("RAIL-887766", "EQUIPMENT_ID"),
            ("lumber",      "COMMODITY"),
            ("38 tons",     "WEIGHT"),
            ("Memphis",     "ORIGIN"),
        ]
    ),

    (
        "This is to inform you that waybill WB-6634 covers 2 carloads of grain.\n"
        "Shipment SHP-3355 is en route from Houston to Nashville.\n"
        "Current status is in transit. Estimated arrival is April 2.",
        [
            ("WB-6634",    "WAYBILL_ID"),
            ("2 carloads", "CARLOADS"),
            ("grain",      "COMMODITY"),
            ("SHP-3355",   "SHIPMENT_ID"),
            ("Houston",    "ORIGIN"),
            ("Nashville",  "DESTINATION"),
            ("in transit", "STATUS"),
            ("April 2",    "ETA"),
        ]
    ),

    # --- Additional VOICE examples ---
    (
        "Speaker 1: Give me the status on SHP-4466.\n"
        "Speaker 2: SHP-4466 is delivered. It arrived in Dallas yesterday.\n"
        "Speaker 1: And the equipment?\n"
        "Speaker 2: Equipment BNSF-334411 handled the load. 3 carloads of lumber.",
        [
            ("SHP-4466",    "SHIPMENT_ID"),
            ("delivered",   "STATUS"),
            ("Dallas",      "DESTINATION"),
            ("BNSF-334411", "EQUIPMENT_ID"),
            ("3 carloads",  "CARLOADS"),
            ("lumber",      "COMMODITY"),
        ]
    ),

    (
        "Speaker 1: What is causing the delay on waybill WB-7743?\n"
        "Speaker 2: There is a mechanical issue with equipment TTGX-221100.\n"
        "Speaker 2: The shipment SHP-5577 is currently on hold in Memphis.\n"
        "Speaker 1: When do we expect it to reach Chicago?\n"
        "Speaker 2: New ETA is end of week.",
        [
            ("WB-7743",          "WAYBILL_ID"),
            ("mechanical issue", "DELAY_REASON"),
            ("TTGX-221100",      "EQUIPMENT_ID"),
            ("SHP-5577",         "SHIPMENT_ID"),
            ("on hold",          "STATUS"),
            ("Memphis",          "ORIGIN"),
            ("Chicago",          "DESTINATION"),
            ("end of week",      "ETA"),
        ]
    ),

    (
        "Speaker 1: Confirm the commodity on SHP-8899.\n"
        "Speaker 2: SHP-8899 is carrying chemicals out of Houston.\n"
        "Speaker 2: 4 carloads, roughly 48 tons. Heading to Kansas City.\n"
        "Speaker 1: Status?\n"
        "Speaker 2: In transit, no issues.",
        [
            ("SHP-8899",    "SHIPMENT_ID"),
            ("chemicals",   "COMMODITY"),
            ("Houston",     "ORIGIN"),
            ("4 carloads",  "CARLOADS"),
            ("48 tons",     "WEIGHT"),
            ("Kansas City", "DESTINATION"),
            ("In transit",  "STATUS"),
        ]
    ),

    (
        "Speaker 1: Has SHP-1122 left Atlanta yet?\n"
        "Speaker 2: Yes, SHP-1122 departed Atlanta this morning.\n"
        "Speaker 2: Waybill WB-9981 covers the load. Auto parts, 22 tons.\n"
        "Speaker 1: Destination and ETA?\n"
        "Speaker 2: Heading to Nashville. ETA is March 30.",
        [
            ("SHP-1122",   "SHIPMENT_ID"),
            ("Atlanta",    "ORIGIN"),
            ("WB-9981",    "WAYBILL_ID"),
            ("Auto parts", "COMMODITY"),
            ("22 tons",    "WEIGHT"),
            ("Nashville",  "DESTINATION"),
            ("March 30",   "ETA"),
        ]
    ),

    (
        "Speaker 1: I need the full details on equipment RAIL-003344.\n"
        "Speaker 2: RAIL-003344 is assigned to shipment SHP-6678.\n"
        "Speaker 2: Carrying steel coils from Pittsburgh to Dallas.\n"
        "Speaker 2: Weight is 60 tons, 5 carloads. Status is in transit.",
        [
            ("RAIL-003344", "EQUIPMENT_ID"),
            ("SHP-6678",    "SHIPMENT_ID"),
            ("steel coils", "COMMODITY"),
            ("Pittsburgh",  "ORIGIN"),
            ("Dallas",      "DESTINATION"),
            ("60 tons",     "WEIGHT"),
            ("5 carloads",  "CARLOADS"),
            ("in transit",  "STATUS"),
        ]
    ),

    (
        "Speaker 1: Is there a weather hold on any shipments out of Chicago?\n"
        "Speaker 2: Yes, SHP-7790 and SHP-7791 are both on hold.\n"
        "Speaker 2: Weather hold expected to lift by April 4.\n"
        "Speaker 1: What commodity?\n"
        "Speaker 2: Both are carrying grain. About 30 tons each.",
        [
            ("weather hold", "DELAY_REASON"),
            ("Chicago",      "ORIGIN"),
            ("SHP-7790",     "SHIPMENT_ID"),
            ("on hold",      "STATUS"),
            ("April 4",      "ETA"),
            ("grain",        "COMMODITY"),
            ("30 tons",      "WEIGHT"),
        ]
    ),

]