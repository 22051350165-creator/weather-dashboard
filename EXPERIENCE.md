### Part 4: Experience Documentation

---

- 1. Tool Selection Justification

For this project, I chose Cursor because I think it is the most practical tool for building a small application while still getting support from an AI coding assistant. Unlike regular code editors, Cursor doesn’t just autocomplete lines—it understands the whole project and gives suggestions that fit the structure of the application. Since my project required combining a Tkinter interface, API requests, and error handling, having a tool that could see the bigger picture made the process much easier for me.

Another reason I selected Cursor was the way it works with natural-language prompts. Instead of writing every part from scratch, I could simply explain what I wanted—like adding weather data, improving the layout, or fixing an error—and Cursor generated clean Python code that I could review and adjust. This saved a lot of time and helped understand the logic behind each part of the project. Overall, Cursor felt like the most supportive and efficient option for completing this assignment.

---

- 2. Development Process

During development, I used Cursor as a collaborative coding assistant. I began by prompting it to generate a basic Tkinter layout for a weather application. After that, I incrementally expanded the functionality by asking Cursor to add an API call, create weather condition mappings with emojis, implement exception handling, and update the GUI labels dynamically. Each time I wanted a change, I highlighted the relevant section of code and provided a direct instruction, which Cursor immediately rewrote.

The most effective prompts were specific instructions such as:

“Add detailed comments explaining each function for beginners.”
“Improve error handling for invalid city names and network failures.”
“Refactor the UI to make the layout cleaner and centered.”
“Add weather icons via emoji mapping.”

The development process took several iterations. The base working version of the application was generated within 2–3 iterations, while polishing the GUI, writing comprehensive comments, and refining documentation took around 5–7 more iterative improvements. Cursor consistently improved the project with each refinement prompt.

---

- 3. Challenges and Solutions

One of the main challenges I encountered was dealing with external dependencies—especially the requests library and the OpenWeatherMap API key. Initially, the application failed to run because the requests module was not installed on my system. Cursor helped by generating clear installation instructions, but I still had to run the pip install command manually.

Another challenge was designing a clean and user-friendly Tkinter layout. Cursor provided strong initial drafts, but some spacing, alignment, and resizing issues required manual adjustments. I modified padding values, rearranged widget placement, and expanded comments to make the code more readable.

Additionally, integrating error handling for invalid input and server errors required testing multiple edge cases. Cursor suggested good starting logic, but I refined the conditions manually to ensure the program remained stable even with network failures or incorrect city names.

Overall, the AI tool helped generate foundation code quickly, but careful testing and manual adjustments were necessary to produce a fully functional and polished final application.

---

- 4. Reflection

This project revealed how transformative vibe coding tools can be for software development. I was surprised by how effectively Cursor understood high-level instructions and produced cohesive, multi-file code structures with minimal effort. Instead of focusing on boilerplate or repetitive syntax, I was able to dedicate more time to design decisions, testing, and documentation.

Using Cursor significantly changed my workflow. Instead of writing everything from scratch, I worked more like a designer or director—describing features and improvements, reviewing AI-generated outputs, and adjusting what was necessary. This made development faster and more enjoyable.

I would absolutely consider using this tool for future projects, especially prototypes, learning exercises, and medium-complexity applications. Cursor reduces cognitive load and accelerates the implementation phase, although final polishing still benefits from human review.

Looking ahead, tools like Cursor may reshape software development by shifting the programmer’s role from writing code line-by-line to guiding AI agents that generate functional applications. This could increase productivity, reduce entry barriers, and redefine how digital products are created in both educational and professional environments.

---
