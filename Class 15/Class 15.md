`What You’ll Learn`

This class teaches you how modern developers work with AI, version control, and deployment tools.
By the end, you’ll be able to:
- Talk to AI properly using prompts
- Understand Git vs GitHub
- Use basic Git commands
- Deploy a website using Vercel
- Clone a website using AI prompts

### Notes

`Prompt Engineering (Talking to AI Properly)`

### What is a Prompt?

A prompt is the instruction you give to AI.

Bad Prompt
```
Make a website
```

Good Prompt
```
Create a responsive landing page using HTML and CSS for a fitness app with a hero section, features, and CTA button.
```

### Prompt Best Practices

- Be Clear
- Tell AI exactly what you want.

### Give Context

- Explain who you are and what you need.    
- `Example:
```
You are a frontend developer. Create a simple portfolio website for a beginner student.
```

### Break Big Tasks into Small Ones

AI works best step-by-step.
Instead of:
- `Build Netflix clone`

Do:
- `Create homepage layout`
- `Add movie cards`
- `Style using CSS`

---

`COT, TOT & Temperature`

### COT – Chain of Thought

Means: Ask AI to think step by step.

Example: Explain how Git works step by step in simple words.

Best for:

- Learning
- Debugging
- Understanding logic

### TOT – Tree of Thought

Means: Ask AI to give multiple solutions or paths.

Example: Give me 3 different ways to design a landing page.

Best for:

- Design ideas
- Brainstorming
- Creative work

### Temperature

Controls creativity level of AI.

- Low (0.2 – 0.4): Accurate, boring, safe
- Medium (0.5 – 0.7): Balanced
- High (0.8 – 1): Creative, risky

Example:

- Write a professional email (low temperature)
- Write a creative brand slogan (high temperature)

---

`Git vs GitHub`

### What is Git?

Git is a tool that runs on your computer. It helps you:

- Save versions of your code
- Track changes
- Go back in time if something breaks

> Git = Version control system

### What is GitHub?

GitHub is a website. It helps you:
- Store your Git projects online
- Share code with others
- Work in teams

> GitHub = Online storage for Git projects

### Simple Analogy

Git = Camera (takes snapshots)
GitHub = Google Drive (stores photos)

---

`Git Configuration (One-Time Setup)`

Before using Git, you must tell it who you are.

- Set Username
```markdown
git config --global user.name "[username]"
```

- Set Email
```markdown
git config --global user.email "[email]"
```

> This info appears in your commits.

- Check Git Configuration
```markdown
git config --list
```

---

`Vercel Deployment (Put Website Online)`

### What is Vercel?

Vercel lets you:
- Deploy websites
- Share live links
- Host frontend projects for FREE

### Used For

- HTML/CSS
- React
- Next.js

### Steps to Deploy on Vercel

- Push your code to GitHub
- Go to vercel.com
- Login using GitHub
- Click New Project
- Select your repository
- Click Deploy
- `🎉 Your website is now live!`

---

`Class Task`
### Create a clone of Shark Tank Pakistan's website
