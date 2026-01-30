### 🔹 What is a Chatbot?

A **chatbot** is a software application that simulates **human conversation** using text or voice.

It can:

* Answer questions
* Provide support
* Automate tasks
* Assist users 24/7

#### 📌 Types of Chatbots

1. Rule-based (if/else logic)
2. Retrieval-based (predefined answers)
3. AI/LLM-based (dynamic, intelligent responses)

---

### 🔹 Chatbot Architecture (Basics)

```
User → Input → Processing → Model/Logic → Response → User
```

#### Components

* UI (chat interface)
* Backend (server)
* NLP/LLM model
* Database (optional)
* Memory/context

---

### 🔹 Dialog Flow (Theoretical)

Dialog flow defines **how a conversation moves step-by-step**.

#### 📌 Key Concepts

* Intent → what user wants
* Entity → important data (name, date, product)
* Context → conversation memory
* Response → system reply

#### 📌 Flow Example

```
User: I want to book a call
Bot: What date?
User: Tomorrow
Bot: What time?
Bot: Booking confirmed
```

#### 📌 Flow Types

* Linear flow
* Decision tree
* State machine
* Context-aware (AI)

---

### 🔹 Rule-Based vs AI Chatbot

| Feature      | Rule-Based | AI-Based   |
| ------------ | ---------- | ---------- |
| Logic        | Fixed      | Dynamic    |
| Flexibility  | Low        | High       |
| Setup        | Easy       | Medium     |
| Intelligence | Limited    | Smart      |
| Use Case     | FAQs       | Assistants |

---

### 🔹 Simple Chatbot Using Google Gen API + Python

### Step 1: Install Library

```
pip install google-generativeai
```

### Step 2: Setup API Key

Get API key from Google AI Studio.

```
export GOOGLE_API_KEY="your_key_here"
```

(Windows: use set instead of export)

### Step 3: Basic Python Chatbot

```python
import google.generativeai as genai

# Configure API
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")

print("Chatbot started. Type 'exit' to stop.
")

chat = model.start_chat(history=[])

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input)
    print("Bot:", response.text)
```

### 🔹 How It Works

* Start chat session
* Send user message
* Model generates response
* Print reply
* Repeat loop

---

### 🔹 Add Improvements (Next Steps)

* Add memory/history
* Save chats to database
* Add system prompt
* Add web UI (Flask / FastAPI)
* Add input sanitization
* Deploy to cloud

---

### 🔹 Real-World Use Cases

* Customer support bot
* FAQ bot
* AI tutor
* Personal assistant
* Lead qualification bot

---

### 🔹 Class 28 Takeaway

* Chatbots simulate conversations
* Dialog flow controls logic
* AI models make them smarter
* Python + Gen API can build one quickly

---

✅ End of Notes
