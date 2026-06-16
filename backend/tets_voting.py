from app.core.voting import VotingEngine
from app.schemas.schemas import AgentResult

engine = VotingEngine()

results = [
    AgentResult(
        success=True,
        category="Invoice",
        reasoning="Invoice data"
    ),
    AgentResult(
        success=True,
        category="Invoice",
        reasoning="Invoice data"
    ),
    AgentResult(
        success=True,
        category="Invoice",
        reasoning="Invoice data"
    ),
    AgentResult(
        success=True,
        category="News",
        reasoning="News article"
    ),
    AgentResult(
        success=False,
        error="503"
    )
]

result = engine.vote(
    page_number=1,
    results=results
)

print(result)