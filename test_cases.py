TEST_CASES = [
    {
        "question": "What is the translation boundary principle?",
        "must_contain": ["translation boundary", "integration layer", "application layer"],
        "must_not_contain": [],
        "ideal_answer": (
            "The translation boundary separates the integration layer from "
            "the application layer. JSON parsing belongs in the application "
            "layer not the integration layer. The integration layer stays "
            "payload-agnostic by passing the raw JSON string unchanged."
            )
        },
    {
        "question": "How does YAJL parse JSON on IBMi?",
        "must_contain": ["YAJL", "tree-node", "sanitise"],
        "must_not_contain": [],
        "ideal_answer": (
        "In IBMi event-driven integration using the Infoview connector pattern, "
        "YAJL parsing follows six steps: sanitise the JSON string first to replace "
        "invalid IBMi characters, convert to tree-node structure using YAJL services, "
        "navigate to key nodes using relative paths, iterate child nodes using DoWhile "
        "loops with GetFirstChild and GetNextChild until null, handle simple vs complex "
        "attributes using If-ElseIf logic, and handle arrays with nested DoWhile loops. "
        "All values received via the connector arrive as character strings requiring "
        "explicit type conversion."
        )
    },
    {
        "question": "What are the common mistakes in IBMi event integration?",
        "must_contain": ["security", "configuration", "null", "scaling"],
        "must_not_contain": [],
        "ideal_answer": (
        "Based on a production implementation using Infoview connectors "
        "between IBMi and Kafka, five documented mistakes are: "
        "1. Underestimating security and user profile authority setup for RPC calls. "
        "2. Silent success masking missing configuration — components work individually "
        "but end-to-end flow fails. "
        "3. Assuming null handling agreement stays agreed without schema validation. "
        "4. Connector parameter extraction more complex than initial prototype suggested. "
        "5. Scaling not considered early enough — constraints surface as integrations grow."
        )
    },
    {
        "question": "What are the integration patterns for connecting IBMi to modern applications?",
        "must_contain": ["Infoview", "REST", "CDC", "MQ"],
        "must_not_contain": [],
        "ideal_answer": (
            "Four integration patterns exist for IBMi modernisation: "
            "Confluent Kafka with Infoview connectors for event-driven decoupled integration, "
            "REST API from RPG for synchronous request-response, "
            "Journal-based CDC for non-invasive data replication, "
            "and IBM MQ bridge for existing MQ environments."
        )
    },
    {
        "question": "When should I use journal-based CDC instead of the Infoview connector pattern?",
        "must_contain": ["CDC", "journal", "non-invasive", "data"],
        "must_not_contain": [],
        "ideal_answer": (
            "Use journal-based CDC when cloud applications need IBMi data for analytics "
            "or AI training without triggering business logic, and when no IBMi code changes "
            "are permitted. The Infoview connector pattern is better when bi-directional "
            "event-driven integration with business logic invocation is needed."
        )
    }
]