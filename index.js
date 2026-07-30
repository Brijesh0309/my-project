import { GoogleGenAI } from "@google/genai";
import dotenv from "dotenv";
import readline from "readline";

dotenv.config();
console.log("Working Directory:", process.cwd());
console.log("API Key:", process.env.GEMINI_API_KEY);

const ai = new GoogleGenAI({
  apiKey: process.env.GEMINI_API_KEY,
});

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

async function askGemini(prompt) {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-2.5-pro", // Agar ye model error de to apna working model use karo
      contents: prompt,
    });

    console.log("\n🤖 AI:", response.text);
  } catch (error) {
    console.error("\n❌ Error:", error.message);
  }

  startChat();
}

function startChat() {
  rl.question("\n👤 You: ", async (input) => {
    if (input.toLowerCase() === "exit") {
      console.log("\n👋 Goodbye!");
      rl.close();
      return;
    }

    await askGemini(input);
  });
}

console.log("================================");
console.log("     QA AI Agent Started");
console.log("Type 'exit' to quit.");
console.log("================================");

startChat();