#!/usr/bin/env python
from random import randint
from pydub import AudioSegment
from pydub.utils import make_chunks
from pathlib import Path
from openai import OpenAI
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from state import MeetingMinutesState
from dotenv import load_dotenv
load_dotenv()
from meeting_minutes_crew.crew import MeetingMinutesCrew
from meeting_minutes_crew.tools.gmail_tool import SendEmailTool

import warnings
warnings.filterwarnings("ignore")

client = OpenAI()

#@Flow(state_class=MeetingMinutesState)
class MeetingMinutesFlow(Flow[MeetingMinutesState]):

    @start()
    def transcribe_meeting(self):
        audio_file = Path("earnings_call.wav")
        audio = AudioSegment.from_file(audio_file)
        chunks = make_chunks(audio, 60000)
        
        full_transcription = ""
        for i, chunk in enumerate(chunks):
            chunk.export("temp_chunk.wav", format="wav")
            with open("temp_chunk.wav","rb") as f:
                transcription = client.audio.transcriptions.create(model="whisper-1",file=f)
            full_transcription += transcription.text
            print(f"Transcribed chunk {i+1}/{len(chunks)}")
        
        self.state.transcript = full_transcription
        print("Transcription complete")
        print(self.state.transcript)
    
    @listen(transcribe_meeting)
    def generate_meeting_minutes(self):
        crew = MeetingMinutesCrew().crew()
        inputs = {"transcript": self.state.transcript}
        result = crew.kickoff(inputs=inputs)
        self.state.meeting_minutes_summary = result
        with open("meeting_minutes.md", "w") as f:
            f.write(result.raw)
        tool = SendEmailTool()
        tool.run(recipient="amithvardhangd3@gmail.com", subject="Meeting Minutes", body=self.state.meeting_minutes_summary)
        print("Minutes generated!")

if __name__ == "__main__":
    flow = MeetingMinutesFlow()
    flow.kickoff()
            

    """@start()
    def generate_sentence_count(self, crewai_trigger_payload: dict = None):
        print("Generating sentence count")

        # Use trigger payload if available
        if crewai_trigger_payload:
            # Example: use trigger data to influence sentence count
            self.state.sentence_count = crewai_trigger_payload.get('sentence_count', randint(1, 5))
            print(f"Using trigger payload: {crewai_trigger_payload}")
        else:
            self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = (
            PoemCrew()
            .crew()
            .kickoff(inputs={"sentence_count": self.state.sentence_count})
        )

        print("Poem generated", result.raw)
        self.state.poem = result.raw

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)


def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


def run_with_trigger():
    """
    """Run the flow with trigger payload."""
    """
    import json
    import sys

    # Get trigger payload from command line argument
    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    # Create flow and kickoff with trigger payload
    # The @start() methods will automatically receive crewai_trigger_payload parameter
    poem_flow = PoemFlow()

    try:
        result = poem_flow.kickoff({"crewai_trigger_payload": trigger_payload})
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the flow with trigger: {e}")


if __name__ == "__main__":
    kickoff()
"""