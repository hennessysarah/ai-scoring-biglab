# ai-scoring-biglab
Scripts for Autobiographical Interview (Levine et al., 2002) scoring procedures (semi-automated), for use in large lab settings (30+ scorers, spanning multiple months with regular check-ins). 

Note: see Klus et al., 2025 and associated HuggingFace page for fully automated AI Scoring procedures. 

General steps used in Hennessy et al. studies on music-evoked nostalgia:

Step 1: Data collection (audio recorded)
Step 2: Transcription (auto via Zoom or other)
Step 3: Transcription Quality Check

Step 4: **Blinding** (blind memories so they no long contain information regarding participant ID, age group, experimental condition, session number). Blinding is run from a single "edited" (QCed) folder using _memory_blinder.py_ and a "secret scoring key". 

Step 5: **Sort**. This step assigns memories to each researcher for the week, based on a scoring key. Run _raw_sorter.py_ from the edited_renamed folder for a given set. Then "personal folders" are uploaded to researcher-facing site (i.e., google drive). 

Step 6: **Manual Scoring**. researchers manually score memories, using keyboard shortcuts. Two scorers per  memory. 

Step 7: **Auto Scoring**. Initial spreadsheets are made using _scoreAI_multisub_personal.py_, which counts scores and generates one spreadsheet per memory (two scorers in each spreadsheet). RAs then compare scores and reconcile. 

Step 8: **Final scoring**. After reconcilliation, run _scoreAI_doublesheet.py_ to run final scores and collapse across scorers, unblinding memories based on scoring key. Then, formal stats analysis continues. 




