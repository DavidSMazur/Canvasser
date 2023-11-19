## Inspiration 🌟
Canvas layouts are a universal problem. Our team, hailing from multiple nationalities, bonded over our common frustration with unnavigable Canvas layouts. 😵

From scattered assignment files 📂 to unorganized submission slots, **Canvas can be confusing**. The solution? For students to be able to talk with Canvas and get the **precise** answer they need at lightning speed ⚡. More importantly, we provide critical accessibility support for students. 🎓

## What it does 🚀
Canvassist is a personalized assistant for all Canvas needs. Students can navigate to Canvassist, select their course, and begin asking questions specific to each coursework! Our integrated AI 🤖 contains all pertinent information about student coursework such as assignments and syllabus and will accurately answer any questions presented. Additionally, we cut down inefficiency by allowing students to submit assignments directly from Canvassist. Simply navigate to the submission page, select your coursework, and a list of available submissions will be available to choose and _instantly submit_. ✅

## How we built it 🔨
To bring this innovative web application to life, we incorporated a diverse technology stack that seamlessly integrates various components. Our software's front-end is developed using **Streamlit**, a diverse and resourceful Python library that allows for dynamic user interaction and seamless API integration 🌐. On the back-end, we used **MongoDB** as a vector database for our prompt as well as canvas information embed. We used **Langchain** to embed prompts and assignment data to and compare them using the **OpenAI API**. From the comparison, we return a response to the front end using **Fast API**.

## Challenges we ran into 🏃‍♂️💨
In the development of Canvassist, challenges emerged as we grappled with embedding assignments into MongoDB using FastAPI, navigating its steep learning curve. Identifying assignment names for direct student submissions proved intricate and required collaborative problem-solving. Through persistent exploration and shared insights, we overcome these obstacles, streamlining assignment storage and submission processes. Lessons learned emphasized the importance of collaborative problem-solving and continual exploration in mastering FastAPI's complexities. Ultimately, these challenges became opportunities for growth, contributing to the development of a robust and feature-rich Canvassist application.

## What we learned 🤔
On the technical front, we learned everything from front end Streamlit to LangChain LLM Agents. Even more importantly, this was half our team's first hackathon; although we have learned how to learn our entire lives, I can say with confidence that I have never learned so much in 24 hours. MHacks really taught us how to learn quickly and effectively for application.

## What's next for Canvassist 🌈
Canvassist will integrate submission directly into chat using LLM agents to determine the exact submission slot for each assignment. Furthermore, we would also like to integrate our features into other classroom learning tools such as Google classroom and D2L. Confusing educational pages is a problem that persists across the globe; We hope to expand our tool to break down the educational barriers and democratize education for all. 🎓
