# Lessons Learned: Prompting for Effective LLM Reasoning and Planning

This document summarizes key lessons and example prompts from the course notebooks.

## Quick Example: System and User Prompts

LLM prompts typically consist of two parts:
- **System Prompt**: Defines the AI's role, behavior, and instructions (optional but recommended)
- **User Prompt**: Contains the actual question or task from the user

### What You'd Type in a Chat Interface

In chat interfaces like ChatGPT, you typically combine both into one message:

```
You are a helpful coding assistant. You explain code clearly and provide working examples.

Explain how Python list comprehensions work and provide a simple example.
```

However, when using the API, it's better to separate them for more control over the AI's behavior.

### Python Code Example

```python
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = OpenAI(
    base_url="https://openai.vocareum.com/v1",  # Or use OpenAI's endpoint
    api_key=os.getenv("VOCAREUM_API_KEY")
)

# Define prompts separately
system_prompt = "You are a helpful coding assistant. You explain code clearly and provide working examples."
user_prompt = "Explain how Python list comprehensions work and provide a simple example."

# Make API call - system and user are sent as separate messages
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},  # Sets behavior
        {"role": "user", "content": user_prompt}       # Your question
    ],
    temperature=0.7
)

# Get the response
answer = response.choices[0].message.content
print(answer)
```

---

## Pre-Lesson Exercise: Introduction to Prompting for LLM Reasoning and Planning

**Notebook**: `introduction-to-prompting-for-llm-reasoning-and-planning.ipynb`

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

## Lesson 1: Role-Based Prompting (Agent Personas)

**Notebook**: `lesson-1-role-based-prompting.ipynb`

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

**With Tone and Style Specifications:**
```
System: [Previous persona prompt]

Tone and style:
- Speak in a warm, grandfatherly manner with occasional philosophical tangents
- Use "you see" and "imagine, if you will" when explaining concepts
- Express wonder at the universe's mysteries
- Show humility about your achievements while being passionate about scientific inquiry
- Occasionally make self-deprecating jokes about your hair or poor memory for practical matters

User: Can you tell me about relativity?
```

---

## Lesson 2: Chain-of-Thought and ReACT Prompting

**Notebook**: `lesson-2-chain-of-thought-and-react-prompting-part-ii.ipynb`

**Key Learning**: ReACT (Reasoning + Acting) prompting enables LLMs to use external tools and iterate through complex problem-solving tasks.

**Techniques**:
- Structure prompts with THINK/ACT/OBSERVE pattern
- Define available tools and their usage
- Parse tool calls from model responses
- Implement iterative loops for multi-step reasoning

### ReACT Prompt Structure

```
System: You are a meticulous Retail Demand Analyst that can solve any TASK in a multi-step process using tool calls and reasoning.

## Instructions:
- You will use step-by-step reasoning by
    - THINKING the next steps to take to complete the task and what next tool call to take to get one step closer to the final answer
    - ACTING on the single next tool call to take
- You will always respond with a single THINK/ACT message of the following format:
    THINK:
    [Carry out any reasoning needed to solve the problem not requiring a tool call]
    [Conclusion about what next tool call to take based on what data is needed and what tools are available]
    ACT:
    [Tool to use and arguments]
- As soon as you know the final answer, call the `final_answer` tool in an `ACT` message.
- ALWAYS provide a tool call, after ACT:, else you will fail.

## Available Tools
* `calculator(expression: str)`: Perform an arithmetic calculation
* `get_sales_data()`: Get the sales data
* `call_weather_api(date: str)`: Get weather data for a specific date
* `final_answer(...)`: Return the final answer

User: TASK: Find the single largest sales spike according to the percentage increase with a short explanation for it based on factors such as weather.
```

### ReACT Loop Implementation

The ReACT pattern creates an iterative loop:
1. **THINK**: Model reasons about what to do next
2. **ACT**: Model calls a tool
3. **OBSERVE**: Tool returns results
4. Repeat until final answer is reached

---

## Lesson 3: Prompt Instruction Refinement

**Notebook**: `lesson-3-prompt-instruction-refinement.ipynb`

**Key Learning**: Iterative prompt refinement with clear definitions, guidelines, examples, and structured output formats significantly improves accuracy and consistency.

**Techniques**:
- Add clear role definitions
- Provide detailed context and definitions
- Include explicit guidelines for handling edge cases
- Specify structured output formats
- Add concrete examples

### Prompt Refinement Example

**Initial Prompt:**
```
Analyze the following recipe and determine whether it satisfies each dietary restriction in the list.
For each restriction, classify it as "satisfied", "not satisfied", or "undeterminable" based on the recipe information.

Recipe: [recipe]
Ingredients: [ingredients]
Dietary Restrictions to Check: [restrictions]

Please provide your response in JSON format.
```

**Refined Prompt:**
```
You are a dietary consultant specializing in food allergies and dietary restrictions.

Your task is to analyze the following recipe and determine whether it satisfies each dietary restriction in the list.
For each restriction, classify it as "satisfied," "not satisfied," or "undeterminable" based on the recipe information.

Important context and definitions for dietary restrictions:
- Vegetarian: No meat, poultry, fish, or seafood. May include eggs and dairy.
- Vegan: No animal products whatsoever, including meat, dairy, eggs, honey.
- Gluten-free: No wheat, barley, rye, or derivatives. Note that regular all-purpose flour contains gluten.
[... additional definitions ...]

Guidelines for your analysis:
- Mark a restriction as "satisfied" only if you are certain the recipe meets it.
- Mark a restriction as "not satisfied" if any ingredient clearly violates it.
- Mark a restriction as "undeterminable" if you lack sufficient information.
- For each classification, briefly explain your reasoning and identify specific ingredients that affect your decision.

Handling ambiguities:
- For "vegetable oil" or unspecified oil, consider it plant-based unless otherwise noted.
- Assume "broth" or "stock" matches the recipe's main protein unless specified.
[... additional ambiguity handling rules ...]

Example analysis for a simple recipe:
[Concrete example with expected output format]

Recipe to analyze: [recipe]
Ingredients: [ingredients]
Dietary Restrictions to Check: [restrictions]

Please format your response as a JSON object where:
- Each key is the name of a dietary restriction
- Each value is an object with properties:
  - "classification": "satisfied", "not satisfied", or "undeterminable"
  - "explanation": brief reasoning for your classification
  - "critical_ingredients": array of ingredients that determined your classification
```

---

## Lesson 4: Chaining Prompts for Agentic Reasoning

**Notebook**: `lesson-4-chaining-prompts-for-agentic-reasoning.ipynb`

**Key Learning**: Breaking complex tasks into sequential stages with gate checks creates robust, maintainable agentic systems.

**Techniques**:
- Divide complex tasks into discrete stages
- Use structured data validation (e.g., Pydantic models)
- Implement gate checks between stages
- Chain outputs from one stage as inputs to the next

### Prompt Chain Example: Auto Insurance Claim Triage

**Stage I: Information Extraction**
```
System: You are an auto insurance claim processing assistant. Your task is to extract key information from First Notice of Loss (FNOL) reports.

Format your response as a valid JSON object with the following keys:
- claim_id (str): The claim ID
- name (str): The customer's full name
- vehicle (str): The vehicle make, model, and year
- loss_desc (str): A concise description of the incident
- damage_area (list[str]): A list of damaged areas on the vehicle

Only respond with the JSON object, nothing else.

User: [FNOL text]
```

**Gate 1**: Validate extracted information using Pydantic models

**Stage II: Severity Assessment**
```
System: You are an auto insurance damage assessor. Your task is to evaluate the severity of vehicle damage and estimate repair costs.

Apply these carrier heuristics:
- Minor damage: Small dents, scratches, glass chips (cost range: $100-$1,000)
- Moderate damage: Single panel damage, bumper replacement, door damage (cost range: $1,000-$5,000)
- Major damage: Structural damage, multiple panel replacement, engine/drivetrain issues, total loss candidates (cost range: $5,000-$50,000)

Based on the claim information provided, determine:
1. Severity level (Minor, Moderate, or Major)
2. Estimated repair cost (in USD)

Format your response as a valid JSON object with the following keys:
- severity: One of "Minor", "Moderate", or "Major"
- est_cost: Numeric estimate of repair costs

Only respond with the JSON object, nothing else.

User: [Claim information from Stage I]
```

**Gate 2**: Validate cost range matches severity level

**Stage III: Queue Routing**
```
System: You are an auto insurance claim routing specialist. Your task is to determine the appropriate processing queue for each claim.

Use these routing rules:
- 'glass' queue: For Minor damage involving ONLY glass (windshield, windows)
- 'fast_track' queue: For other Minor damage
- 'material_damage' queue: For all Moderate damage
- 'total_loss' queue: For all Major damage

Format your response as a valid JSON object with the following keys:
- claim_id: Use the provided claim ID
- queue: One of "glass", "fast_track", "material_damage", or "total_loss"

Only respond with the JSON object, nothing else.

User: [Claim information + Severity assessment from Stages I and II]
```

**Gate 3**: Validate routing decision

### Benefits of Prompt Chaining

- **Modularity**: Each stage has a focused responsibility
- **Error Prevention**: Gate checks catch issues early
- **Maintainability**: Easy to update individual stages
- **Testability**: Each stage can be tested independently

---

## Lesson 5: Implementing LLM Feedback Loops

**Notebook**: `lesson-5-implementing-llm-feedback-loops.ipynb`

**Key Learning**: Iterative feedback loops enable LLMs to improve code generation and problem-solving through test-driven refinement.

**Techniques**:
- Generate initial solution
- Execute code and run tests
- Format test results as structured feedback
- Iteratively refine based on failures
- Continue until all tests pass or max iterations reached

### Feedback Loop Structure

**Initial Generation:**
```
System: You are an expert Python developer. Please write a Python function based on the following requirements:

[Task description with examples]

Write only the function surrounded by ```python and ``` without any additional explanations or examples.

User: [Task description]
```

**Feedback Iteration:**
```
System: You are an expert Python developer. You wrote a function based on these requirements:

[Task description]

Here is your current implementation:
```python
[Current code]
```

I've tested your code and here are the results:
[Formatted test results with pass/fail status, expected vs actual outputs, error messages]

Please improve your code to fix any issues and make sure it passes all test cases.
Write only the improved function without any explanation.

User: [Feedback message]
```

### Feedback Format Example

```
Test Results: 8 passed, 4 failed

Failed Test Cases:

Test #6:
  Inputs: ([1, 3, 4], 'median')
  Expected: 3
  Actual: None

Test #7:
  Inputs: ([1, 2, 3, 5], 'median')
  Expected: 2.5
  Actual: None

[... additional failed tests ...]
```

### Benefits of Feedback Loops

- **Incremental Improvement**: Model fixes issues one at a time
- **Test-Driven**: Ensures correctness through automated testing
- **Self-Correction**: Model learns from its mistakes
- **Robustness**: Handles incomplete or evolving requirements

---

## Key Takeaways

1. **Progressive Refinement**: Start simple, then add specificity (roles, constraints, structure)
2. **Role Definition**: Detailed persona specifications create more authentic AI behavior
3. **Explicit Reasoning**: Asking for step-by-step thinking improves analysis quality
4. **Structured Output**: Clear format requirements help ensure consistent, parseable responses
5. **Context Matters**: Providing relevant data and constraints guides the LLM toward useful outputs
6. **Tool Integration**: ReACT patterns enable LLMs to use external tools for complex tasks
7. **Iterative Refinement**: Feedback loops improve code quality and problem-solving accuracy
8. **Modular Design**: Chaining prompts creates maintainable, testable agentic systems
9. **Gate Checks**: Validation between stages prevents error cascades
10. **Examples and Guidelines**: Concrete examples and clear guidelines significantly improve prompt effectiveness
