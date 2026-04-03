Inspiration:
Current structural inspections often put engineers in dangerous, hard-to-reach environments. The inspiration behind StructurSense is to promote a human-centered approach to infrastructure maintenance. By using AI as a reliable assistant, we can analyze visual data before a human ever has to climb a bridge or scaffold. The goal is to keep inspectors safer and make the preliminary assessment process much faster and more accessible.

What it does:
StructurSense is a web-based dashboard where users can upload images of infrastructure, such as concrete pillars, road surfaces, or steel bridge girders. The app uses the Gemini API to scan the image for signs of structural distress, instantly flagging issues like fatigue cracking, concrete spalling, or steel corrosion. It then generates an accessible, plain-language safety report.To quantify the risk, the tool helps conceptualize a simplified Damage Index ($D$) based on the identified severity: D = \sum_{i=1}^{n} (w_i x s_i) where w_i represents the structural weight or importance of the component, and s_i is the AI-assessed severity of the identified defect.

How we built it:
We built the core logic using Python and integrated the gemini-2.5-flash model via Google AI Studio. Gemini's vast token limits and multimodal capabilities allowed us to feed it raw images alongside a strict prompt structure to return standardized, professional inspection reports. We rapidly prototyped the frontend using Streamlit to ensure a seamless image upload and reporting workflow.

Challenges we ran into:
With a tight hackathon time limit, the biggest challenge was fine-tuning the prompt engineering. Initially, the model occasionally struggled to distinguish between harmless superficial water stains and actual concrete spalling. We had to iterate quickly, refining our prompts to guide Gemini's vision model to look for specific textural and geometric cues associated with critical corrosion and cracking.

Accomplishments that we're proud of:
We are incredibly proud of taking a complex civil engineering challenge and turning it into a highly functional, user-friendly prototype in just a few hours. The accuracy of the multimodal analysis was impressive, successfully identifying rust and surface defects on our test images without requiring a custom-trained computer vision model.

What we learned:
We learned just how powerful the Gemini API is for zero-shot image classification and analysis tasks. By providing the right context and constraints to the model, we could extract actionable, domain-specific insights immediately.

What's next for StructurSense:
The immediate next step is expanding the model to handle continuous video streams. Ultimately, the long-term vision is to connect this AI backbone to drone feeds or augmented reality headsets for field inspectors, allowing them to see real-time, AI-generated overlays of structural health risks while they are on site.

Built With:
gemini-api,
github,
google-ai-studio,
mac-os,
python,
streamlit
