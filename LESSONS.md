# Lessons Learned: Prompting for Effective LLM Reasoning and Planning

This document summarizes key lessons and example prompts from the course notebooks.

## Lesson 1: Introduction to Prompting

**Key Learning**: Progressive prompt refinement significantly improves LLM output quality and relevance.

**Techniques**:
- Start with generic prompts
- Add professional roles for expertise
- Introduce concrete constraints for prioritization
- Request step-by-step reasoning

### Example Prompt Evolution

**Generic Prompt:**
```
System: You are a helpful assistant.
User: Give me a simple plan to declutter and organize my workspace.
```

**Role-Based Prompt:**
```
System: You are a certified professional organizer.
User: Give me a simple plan to declutter and organize my workspace.
```

**Constrained Prompt:**
```
System: You are a certified professional organizer. I have only 15 minutes, a $20 budget, and limited floor space; I want to keep sentimental items but maximize desk surface.
User: Give me a simple plan to declutter and organize my workspace.
```

---

## Lesson 2: Role-Based Prompting (Agent Personas)

**Key Learning**: Detailed persona specifications create more authentic and consistent AI responses.

**Techniques**:
- Define baseline role
- Add persona-specific attributes (personality, speech style, expertise)
- Specify tone and conversational style
- Test with Q&A format for consistency

### Example Prompt Evolution

**Baseline Role:**
```
System: Pretend you are Albert Einstein and answer my questions about your work and life.
User: Can you tell me about relativity?
```

**Enhanced with Persona Attributes:**
```
System: Pretend you are Albert Einstein and answer my questions about your work and life.

Adopt these persona characteristics:
- Personality: Curious, humble yet confident, slightly absentminded, with a playful sense of humor
- Speech style: German-accented English with occasional German phrases, uses metaphors and thought experiments to explain complex ideas
- Expertise: Revolutionary physics theories (relativity, photoelectric effect, mass-energy equivalence), philosophy of science, and pacifism
- Historical context: You lived 1879-1955, worked at the Swiss Patent Office early in your career, later taught at Princeton, left Germany when Hitler rose to power

Answer as if you are Einstein speaking in 1950, reflecting on your life and work. Only discuss information that would have been known to you in your lifetime.

User: Can you tell me about relativity?
```

---

## Lesson 3: Chain-of-Thought (CoT) Prompting

**Key Learning**: Explicit step-by-step reasoning instructions help LLMs analyze complex data and provide structured, logical responses.

**Techniques**:
- Add explicit "think step by step" instructions
- Provide structured analysis frameworks
- Request specific output formats (JSON, structured sections)
- Guide through multi-step reasoning processes

### Example Prompt

**Simple CoT:**
```
System: You are a meticulous Retail Demand Analyst. Your task is to analyze provided sales data and promotion schedules to identify and explain significant sales spikes for specific SKUs.

Think step by step.

User: Analyze the data provided below and hypothesize causes for any observed sales spikes.

[Sales data, promotions, weather, competitor pricing data]
```

**Developed CoT with Structured Output:**
```
System: You are a meticulous Retail Demand Analyst. Your task is to analyze provided sales data and promotion schedules to identify and explain significant sales spikes for specific SKUs.

Think in steps.

User: ## INSTRUCTIONS:
Analyze the data provided below and hypothesize causes for any observed sales spikes.

Instructions:
Identify the single largest spike and hypothesize its causes.

## OUTPUT FORMAT:
STRUCTURED ANALYSIS:
[Structured Analysis]

LARGEST SPIKE:
```json
{
    "date": "YYYY-MM-DD",
    "amount_before_increase": "X.XX",
    "amount_after_increase": "X.XX",
    "percentage_increase": "X.XX%",
    "causes": [
        "Cause 1",
        "Cause 2",
        "Cause 3"
    ]
}
```

## CONTEXT
[Sales data, promotions, weather, competitor pricing data]
```

---

## Key Takeaways

1. **Progressive Refinement**: Start simple, then add specificity (roles, constraints, structure)
2. **Role Definition**: Detailed persona specifications create more authentic AI behavior
3. **Explicit Reasoning**: Asking for step-by-step thinking improves analysis quality
4. **Structured Output**: Clear format requirements help ensure consistent, parseable responses
5. **Context Matters**: Providing relevant data and constraints guides the LLM toward useful outputs

