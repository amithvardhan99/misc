# Creating a state that holds the transcribed data and the summary of the transcribed data. This data can be used for future reference.

from pydantic import BaseModel

class MeetingMinutesState(BaseModel):
    transcript: str = ""
    meeting_minutes_summary: str = ""

    