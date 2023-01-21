testcase = [[[  "3",
                "B b1 p4 4",
                "B b2 p3 3",
                "B b3 p2 2"],
            [   "b1: $4 -> p4",
                "b2: $3 -> p3",
                "b3: $2 -> p2"]],

            [[  "3",
                "B b1 p4 4",
                "B b1 p3 3",
                "B b2 p1 1"],
            [   "b1: $7 -> p3 p4",
                "b2: $1 -> p1"]],

            [[  "3",
                "B b2 p1 1",
                "B b1 p1 2",
                "B b3 p1 3"],
            [   "b1: $0",
                "b2: $0",
                "b3: $3 -> p1"]],

            [[  "3",
                "B b3 p3 1",
                "B b1 p3 2",
                "B b1 p2 3"],
            [   "b1: $5 -> p2 p3",
                "b3: $0"]],
                
            [[  "4",
                "B b1 p4 4",
                "B b2 p3 3",
                "W b1 p4",
                "B b3 p2 2"],
            [   "b1: $0",
                "b2: $3 -> p3",
                "b3: $2 -> p2"]],
                
            [[  "4",
                "B b1 p4 4",
                "B b1 p3 3",
                "B b2 p1 1",
                "W b2 p1"],
            [   "b1: $7 -> p3 p4",
                "b2: $0"]],
            
            [[  "4",
                "B b2 p1 1",
                "B b1 p1 2",
                "B b3 p1 3",
                "W b3 p1"],
            [   "b1: $2 -> p1",
                "b2: $0",
                "b3: $0"]],
                
            [[  "5",
                "B b3 p3 1",
                "B b1 p3 2",
                "B b1 p2 3",
                "B b1 p1 1",
                "W b1 p2"],
            [   "b1: $3 -> p1 p3",
                "b3: $0"]],
                
            [[  "8",
                "B b1 p1 2",
                "B b2 p1 2",
                "B b3 p1 2",
                "B b3 p2 99",
                "B b2 p2 2",
                "B b1 p2 2",
                "W b3 p2",
                "B b1 p4 4"],
            [   "b1: $6 -> p1 p4",
                "b2: $2 -> p2",
                "b3: $0"]]]