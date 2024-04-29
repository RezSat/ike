# Ike: An AI-Based Answer Engine

"Okay, yes, there is an API key in here, but I'll remove it or revoke it after the end of the Google AI Hackathon. Until then, the API key can sit here, no big deal."

### Content

- Project Description
- Setup Guide
- Preview Images
- Video Demos
- Known Issues

## Project Description

As the name suggests, Ike is an AI-powered Answer Engine. However, this Answer Engine is specifically tailored for the G.C.E. O/L specification. Now, explaining what that entails might be as tricky hehe, so let me walk you through my process to shed some light on it.

First, I went on a digital treasure hunt and snagged the freely available textbooks from the [Educational Publication Department](http://www.edupub.gov.lk/BooksDownload.php) of Sri Lanka. I grabbed the Grade-9, Grade-10, and Grade-11 textbooks since the G.C.E. O/L examination relies heavily on these three grades. These textbooks covered subjects like:

- Mathematics
- Science
- History
- Geography
- Business & Accounting Studies
- I.C.T.
- Health Science
- Civic
- Entrepreneurship Studies

I then performed the daring feat of extracting the text directly from these PDFs, no fancy refinement, just a straightforward conversion from PDF to text. After splitting them up, I stored them with FAISS, used langchain, and magically transformed them into a question-answer bot. I also tapped into Google Translate for Sinhala-English translation because, hey, I want students to use it in Sinhala too!

So, in a nutshell, Ike is essentially a customized answer engine for GCE O/L specifications.

#### WHY?

Well, mostly because there's a scarcity of online resources, especially in Sinhala. My grand plan is to refine the datasets further, add more data including O/L past papers and answers, so it covers an even wider array of question-answer formats. But for now, here's what I've got.

## Setup Guide

Tested on WSL (Ubuntu) and Python 3.10.12, use a Virtual Environment.

```bash
git clone https://github.com/RezSat/ike
cd ike
-----> add the google api key inside config.py (for now its already there)
pip install -r requirements.txt
python app.py
```

That's it! Just run it and visit the provided URL, e.g., http://127.0.0.1:5000.

DEMO: https://yehanwasura.pythonanywhere.com/

## Preview Images

![Home Page](https://i.ibb.co/q97fJYg/Screenshot-2024-04-29-003833.png)
![Subject English Page](https://i.ibb.co/VLfxLdZ/Screenshot-2024-04-29-003854.png)
![Subject Sinhala Page](https://i.ibb.co/k8xH9qS/Screenshot-2024-04-29-003906.png)
![Ask English Page](https://i.ibb.co/GssjmsQ/Screenshot-2024-04-29-003923.png)
![Answer English Page](https://i.ibb.co/Tk6wzXy/Screenshot-2024-04-29-003959.png)

## Video Demos

Coming Soon!

## Known Issues

Yes, there are a few known issues that should be as easy to solve as finding your socks in the morning, but alas, time was not on my side. My computer decided to take a vacation and gave me a headache to fix it. Anyways, here are some issues:

- Not properly rendering answers for the Sinhala version
- The image answer option is taking a snooze (heheh)
- Sometimes it decides to crash with a Reason: OTHER (yeah, I don't really get what that is either.)